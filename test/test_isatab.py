"""Tests for parsing and extracting information from ISA-Tab formatted metadata.
"""
import os
import unittest

from bcbio import isatab

class IsatabTest(unittest.TestCase):
    def setUp(self):
        self._dir = os.path.join(os.path.dirname(__file__), "isatab")

    def test_basic_parsing(self):
        """Test general parsing of an example ISA directory.
        """
        work_dir = os.path.join(self._dir, "BII-I-1")
        rec = isatab.parse(work_dir)
        assert rec.metadata["Investigation Identifier"] == "BII-I-1"
        assert len(rec.ontology_refs) == 6
        assert rec.ontology_refs[2]["Term Source Name"] == "UO"
        assert len(rec.publications) == 1
        assert rec.publications[0]["Investigation Publication DOI"] == "doi:10.1186/jbiol54"

        assert len(rec.studies) == 2
        study = rec.studies[0]
        assert study.metadata["Study File Name"] == "s_BII-S-1.txt"
        assert len(study.assays) == 3
        assert study.assays[0].metadata["Study Assay File Name"] == "a_metabolome.txt"
        study = rec.studies[1]
        assert study.nodes['NZ_0hrs_Grow_1'].metadata["organism"] == \
               ["Saccharomyces cerevisiae (Baker's yeast)"]
        assert study.assays[0].nodes['E-MAXD-4-raw-data-426648783.txt'
                                     ].metadata["ArrayExpress Accession"] == \
                                     ["E-MAXD-4"]

    def test_minimal_parsing(self):
        """Parse a minimal ISA-Tab file without some field values filled in.
        """
        work_dir = os.path.join(self._dir, "minimal")
        rec = isatab.parse(work_dir)
        assert len(rec.publications) == 0
        assert len(rec.metadata) == 0

        assert len(rec.studies) == 1
        assert len(rec.studies[0].design_descriptors) == 0

        sname = "C2C12 sample1 rep3"
        study = rec.studies[0]
        assay_node = study.assays[0].nodes["AFFY#35C.CEL"]
        assert assay_node.metadata["Sample Name"] == [sname]
        assert study.nodes[sname].metadata["strain"] == ["C3H"]

    def test_nextgen_parsing(self):
        """Parse ISA-Tab file representing next gen sequencing data
        """
        work_dir = os.path.join(self._dir, "BII-S-3")
        rec = isatab.parse(work_dir)
        assay = rec.studies[0].assays[0]
        assert assay.metadata['Study Assay Technology Platform'] == '454 Genome Sequencer FLX'
        assert assay.nodes.has_key("ftp://ftp.ncbi.nih.gov/pub/TraceDB/ShortRead/"
                                   "SRA000266/EWOEPZA01.sff")

    def test_get_genelists(self):
        """Identify derived genelists available in ISA-Tab experiment
        """
        work_dir = os.path.join(self._dir, "genelist")
        rec = isatab.parse(work_dir)
        study = rec.studies[0]
        assay = study.assays[0]
        assay_node = assay.nodes["KLS1nature.CEL"]
        study_node = study.nodes[assay_node.metadata["Sample Name"][0]]
        assert "16862118-Figure2bSRAS.txt" in assay_node.metadata["Derived Data File"]
        expects = ["Mus musculus (Mouse)", "C57BL/6", "bone marrow"]
        attrs = ["Organism", "strain", "Organism Part"]
        for attr, expect in zip(attrs, expects):
            assert study_node.metadata[attr] == [expect]
