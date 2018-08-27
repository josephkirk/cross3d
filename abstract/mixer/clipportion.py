##
#	\namespace	cross3d.abstract.clipportion
#
#	\remarks	The AbstractClipPortion class provides a base implementation of
#				a cross-application interface to a portion of a clip.
#
#	\author		willc
#	\author		Blur Studio
#	\date		10/15/15
#

import cross3d
from cross3d import abstractmethod

class AbstractClipPortion(object):
	"""The AbstractClipPortion class provides a base implementation of a
		cross-application interface to a portion of a clip within a layer mixer.

	Attributes:
		end: The end of the used region, in global frames.
		start: The start of the used region, in global frames.
		clip: The Clip of which this ClipPortion is a portion.
	"""
	def __init__(self, clip, start, end):
		"""Initializes ClipPortion.

		Args:
			clip(Clip): The clip that this ClipPortion is a portion of.
			start(int): The start of the region, in global frames.
			end(int): The end of the region, in global frames.
		"""
		super(AbstractClipPortion, self).__init__()
		self._start = start
		self._end = end
		self._clip = clip

	@classmethod
	def fromTrackPortion(cls, tp, clip):
		"""Initializes a ClipPortion instance from a TrackPortion and Clip."""
		return cls(clip, tp.start, tp.end)

	@property
	def clip(self):
		"""The associated Clip."""
		return self._clip
	@clip.setter
	def clip(self, value):
		self._clip = value

	@property
	def end(self):
		"""The end of the region, in global frames."""
		return self._end
	@end.setter
	def end(self, value):
		self._end = value
	
	@property
	def start(self):
		"""The start of the region, in global frames."""
		return self._start
	@start.setter
	def start(self, value):
		self._start = value

	@property
	def sourceEnd(self):
		"""The number of frames from the beginning of the clip's file at which
		this ClipPortion ends."""
		return None

	@property
	def sourceStart(self):
		"""The number of frames from the beginning of the clip's file at which
		this ClipPortion starts."""
		return None

################################################################################

# register the symbol
cross3d.registerSymbol('ClipPortion', AbstractClipPortion)
