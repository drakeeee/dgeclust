## Copyright (C) 2012-2013 Dimitrios V. Vavoulis
## Computational Genomics Group (http://bioinformatics.bris.ac.uk/)
## Department of Computer Science
## University of Bristol

################################################################################

import numpy  as np

################################################################################

class CountData(object):
    def __init__(self, counts, exposures = None, classes = None):
        self.counts    = counts.values.T
        self.libSizes  = self.counts.sum(1)
        self.exposures = self.libSizes / np.double(self.libSizes.max()) if exposures is None else exposures
        self.classes   = np.arange(self.counts.shape[0])                if classes   is None else classes 
    
################################################################################
