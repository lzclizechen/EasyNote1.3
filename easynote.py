#!/usr/bin/python3

import platform
import getopt, sys

def check_args():
	opts, args = getopt.getopt(sys.argvs[1:], "ghv", ["gui", "help", "version"])




if __name__ == "__main__":
	os_type = platform.system()
	if ( os_type == "Linux"):
		pass
	elif (os_type == "Windows" ):
		pass




