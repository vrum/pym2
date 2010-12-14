#! /usr/bin/python

from ctypes import *
import os

#temp, delete later
GENERIC_WRITE =  0x40000000
CREATE_ALWAYS = 2

class StormLib:
	def __init__(self):
		if os.name == "posix":
			stormlib = cdll.LoadLibrary("StormLib/libStorm.so")

			self.CreateFile = getattr(stormlib,"_Z10CreateFilePKcjjPvjjS1_")
			self.DeleteFile = getattr(stormlib,"_Z10DeleteFilePKc")
			self.WriteFile = getattr(stormlib,"_Z9WriteFilePvPKvjPjS_")

			self.SFileAddFile = getattr(stormlib,"_Z12SFileAddFilePvPKcS1_j")
			self.SFileAddWave = getattr(stormlib,"_Z12SFileAddWavePvPKcS1_jj")
			self.SFileHasFile = getattr(stormlib,"_Z12SFileHasFilePvPKc")
			self.SFileReadFile = getattr(stormlib,"_Z13SFileReadFilePvS_jPjS_")
			self.SFileAddFileEx = getattr(stormlib,"_Z14SFileAddFileExPvPKcS1_jjj")
			self.SFileCloseFile = getattr(stormlib,"_Z14SFileCloseFilePv")
			self.SFileFindClose = getattr(stormlib,"_Z14SFileFindClosePv")
			self.SFileGetLocale = getattr(stormlib,"_Z14SFileGetLocalev")
			self.SFileSetLocale = getattr(stormlib,"_Z14SFileSetLocalej")
			self.SFileOpenFileEx = getattr(stormlib,"_Z15SFileOpenFileExPvPKcjPS_")
			self.SFileRemoveFile = getattr(stormlib,"_Z15SFileRemoveFilePvPKcj")
			self.SFileRenameFile = getattr(stormlib,"_Z15SFileRenameFilePvPKcS1_")
			self.SFileVerifyFile = getattr(stormlib,"_Z15SFileVerifyFilePvPKcj")
			self.SFileAddListFile = getattr(stormlib,"_Z16SFileAddListFilePvPKc")
			self.SFileEnumLocales = getattr(stormlib,"_Z16SFileEnumLocalesPvPKcPjS2_j")
			self.SFileExtractFile = getattr(stormlib,"_Z16SFileExtractFilePvPKcS1_")
			self.SFileGetFileInfo = getattr(stormlib,"_Z16SFileGetFileInfoPvjS_jPj")
			self.SFileGetFileName = getattr(stormlib,"_Z16SFileGetFileNamePvPc")
			self.SFileGetFileSize = getattr(stormlib,"_Z16SFileGetFileSizePvPj")
			self.SFileOpenArchive = getattr(stormlib,"_Z16SFileOpenArchivePKcjjPPv")
			self.SFileAddFile_Init = getattr(stormlib,"_Z17SFileAddFile_InitP11TMPQArchivePKcP12TMPQFileTimejjjPPv")
			self.SFileCloseArchive = getattr(stormlib,"_Z17SFileCloseArchivePv")
			self.SFileFindNextFile = getattr(stormlib,"_Z17SFileFindNextFilePvP16_SFILE_FIND_DATA")
			self.SFileFlushArchive = getattr(stormlib,"_Z17SFileFlushArchivePv")
			self.SFileAddFile_Write = getattr(stormlib,"_Z18SFileAddFile_WritePvS_jj")
			self.SFileFindFirstFile = getattr(stormlib,"_Z18SFileFindFirstFilePvPKcP16_SFILE_FIND_DATAS1_")
			self.SFileGetAttributes = getattr(stormlib,"_Z18SFileGetAttributesPv")
			self.SFileOpenArchiveEx = getattr(stormlib,"_Z18SFileOpenArchiveExPKcjjPPv")
			self.SFileSetAttributes = getattr(stormlib,"_Z18SFileSetAttributesPvj")
			self.SFileSetFileLocale = getattr(stormlib,"_Z18SFileSetFileLocalePvj")
			self.SFileVerifyArchive = getattr(stormlib,"_Z18SFileVerifyArchivePv")
			self.SFileAddFile_Finish = getattr(stormlib,"_Z19SFileAddFile_FinishPvi")
			self.SFileCompactArchive = getattr(stormlib,"_Z19SFileCompactArchivePvPKca")
			self.SFileSetFilePointer = getattr(stormlib,"_Z19SFileSetFilePointerPviPij")
			self.SFileCreateArchiveEx = getattr(stormlib,"_Z20SFileCreateArchiveExPKcjjPPv")
			self.SFileCreateAttributes = getattr(stormlib,"_Z21SFileCreateAttributesPvj")
			self.SFileSetHashTableSize = getattr(stormlib,"_Z21SFileSetHashTableSizePvj")
			self.SFileSetAddFileCallback = getattr(stormlib,"_Z23SFileSetAddFileCallbackPvPFvS_jjaES_")
			self.SFileSetCompactCallback = getattr(stormlib,"_Z23SFileSetCompactCallbackPvPFvS_jP14_LARGE_INTEGERS1_ES_")
			self.SFileSetDataCompression = getattr(stormlib,"_Z23SFileSetDataCompressionj")
			self.SFileUpdateFileAttributes = getattr(stormlib,"_Z25SFileUpdateFileAttributesPvPKc")
		elif os.name == "nt":
			stormlib = windll.LoadLibrary("StormLib/StormLib.dll")
			
			
			self.SFileOpenArchive = getattr(stormlib,"SFileOpenArchive")
			self.SFileCreateArchive = getattr(stormlib,"SFileCreateArchive")
			self.SFileCreateArchiveEx = getattr(stormlib,"SFileCreateArchiveEx")			
			
			self.SFileSetLocale = getattr(stormlib,"SFileSetLocale")
			self.SFileGetLocale = getattr(stormlib,"SFileGetLocale")
			self.SFileFlushArchive = getattr(stormlib,"SFileFlushArchive")
			self.SFileCloseArchive = getattr(stormlib,"SFileCloseArchive")			
			
			self.SFileAddListFile = getattr(stormlib,"SFileAddListFile")
			
			self.SFileSetCompactCallback = getattr(stormlib,"SFileSetCompactCallback")	
			self.SFileCompactArchive = getattr(stormlib,"SFileCompactArchive")
			
			self.SFileSetHashTableSize = getattr(stormlib,"SFileSetHashTableSize")			
			
			self.SFileCreateAttributes = getattr(stormlib,"SFileCreateAttributes")
			self.SFileGetAttributes = getattr(stormlib,"SFileGetAttributes")
			self.SFileSetAttributes = getattr(stormlib,"SFileSetAttributes")
			self.SFileUpdateFileAttributes = getattr(stormlib,"SFileUpdateFileAttributes")			
			
			self.SFileOpenFileEx = getattr(stormlib,"SFileOpenFileEx")
			self.SFileGetFileSize = getattr(stormlib,"SFileGetFileSize")
			self.SFileSetFilePointer = getattr(stormlib,"SFileSetFilePointer")
			self.SFileReadFile = getattr(stormlib,"SFileReadFile")
			self.SFileCloseFile = getattr(stormlib,"SFileCloseFile")			
			
			self.SFileHasFile = getattr(stormlib,"SFileHasFile")
			self.SFileGetFileName = getattr(stormlib,"SFileGetFileName")
			self.SFileGetFileInfo = getattr(stormlib,"SFileGetFileInfo")
			
			self.SFileExtractFile = getattr(stormlib,"SFileExtractFile")
			
			self.SFileVerifyFile = getattr(stormlib,"SFileVerifyFile")
			
			self.SFileVerifyArchive = getattr(stormlib,"SFileVerifyArchive")
			
			self.SFileFindFirstFile = getattr(stormlib,"SFileFindFirstFile")
			self.SFileFindNextFile = getattr(stormlib,"SFileFindNextFile")
			self.SFileFindClose = getattr(stormlib,"SListFileFindClose")
			
			self.SFileEnumLocales = getattr(stormlib,"SFileEnumLocales")
			
			self.SFileCreateFile = getattr(stormlib,"SFileCreateFile")
			self.SFileWriteFile = getattr(stormlib,"SFileWriteFile")
			self.SFileFinishFile = getattr(stormlib, "SFileFinishFile")
			self.SFileAddFileEx = getattr(stormlib,"SFileAddFileEx")
			self.SFileAddFile = getattr(stormlib,"SFileAddFile")
			self.SFileAddWave = getattr(stormlib,"SFileAddWave")
			self.SFileRemoveFile = getattr(stormlib,"SFileRemoveFile")
			self.SFileRenameFile = getattr(stormlib,"SFileRenameFile")
			self.SFileSetFileLocale = getattr(stormlib,"SFileSetFileLocale")
			self.SFileSetDataCompression = getattr(stormlib,"SFileSetDataCompression")
			self.SFileSetAddFileCallback = getattr(stormlib,"SFileSetAddFileCallback")
						

		else:
			print os.name + " not yet supported :/"
	


storm = StormLib()


class MPQ:
	def __init__(self):
		self.hmpq = c_void_p()
		self.hfile = c_void_p()
		
	def createArchive(self,filename):
		return storm.SFileCreateArchive(filename, 0x00010100, 0x8000, byref(self.hmpq))
		
	def openArchive(self, filename):
		return storm.SFileOpenArchive(filename, 0, 0, byref(self.hmpq))
		
	def closeArchive(self):
		storm.SFileCloseArchive(self.hmpq)
		
	def createFile(self, name, filesize):
		storm.SFileCreateFile(self.hmpq, name, None, filesize, 	0, 0x00000200, byref(self.hfile))
		
	def writeFile(self, f):
		storm.SFileWriteFile(self.hfile, byref(f), len(f), 0x01)
		
	def openFile(self, filename):
		storm.SFileOpenFileEx(self.hfile, filename, 0, byref(self.hfile))
		return self.hfile
		
	def addFile(self, filename, name_in_archive, always_add = True):
		if ((storm.SFileAddFileEx(self.hmpq, filename, name_in_archive, 0x00000100, 0, 0) == 0) & always_add):
			storm.SFileRemoveFile(self.hmpq, name_in_archive, 000000)
			return storm.SFileAddFileEx(self.hmpq, filename, name_in_archive, 0x00000100, 0, 0)
		else:
			return 0
	
	def getLocalPaths(self, path):	
		ret = []
		for i in os.listdir(path):
			if (os.path.isfile(path+"\\"+i)):
				ret.append(path+"\\"+i)
			elif(os.path.isdir(path+"\\"+i)):
				ret.extend(self.getLocalPaths(path+"\\"+i))
		return ret
			
	def addDirectory(self, path):
		if (path[-1] == "\\"):
			for i in self.getLocalPaths(path[:-1]):
				print i
				self.addFile(i, i[len(path)::])
		else:
			for i in self.getLocalPaths(path):
				print i
				self.addFile(i, i[len(path)+1::])
			
		
		
		
s = MPQ()
if(s.createArchive("D:\\Programmierung\\Python\\PyM2\\mpq\\patch-z.MPQ") == 0):
	s.openArchive("D:\\Programmierung\\Python\\PyM2\\mpq\\patch-z.MPQ")
print s.addDirectory("D:\\makempq\\")
s.closeArchive()

