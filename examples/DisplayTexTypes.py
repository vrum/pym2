#! /usr/bin/python
from m2 import *

#Dictionary for Texture types
TextureTypes = { 0 : "Hardcoded" , 1 : "Body/Clothes" , 2 : "Items", 3 : "ArmorReflect?", 6 : "Hair/Beard",
8 : "Tauren fur", 9 : "Inventory Art 1", 10 : "quillboarpinata", 11 : "Skin for creatures or gameobjects 1",
12 : "Skin for creatures or gameobjects 2" ,13 : "Skin for creatures or gameobjects 3", 14 : "Inventory Art 2"} 

#open m2
m2 = M2File("HumanMale.m2")
#iterate through textures
for i in m2.textures:
	print "Type is " + TextureTypes[i.type]#print texture type
	print i.name#print texture filename