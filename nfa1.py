#!/usr/bin/python

# Nicholas LaRosa
# CSE 30151
# Project 1

import sys
import re
import os
import math
from NFA import NFA

if len(sys.argv) != 2:
	raise Exception('Usage: nfa.py <nfa_description>\n')

location = sys.argv[1]

ourNFA = NFA( 'nfa1' )

ourNFA.processFile( location )

ourNFA.getInput()

