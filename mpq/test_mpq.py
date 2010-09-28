#! /usr/bin/python

import ctypes
import os

#temp, delete later
GENERIC_WRITE =  0x40000000
CREATE_ALWAYS = 2

class StormLib:
	def __init__(self):
		if os.name == "posix":
			stormlib = ctypes.cdll.LoadLibrary("StormLib/libStorm.so")

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
			stormlib = ctypes.cdll.LoadLibrary("StormLib/StormLib.dll")
			
			
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
	



s = StormLib()