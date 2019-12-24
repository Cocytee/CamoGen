# learning base and statistical work
# Egien values, avergage stats, pop stats and Dicriminant Analysis

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import sklearn as skl

class TerrainStat:
	def __init__(self):
		self.Size = 0
		self.Average = []
		self.Set = []
	def setSize(self):
		self.Size = len(self.Set)*len(self.Set[0])
	def addSet(self,Stat):
		self.Set.append(Stat)
	def setAvg(self):
		self.Average = mean(self.Set)

#folder reading (file list + min size)
#image normalization (ratio + resolution)

def imageFFT(file):
	img = cv.imread(file,0)
	f = np.fft.fft2(img)
	fshift = np.ftt.fftshift(f)
	magnitude_spectrum = 20*np.log(np.abs(fshift))
	return magnitude_spectrum

#terrain stat building