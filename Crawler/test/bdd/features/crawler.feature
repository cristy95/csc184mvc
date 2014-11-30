Feature: Web crawler application to download 
		images from a website

		As a user I wish to be able to download images from a certain website

Scenario: Download images from a website
		Given the crawler is started
		And the homepage is verified
		When it finishes the download
		Then I should see the following images on its folder:
		|file_name			|
		|tpcmast.jpg		|