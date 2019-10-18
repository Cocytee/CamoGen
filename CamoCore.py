# learning base and statistical work
# Egien values, avergage stats, pop stats and Dicriminant Analysis

#need multivariate stats , numpy, stats and opencv package
import cv2 as ocv
import numpy as np
import sklearn as skl
import matplotlib.pyplot as plt

class TerrainStat:
    def __init__(self):
    	self.Size = 0
		self.Average = []
		self.Set = []
	def setSize(self,nb)
		self.Size = nb
	def addSet(self,Stat)
		self.Set.append(Stat)
	def setAvg(self)
		self.Average = mean(self.Set)

def imageInfo(file,disp=False)
	#open file
	#process it
	#display it if needed

#terrainInfo
	# process & disp (AvegrageImage)
	# process & disp (AvegrageFFT)

#SaveTerrainStats
	# save (AverageFFT + FFT_Array)

#GlobalEigen
	# process (AllTerrainEigenValue)
	# save (Eigen)

#GlobalDisplay
	# process & disp DA of all TerrainStats

#CamoGen
	#Use Eigen to generate Camo 
	#Transform at the good resolution