#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-23 16:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

'''
Step1: Run he translator.exe to conver the BUSMB_SBO_Sales_Android_Main_10_0S.xml to ar.lproj/Localizable.strings
Step2: Convert ar.lproj/Localizable.strings to values-ar/string.xml
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from Log import Log
import codecs

# print os.getcwd()
# count = 0
# for dir in os.listdir(os.getcwd()):
# 	if os.path.isdir(dir):
# 		print dir
# 		count = count + 1

# print 'Total dirs count: ', count

relations={
	'values-ar': 'ar.lproj',
	'values-cs': 'cs.lproj',
	'values-da': 'da.lproj',
	'values-de': 'de.lproj',
	'values-el': 'el.lproj',
	'values-en-rUK': 'en-GB.lproj',
	'values-es': 'es.lproj',
	'values-es-rCO': 'es_CO.lproj',
	'values-fi': 'fi.lproj',
	'values-fr': 'fr.lproj',
	'values-he': 'he.lproj',
	'values-hu': 'hu.lproj',
	'values-it': 'it.lproj',
	'values-iw': 'he.lproj',
	'values-ja': 'ja.lproj',
	'values-ko': 'ko.lproj',
	'values-nl': 'nl.lproj',
	'values-no': 'no.lproj',
	'values-pl': 'pl.lproj',
	'values-pt': 'pt.lproj',
	'values-pt-rBR': 'pt_BR.lproj',
	'values-ru': 'ru.lproj',
	'values-sk': 'sk.lproj',
	'values-sv': 'sv.lproj',
	'values-tr': 'tr.lproj',
	'values-zh-rCN': 'zh_CN.lproj',
	'values-zh-rTW': 'zh_TW.lproj',
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

def writeToXmlFile(keys, values, directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	print "Creating android file:" + directory + "/string.xml"

	fo = open(directory + '/string.xml', 'wb')

	stringEncoding = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
	fo.write(stringEncoding)

	for x in range(len(keys)):
		if values[x] is None or values[x] == '':
			print "Key:" + keys[x] + "\'s value is None. Index:" + str(x + 1)
			continue

		key = keys[x]
		value = values[x]
		content = "   <string name=\"" + key + "\">" + value + "</string>\n"
		fo.write(content)

	fo.write("</resources>");
	fo.close()

def convertIOS2Android(localizableStringsInputPath, stringXmlFileOutputPath):
	if not os.path.exists(stringXmlFileOutputPath):
		os.makedirs(stringXmlFileOutputPath)

	if localizableStringsInputPath is not None:
		print "Read Localizable.strings file from ", localizableStringsInputPath
		(keys, values) = getKeysAndValues(localizableStringsInputPath)
		print "Read Localizable.strings finish"

		if stringXmlFileOutputPath is not None:
			writeToXmlFile(keys,values,stringXmlFileOutputPath)
			print "Convert successfully! you can see strings.xml in ", stringXmlFileOutputPath

        else:
            print "Target file path can not be empty! try -h for help."

def convertXML2IOS():
	from subprocess import Popen
	Popen("Main_trans.bat")
			
for k, v in relations.items():
	convertXML2IOS()
	convertIOS2Android(v + '/Localizable.strings', '0_convert_result/' + k)
















