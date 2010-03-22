#! /usr/bin/python

from skin import *

#Create Dictionary for Translating Ids
GeosetTypes = { "00" : "Hairstyles", "01" : "Facial1", "02" : "Facial2", "03" : "Facial3",
"04" : "Bracers", "05" : "Boots", "06" : "Unknown1", "07" : "Ears", "08" : "Wristbands", "09" : "Kneepads",
"10" : "Unknown2", "11" : "Pants", "12" : "Tabard", "13" : "Trousers/Kilt", "14" : "Unknown3",
"15" : "Cape", "16" : "Unknown4", "17" : "Eyeglows", "18" : "Belt" } 

#Open SkinFile
sk = SkinFile("VrykulMale00.skin")
#Iterate through the Geosets
for i in sk.mesh:
	s = str(i.mesh_id)#Convert the GeosetId to a string
	j = len(s)#Get the Length of the string
	if (j<3):#If it's only two digits...
		s = "00"#the Id is 00
	elif(j<4):#if it's length is <4, then it has only one digit
		s =  "0" + s[0]
	else:#get the two important digits
		s =  s[0:2]
	print str(i.mesh_id) +" is " + GeosetTypes[s]#print mesh_id and it's translation
	
	