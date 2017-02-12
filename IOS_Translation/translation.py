#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-23 16:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

'''
Step1: Run he translator.exe to conver the like BUSMB_SBO_Sales_Android_Main_10_AR.xml to ar.lproj/Localizable.strings
Step2: Convert ar.lproj/Localizable.strings to values-ar/string.xml
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import codecs

print os.getcwd()
count = 0
for dir in os.listdir(os.getcwd()):
	if os.path.isdir(dir):
		print dir
		count = count + 1

print 'Total dirs count: ', count

'''
Define files relationships in cleanIOS(): 28 relationships from original lproj to target lporj after cleaing: 
	1. en.lporj: Actually there are 29 lporj files in real translation folder, but en.lproj is the original file, so here we don't need to deal with it.
	2. es_419.lporj: add es_419.lporj from es_CO.lproj
'''
relations={
	'ar.lproj': 'ar.lproj',
	'cs.lproj': 'cs.lproj',
	'da.lproj': 'da.lproj',
	'de.lproj': 'de.lproj',
	'el.lproj': 'el.lproj',
	'en-GB.lproj': 'en-GB.lproj',
	'es_419.lproj': 'es_CO.lproj',
	'es_CO.lproj': 'es_CO.lproj',
	'es.lproj': 'es.lproj',
	'fi.lproj': 'fi.lproj',
	'fr.lproj': 'fr.lproj',
	'he.lproj': 'he.lproj',
	'hu.lproj': 'hu.lproj',
	'it.lproj': 'it.lproj',
	'ja.lproj': 'ja.lproj',
	'ko.lproj': 'ko.lproj',
	'nl.lproj': 'nl.lproj',
	'no.lproj': 'no.lproj',
	'pl.lproj': 'pl.lproj',
	'pt_BR.lproj': 'pt_BR.lproj',
	'pt.lproj': 'pt.lproj',
	'ru.lproj': 'ru.lproj',
	'sk.lproj': 'sk.lproj',
	'sv.lproj': 'sv.lproj',
	'tr.lproj': 'tr.lproj',
	'zh_CN.lproj': 'zh_CN.lproj',
	'zh_TW.lproj': 'zh_TW.lproj',
	'zh.lproj': 'zh_CN.lproj',
}


def getKeysAndValues(path):
	# Jugle the input file path is valid
	if path is None:
		print 'file path is None'
		return 

	# Read the file with coding
	file = codecs.open(path, 'r', 'utf-8')
	string = file.read()
	file.close()

	# Get the key-value dividing by ";
	localStringList = string.strip().split('\";')
	localStringList = localStringList[0:-1]

	# Extract the key and value
	keys = []
	values = []
	for x in range(len(localStringList)):
		keyValue = localStringList[x].strip().split('=')
		if len(keyValue)==2:
			key = keyValue[0].strip().split('\"')[1]
			value = keyValue[1].strip().replace('"', '')
			keys.append(key.strip())
			values.append(value.strip())
		else:
			# Log.error("Result split by '=' is: %@", len(keyValue))
			print "Result split by '=' is: ", len(keyValue)
			print keyValue

	return (keys, values)

def writeToCleanFile(keys, values, directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	print "Creating android file:" + directory + "/string.xml"

	fo = open(directory + '/Localizable.strings', 'wb')

	for x in range(len(keys)):
		if values[x] is None or values[x] == '':
			print "Key:" + keys[x] + "\'s value is None. Index:" + str(x + 1)
			continue

		key = keys[x]
		value = values[x]
		content = "\"" + key + "\"=\"" + value + "\";\n"
		fo.write(content)

	fo.close()

def cleanIOS(localizableStringsInputPath, cleanIOSFileOutputPath):
	if not os.path.exists(cleanIOSFileOutputPath):
		os.makedirs(cleanIOSFileOutputPath)

	if localizableStringsInputPath is not None:
		print "Read Localizable.strings file from ", localizableStringsInputPath
		(keys, values) = getKeysAndValues(localizableStringsInputPath)
		print "Read Localizable.strings finish"

		if cleanIOSFileOutputPath is not None:
			writeToCleanFile(keys,values,cleanIOSFileOutputPath)
			print "Convert successfully! you can see clean ios translation in ", cleanIOSFileOutputPath

        else:
            print "Target file path can not be empty! try -h for help."

# Convert teh 
def convertXML2IOS():
	from subprocess import Popen
	Popen("Main_trans.bat")
						
for k, v in relations.items():
	# print v
	# convertXML2IOS()
	cleanIOS(v + '/Localizable.strings', '0_convert_result/' + k)
















