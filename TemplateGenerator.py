#!/usr/bin/env python3
#
# Copyright (C) 2020
#			Written by Nasrun (Nas) Hayeeyama
#

########################################################
#
#	STANDARD IMPORTS
#

########################################################
#
#	LOCAL IMPORTS
#

########################################################
#
#	GLOBALS
#

########################################################
#
#	EXCEPTION DEFINITIONS
#

class UnableGenerateTemplateFileException( Exception ):
	pass

########################################################
#
#	HELPER FUNCTIONS
#

def readFile( filePath ):
	'''	Read file path and return content of a file
		INPUT : filePath (str) path of file to read
		RETURN : content (str) content of a file from f.read() function
		RAISE : FileNotFoundError if file is not exist
	'''

	content = ''

	#	Read file with 'with' statement
	#	File will close if out of with context
	with open( filePath, 'r' ) as f:
		content = f.read()

	return content

def writeFile( filePath, content ):
	'''	Write file path
		INPUT : filePath (str) path of file to writes
	'''

	#	Open file with 'with' statement
	with open( filePath, 'w' ) as f:
		f.write( content )

########################################################
#
#	CLASS DEFINITIONS
#

class TemplateGenerator( object ):
	''' TemplateGenerator to generate template file
	'''
	
	@staticmethod
	def generateTemplateFile( fileName, templateFileName, attributeToValueDict ):
		'''	Function to generate templete file from file path
			INPUT:	templateFileName (str) name of template file name
					attributeToValueDict (dict) dictionary of attribute to update formatter variable in template
		'''

		#	Read template file
		try:
			templateContent = readFile( templateFileName )
		except FileNotFoundError as e:
			print( 'Unable to read file, file {} is not found'.format( templateFile ) )
			return

		print( attributeToValueDict )

		#	Substution value from attribute to value dict
		try:
			generateTxt = templateContent.format( **attributeToValueDict )
		except KeyError as e:
			print( 'Unable to substitution value from dict, {}'.format( e ) )
			return

		#	Write file
		writeFile( fileName, generateTxt )


