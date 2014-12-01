Feature: Web crawler application to download 
		images from a website

		As a user I wish to be able to download images from a certain website

Scenario: Downloading images when crawler is not started
		Given the crawler is not started
		Then I should not see the following images on the folder:
		|file_name			|
		|tpcmast.jpg		|

Scenario: Download images from a website
		Given the crawler is started
		And the link is verified
		When it finishes the download
		Then I should see the following images on its folder:
		|file_name			|
		|tpcmast.jpg		|


