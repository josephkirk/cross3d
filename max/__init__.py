import os
from cross3d.enum import Enum, EnumGroup

import external

# Define some constants that are needed internally for Studiomax
class _StudiomaxAppData(Enum): pass
class StudiomaxAppData(EnumGroup):
	AltMtlIndex = _StudiomaxAppData(1108)
	AltPropIndex = _StudiomaxAppData(1110)

def init():
	
	# Making sure we can import the layer.
	import MaxPlus as mp
	
	# Importing the layer's classes.
	import studiomaxapplication
	import studiomaxscene