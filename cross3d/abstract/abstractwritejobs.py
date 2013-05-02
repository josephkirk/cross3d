##
#   :namespace  blur3d.api.abstract.abstractwritejobs
#
#   :remarks    [desc::commented]
#   
#   :author     enoch@blur.com
#   :author     Blur Studio
#   :date       07/10/12
#

import os
from blur3d import api


class AbstractWriteJobs(list):

	def add(self, job):
		self.append(job)

	def filesExist(self):
		for job in self:
			if not os.path.exists(job.fileName()):
				return False
		return True


# register the symbol
api.registerSymbol('WriteJobs', AbstractWriteJobs, ifNotFound=True)