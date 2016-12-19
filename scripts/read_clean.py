# -*- coding: utf-8 -*-
"""
Author: Tim Boomer
Title: Read and Clean Doggetts 1848/49 Directory OCR Text Output
"""

import os
import pandas as pd

os.chdir("C:/Users/tboom_000/Documents/Personal/Projects/Doggetts/source")
with open ("./doggettsnewyorkc1848dogg_djvu.txt") as f:
    raw = f.readlines()

# Remove non-directory text lines.
# Remove all blank lines

# Flag lines for removal with the initial text sequence "ZZY"

# Flag all lines from beginning of file to "Names too late for insertion"

# Repeat 1 to 3 until the end of file:

# 1. Skip lines until a line in all caps that is out of alphabetical sequence. This
# is the beginning of advertising text

# 2. Flag lines until a line with exactly 3 all cap characters is found. This is a
# column header for directory entries.

# 3. Flag header lines: Current line up to the next line that is not a column header
# or page number.
