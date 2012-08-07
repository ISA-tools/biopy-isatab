#!/usr/bin/env python
"""Setup file and install script for deploying the stem cell discovery engine.
"""
from setuptools import setup, find_packages

setup(name = "biopy-isatab",
      version = "0.1.1",
      author = "Brad Chapman",
      author_email = "chapmanb@50mail.com",
      description = "Python parser for ISAtab, a biological file format for experimental metadata",
      license = "MIT",
      url = "https://github.com/ISA-tools/biopy-isatab",
      namespace_packages = ["bcbio"],
      packages = find_packages(),
      scripts = [],
      install_requires = [
      ])
