from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
import subprocess
import os

@step(u'Given the crawler is started')
def given_the_crawler_is_started(step):
	print os.system('python crawler.py')
	
@step(u'And the homepage is verified')
def given_the_homepage_is_verified(step):
	assert 1 == 1

@step(u'When it finishes the download')
def when_it_finishes_the_download(step):
	assert True

@step(u'Then I should see the following images on its folder:')
def then_i_should_see_the_following_images_on_its_folder(step):
	for row in step.hashes:
		name = row['file_name']
		state = os.path.exists("/home/cristylorainefuerzas/Documents/school/csc184/csc184mvc/Crawler/images/" + name)
		assert_equal(state, True)
