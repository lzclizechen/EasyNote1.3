#!/usr/bin/python3

import platform
import re
import os.path
import getopt, sys

		
__ver__ = "1.3"
os_type = platform.system()
py_ver  = sys.version[0]

if ( py_ver == "3") :
	import tkinter as tk
else:
	import Tkinter as tk





class Inventory():
	pass

class MotionDairy():
	pass

class TodoTask():
	pass

class App():

	def __init__(self, master):

		frame = tk.Frame(master) # 添加一个Frame框架
		frame.pack(side=tk.LEFT, padx=10, pady=10) # 自动调整

		self.hi_there = tk.Button(frame, text="Welcome！", bg="black", fg="white", command=self.say_hi) # 添加按钮组件
		self.hi_there.pack() # 

	def say_hi(self):	
		print("Welcome to use EasyNote1.3！\n")

class CtrlPenal():
	def __init__():
		pass
	def startMode(self, mode=""):
		pass
	def config(self, mode=""):
		pass
	def window():
		pass
	def checkArgs():
		opts, args = getopt.getopt(sys.argvs[1:], "ghvc", ["gui", "help", "cmd", "version"])
		for o, a in opts:
			if o in ("-h", "--help"):
				self.usage()
			elif o in ("-v", "--version"):	
				print(__ver__)
			elif o in ("-g", "--gui"):
				pass
			elif o in ("-c", "--cmd"):
				pass
			else:
				if(os_type == "Windows"):
					pass
				else:
					pass
	def usage():
		info = """
			-h, --help     print this message
			-v, --version  print version information
			-g, --gui      start with window mode if linux
			-c, --cmd      start with cmd mode if windows
		""";
		print(info)


if __name__ == "__main__":
	if ( os_type == "Linux"):
		pass
	elif (os_type == "Windows" ):
		pass
	root = tk.Tk()   # 实例化顶层 
	app = App(root)  # root作为参数， 一般是这么写

	root.mainloop()  # 主循环	




