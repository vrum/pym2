TextureTypes = { 0 : "Hardcoded" , 1 : "Body/Clothes" , 2 : "Items", 3 : "ArmorReflect?", 6 : "Hair/Beard",
8 : "Tauren fur", 9 : "Inventory Art 1", 10 : "quillboarpinata", 11 : "Skin for creatures or gameobjects 1",
12 : "Skin for creatures or gameobjects 2" ,13 : "Skin for creatures or gameobjects 3", 14 : "Inventory Art 2"} 

GeosetTypes = { "00" : "Hairstyles", "01" : "Facial1", "02" : "Facial2", "03" : "Facial3",
"04" : "Bracers", "05" : "Boots", "06" : "Unknown1", "07" : "Ears", "08" : "Wristbands", "09" : "Kneepads",
"10" : "Unknown2", "11" : "Pants", "12" : "Tabard", "13" : "Trousers/Kilt", "14" : "Unknown3",
"15" : "Cape", "16" : "Unknown4", "17" : "Eyeglows", "18" : "Belt" } 

tex_type = { 0 : 0, 1 : 1, 2:2, 3:3, 4:6, 5:8,6:9,7:10,8:11,9:12,10:13,11:14}

type_tex = { 0 : 0, 1 : 1, 2:2, 3:3, 6:4,8:5,9:6,10:7,11:8,12:9,13:10,14:11}

attachment_types = { 0:"Mountpoint/Left Wrist", 1:"Right Palm", 2:"Left Palm", 3:"Right Elbow", 4:"Left Elbow", 5:"Right Shoulder", 6:"Left Shoulder",
7:"Right Knee", 8:"Left Knee", 9:"Unk1",10:"Unk2",11:"Helmet",12:"Back",13:"Unk3",14:"Unk4",15:"Bust1",16:"Bust2",17:"Breath",18:"Name",19:"Ground",
20:"Top of Head",21:"Left Palm 2", 22:"Right Palm 2",23:"Unk5",24:"Unk6",25:"Unk7",26:"Right Back Sheath",27:"Left Back Sheath",28:"Middle Back Sheath",
29:"Belly",30:"Left Back",31:"Right Back",32:"Left Hip Sheath",33:"Right Hip Sheath",34:"Bust3",35:"Right Palm 3",36:"Unk8",37:"demolishervehicle1",
38:"demolishervehicle2",39:"vehicle seat 1",40:"vehicle seat 2",41:"vehicle seat 3",42:"vehicle seat 4",43:"Unk9",44:"Unk10",45:"Unk11",46:"Unk12",
47:"Unk13",48:"Unk14",49:"Unk15"}

LightTypes = {0:"Directional Light",1:"Point Light"}

KeyBoneTypes = {-1:"None", 0 :"ArmL", 1: "ArmR", 2 :"ShoulderL", 3 :"ShoulderR", 4: "SpineLow", 5: "Waist", 6: "Head", 7 :"Jaw", 8: "IndexFingerR", 9: "MiddleFingerR", 10: "PinkyFingerR", 11:"RingFingerR", 12 :"ThumbR", 13 :"IndexFingerL", 14 :"MiddleFingerL", 15 :"PinkyFingerL", 16: "RingFingerL", 17: "ThumbL", 18: "$BTH", 19: "$CSR", 20: "$CSL", 21: "_Breath", 22 :"_Name", 23 :"_NameMount", 24 :"$CHD", 25 :"$CCH", 26 :"Root", 27 :"Wheel1", 28 :"Wheel2", 29 :"Wheel3", 30 :"Wheel4", 31 :"Wheel5", 32: "Wheel6", 33: "Wheel7", 34: "Wheel8" }

def makeZeroTerminated(name):	
	name.encode("cp1252")
	if len(name) == 0:
		name = "\0"
	if name[len(name)-1] != "\0":
			name += "\0"
	return name
