#!/usr/bin/env python3
#
# Copyright (C) 2020
#			Written by Nasrun (Nas) Hayeeyama
#

########################################################
#
#	STANDARD IMPORTS
#

from datetime import datetime

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

########################################################
#
#	HELPER FUNCTIONS
#


def getCurrentYearStringFormat():
	'''	Function to get current year with string format

		@rtype string : current year with string format 
	'''
	currentDateTime = datetime.now()
	year = currentDateTime.year
	return str( year )

def getCurrentMonthStringFormat():
	'''	Function to get current month with string format
	
		@rtype string : current month with string format
	'''
	currentDateTime = datetime.now()
	month = currentDateTime.month
	return str( month )

########################################################
#
#	CLASS DEFINITIONS
#

class ParameterObject( object ):
	''' Class to contain attribute from construct keyword argument
	'''

	def __init__( self, **kwargs ):
		'''	This class get keyword argument when construct object to store as attribute
			Reference : https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python
		'''
		self.__dict__.update( kwargs )

	def getAttributeDict( self ):
		'''	Get dict from set attribute
			RETURN attributeDict (dict) dictionary of attribute
		'''
		return dict( self.__dict__ )

	def setValueToAttribute( self, attrName, value ):
		'''	Set value to specified attribute
			INPUT : attrName (str) name of attribute, must same attribute when constrct object
					value (str) value of attribute
			RAISE : KeyError if set another attribute
					AssertionError if attrname and value are not string type
		'''

		assert type( attrName ) == str and type( value ) == str, 'attrName and value must be string type'

		if attrName not in self.__dict__:
			raise KeyError

		#	Update value
		self.__dict__[ attrName ] = value

	def addAttributeValue( self, attrName, value ):

		assert attrName not in self.__dict__, 'attrName {} already in __dict__'.format( attrName ) 
		self.__dict__[ attrName ] = value

class TemplateFileConfigureDict( object ):
	''' Object to store dictionary of file template to variable dict
	'''

	PythonClassTemplatePath = 'template/class.py'
	PythonMainTemplatePath = 'template/main.py'
	CplusplusClassTemplatePath = 'template/classdef.c++'
	CplusplusHeaderTemplatePath = 'template/classheader.h'

	FileNameFieldName = 'FILENAME'
	
	TemplateFileToParameterObjectDict = {

		#	Python class template python		
		PythonClassTemplatePath : ParameterObject( PYTHONVERSION='', \
													YEAR=getCurrentYearStringFormat(), \
													DEVELOPER='Nasrun (Nas) Hayeeyama',
													PARENTCLASSNAME='object' ),

		#	Python main template python									
		PythonMainTemplatePath : ParameterObject( PYTHONVERSION='', \
													YEAR=getCurrentYearStringFormat(), \
													DEVELOPER='Nasrun (Nas) Hayeeyama', \
													NUM_REQ_ARGUMENT='0', \
													DESCRIPTION='', \
													USAGE='' ),
		
		#	c++ class template python									
		CplusplusClassTemplatePath : ParameterObject( YEAR=getCurrentYearStringFormat(), \
													DEVELOPER='Nasrun (Nas) Hayeeyama' ),

		#	c++ header template python									
		CplusplusHeaderTemplatePath : ParameterObject( YEAR=getCurrentYearStringFormat(), \
													DEVELOPER='Nasrun (Nas) Hayeeyama' )

	}

	