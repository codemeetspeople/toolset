"""In this module toolset package appends to system path for easy import."""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolset'))
