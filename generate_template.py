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
NUM_REQUIRE_ARGUMENT = 1

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
		CplusplusClass = 'cpp-class'
		CplusplusHeader = 'cpp-header'

	#	Mapping dict of generator type to template
	GeneratorTypeToTemplateFile = {
		TemplateGeneratorType.PythonClass : TemplateFileConfigureDict.PythonClassTemplatePath,
		TemplateGeneratorType.PythonMain : TemplateFileConfigureDict.PythonMainTemplatePath,
		TemplateGeneratorType.CplusplusClass : TemplateFileConfigureDict.CplusplusClassTemplatePath,
		TemplateGeneratorType.CplusplusHeader : TemplateFileConfigureDict.CplusplusHeaderTemplatePath
	}

	def __init__( self, generatorType ):
		'''	Initial, set generator type when constuct this object
		'''

		#	Set generator
		self.generatorType = generatorType

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

	def constructOptionsDict( self, fileName, options ):
		'''	Construct dict from options object
		'''	

		#	Get only file name of path
		baseFileName = os.path.split( fileName )[ 1 ]
		beseFileNameNoExt = os.path.splitext( baseFileName )[ 0 ]

		#	Add file to object
		defaultDict = self.parameterObject.getAttributeDict()

		for key in defaultDict:
			val = getattr( options, key )
			self.parameterObject.setValueToAttribute( key, val )
		
		self.parameterObject.addAttributeValue( TemplateFileConfigureDict.FileNameFieldName, beseFileNameNoExt )

	def run( self, fileName ):
		'''	Run!!!
		'''
		
		#	Get default attribute in dict and update default file name
		dataDict = self.parameterObject.getAttributeDict()
		TemplateGenerator.generateTemplateFile( fileName, self.templatePath, dataDict )

	

########################################################
#
#	Function bodies
#

########################################################
#
#	main
#	
def main():

	generatorType = 'python-main'

	mainGenerator = MainGenerator( generatorType )
	
	#	initial parser instance
	parser = optparse.OptionParser()

	#	Set options
	mainGenerator.setOptionToOptParser( parser )

	( options, args ) = parser.parse_args()

	#	check number of argument from NUM_REQUIRE_ARGUMENT
	if len( args ) != 1:	
		
		#	raise error from parser
		parser.error( "require {} argument(s)".format( NUM_REQUIRE_ARGUMENT ) )
		sys.exit( -1 )

	fileName = args[0]

	mainGenerator.constructOptionsDict( fileName, options )

	mainGenerator.run( fileName )

########################################################
#
#	call main
#

if __name__=='__main__':
	main()

