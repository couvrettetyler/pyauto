'''This is the __init__ file that will load the pyauto.* things'''

import os
import sys

from .highlevel import Bench, launch_gui
from .measuments import TestPlan

dirname = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(dirname,'inst'))

for directory in os.listdir(os.path.join(dirname,'inst')):
    if os.path.isdir(os.path.join(dirname, 'inst', directory)):
        sys.path.append(os.path.join(dirname, 'inst', directory))

__all__ = ['Bench', 'launch_gui', 'TestPlan']

#launch_gui()
