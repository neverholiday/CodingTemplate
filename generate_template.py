#!/usr/bin/env python3
#
# Copyright (C) 2020
#			Written by Nasrun (Nas) Hayeeyama
#

VERSIONNUMBER = 'v1.0'
PROGRAM_DESCRIPTION = "Script for generate template file"

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

from TemplateFileConfigureDict import TemplateFileConfigureDict
from TemplateGenerator import TemplateGenerator

########################################################
#
#	Standard globals
#
NUM_REQUIRE_ARGUMENT = 2

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

class MainGenerator( object ):
	''' Main object to generate template
	'''

	class TemplateGeneratorType:
		PythonClass = 'python-class'
		PythonMain = 'python-main'

	#	Mapping dict of generator type to template
	GeneratorTypeToTemplateFile = {
		TemplateGeneratorType.PythonClass : TemplateFileConfigureDict.PythonClassTemplatePath,
		TemplateGeneratorType.PythonMain : TemplateFileConfigureDict.PythonMainTemplatePath
	}

	def __init__( self, generatorType, fileName ):
		'''	Initial, set generator type when constuct this object
		'''

		#	Set generator
		self.generatorType = generatorType

		#	Set fileName
		self.fileName = fileName

		#	Get template path
		self.templatePath = MainGenerator.GeneratorTypeToTemplateFile[ generatorType ]

		#	Get default attribute and value dict
		self.parameterObject = TemplateFileConfigureDict.TemplateFileToParameterObjectDict[ self.templatePath ]

	def setOptionToOptParser( self, parser ):
		'''	Loop to set attribute value to opt parser
		'''

		defaultDict = self.parameterObject.getAttributeDict()

		for attrName, val in defaultDict.items():

			parser.add_option( "--{}".format( attrName ),
                  action="store", type="string", dest=attrName, default=val,
				  help='Default of {} is {!r}'.format( attrName, val ) )

	def constructOptionsDict( self, options ):
		'''	Construct dict from options object
		'''	

		defaultDict = self.parameterObject.getAttributeDict()

		for key in defaultDict:
			val = getattr( options, key )
			self.parameterObject.setValueToAttribute( key, val )

	def run( self ):
		'''	Run!!!
		'''
		dataDict = self.parameterObject.getAttributeDict()
		print( dataDict )
		TemplateGenerator.generateTemplateFile( self.fileName, self.templatePath, dataDict )

	

########################################################
#
#	Function bodies
#

########################################################
#
#	main
#	
def main():

	#	Get raw argument from sys
	args = list( sys.argv[ 1 : ] )

	if len( args ) < 2:
		print( 'Usage ./generate_template.py <generatorType> <fileName>' )
		return

	#	Get argument 
	generatorType = args[ 0 ]
	fileName = args[ 1 ]

	mainGenerator = MainGenerator( generatorType, fileName )
	
	#	initial parser instance
	parser = optparse.OptionParser()

	#	Set options
	mainGenerator.setOptionToOptParser( parser )

	( options, args ) = parser.parse_args()

	mainGenerator.constructOptionsDict( options )

	mainGenerator.run()

########################################################
#
#	call main
#

if __name__=='__main__':
	main()

