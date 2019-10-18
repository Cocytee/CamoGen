# create a session storing the camo and the current setting values
# interacting with GUI
# camocore init possible

#display console and lauching camo_init

#Session Class 
	#storing Setting Classes and CamoImg
	#try / tests
	#running things
class Session:
    def __init__(self, pset, cset, sset, cc):
		self.ProcSetting = pset
		self.CamoSetting = cset
		self.SaveSetting = sset
		self.CamoCurrent = cc

