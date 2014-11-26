import httplib2
import os
import re
import threading
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup

class Singleton(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance