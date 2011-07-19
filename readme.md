#### Python Parser for ISA-Tab

This is a python parser for extracting information from ISA-Tab
formatted metadata. Usage is:

          from bcbio import isatab
          rec = isatab.parse(isatab_metadata_directory)

The returned record matches the general Investigation/Study/Assay
structure of ISATab. The top level ISATabRecord` object
contains information about the investigation, along with study
information as `ISATabStudyRecord` objects. Each record has assay
information in `ISATabAssayRecord` sub-objects.

The output is described in more detail in the parser module:

https://github.com/ISA-tools/biopy-isatab/blob/master/bcbio/istab/parser.py

and the test directory contains example of use and information
extraction:

https://github.com/ISA-tools/biopy-isatab/blob/master/test/test_isatab.py

More information about ISATab:

- General info: <http://isa-tools.org>
- Twitter: [@isatools](http://twitter.com/isatools)
- IRC: [irc://irc.freenode.net/#isatab](irc://irc.freenode.net/#isatab)
- Development blog: <http://isatools.wordpress.com>
