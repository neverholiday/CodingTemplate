#!/usr/bin/env python{PYTHONVERSION}
#
# Copyright (C) {YEAR}
#			Written by {DEVELOPER}
#

VERSIONNUMBER = 'v1.0'
PROGRAM_DESCRIPTION = "{DESCRIPTION}"

########################################################
#
#	STANDARD IMPORTS
#

import sys
import os

import optparse

########################################################
#
#	LOCAL IMPORTS
#


########################################################
#
#	Standard globals
#
NUM_REQUIRE_ARGUMENT = {NUM_REQ_ARGUMENT}

########################################################
#
#	Program specific globals
#

########################################################
#
#	Helper functions
#

########################################################
#
#	Class definitions
#

########################################################
#
#	Function bodies
#

########################################################
#
#	main
#	
def main():
	
	#	define usage of programing
	programUsage = "%prog [option] <args> " + str( VERSIONNUMBER ) + ', Copyright (C) {YEAR}'

	#	initial parser instance
	parser = optparse.OptionParser( usage = programUsage, description=PROGRAM_DESCRIPTION )

	#	add option of main script
	parser.add_option( "-o", "--myOption", dest = "myOption",
						help = "Specify option document here." )

	#	add option
	( options, args ) = parser.parse_args()

	#	check number of argument from NUM_REQUIRE_ARGUMENT
	if len( args ) != NUM_REQUIRE_ARGUMENT:	
		
		#	raise error from parser
		parser.error( "require {{}} argument(s)".format( NUM_REQUIRE_ARGUMENT ) )
		sys.exit( -1 )

	#########################################################
	#
	#		get option and argument
	#
	argList = list( args )
	myOption = options.myOption
	

########################################################
#
#	call main
#

if __name__=='__main__':
	main()

