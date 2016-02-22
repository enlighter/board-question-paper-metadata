''' [In Ubuntu based systems make sure you have python-dev packages installed in your system,
	such as python-dev, python-all-dev, python3-dev et al]
	sudo [-E] pip install lxml
	sudo [-E] pip install pprintpp
	In case of python2 as system default, use pip3 instead

	__author__: "Sushovan Mandal"
	__email__: "mandal.sushovan92@gmail.com"

	use python >= 3.4
'''
#!/usr/bin/python3

import sys
import os
#import posixpath
import traceback
from io import StringIO
#from pprintpp import pprint  # pretty-print
from lxml.etree import tostring
from lxml.builder import E
#from extractFromEpub import metadata_extraction as epub_extraction
from utils.datahandler import xml_dump, empty_contents, logger

class metadata:
	'''metadata standard = NDL 2.0'''
	def __init__(self):
		print("creating new metadata instance")
		self._xml_wrapper_head = 'E.dublin_core('
		self._xml_wrapper_tail = ' schema="dc")'
		self._xml_element_head = 'E.dcvalue('
		self._xml_element_tail = ' )' #language="en")'
		self._xml_body = ''
		self.xml = ''

	def _xml_bind_(self, body=''):
		ret = self._xml_wrapper_head
		if body:
			ret += body
		ret += self._xml_wrapper_tail
		#DEBUG
		print("whole xml structure:")
		print(ret)
		return ret

	def _append_element_(self, args=''):
		if self._xml_body:
			self._xml_body += ','
		self._xml_body += self._xml_element_head + args + self._xml_element_tail + ','
		#DEBUG
		print(self._xml_body)

	def _create_xml_(self):
		self.xml = eval(self._xml_bind_(self._xml_body))
		# use decode explicitly in python 3 as tostring returns a byte type object
		# which needs to be decoded to string (preferably immediately) so the program
		# internally works only on strings
		return tostring( self.xml, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode()


def get_files(directory_path):
	old_stdout = sys.stdout
	sys.stdout = my_stdout = StringIO()

	try:
		files_list = []
		for root, dirnames, filenames in os.walk(directory_path):
			for filename in filenames:
				files_list.append(os.path.join(root, filename))
		#print(files_list)

	except:
			e = sys.exc_info()
			trace = traceback.format_exc()
			print( trace + '\ngracefully exiting...', file=sys.stdout)
			print( str(e) + '\ngracefully exiting...', file=sys.stderr)

	log = my_stdout.getvalue()
	sys.stdout = old_stdout
	try:
		# write log file
		writelog = logger(log)
		writelog.dump()
	except:
		e = sys.exc_info()
		print( str(e) + "\nCouldn't log", file=sys.stdout)
		print( str(e) + "\nCouldn't log", file=sys.stderr)

# create_sip('extras/sample0.epub')
# create_sip('extras/sample1.epub')
# get_files('extras')

#path = input('Which folder is your files in? ')
#get_files(path)

xml = metadata()
xml._append_element_('test="ab"')
print( xml._create_xml_() )