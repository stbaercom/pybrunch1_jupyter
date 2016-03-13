from __future__ import print_function # For 2.7, it may help...

from IPython.display import display, Audio, Image, Math, HTML, SVG
from ipywidgets import interact, interactive, fixed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections
import os.path
import ipywidgets


from IPython import version_info as ipython_version_info
from sys import version_info as python_version_info

print("Python Version: {}".format (python_version_info))
print("Jupyter Version: {}".format(ipython_version_info))
print("Python Name: {}".format(sys.version.split("|")[1]))