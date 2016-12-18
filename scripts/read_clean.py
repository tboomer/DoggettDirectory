# -*- coding: utf-8 -*-
"""
Author: Tim Boomer
Title: Read and Clean Doggetts 1848/49 Directory OCR Text Output
"""

import os

os.chdir("C:/Users/tboom_000/Documents/Personal/Projects/Doggetts/source")
with open ("./doggettsnewyorkc1848dogg_djvu.txt") as f:
    raw = f.readlines()

# Remove non-directory text lines
