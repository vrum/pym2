from py2exe.build_exe import py2exe 
from distutils.core import setup


setup(windows=[{"script":"startme.py"}], 
	options={
		"py2exe":
			{
			"includes":
				["sip","ctypes","logging"],
			"excludes":
				["OpenGL"],
			}
	}
)

