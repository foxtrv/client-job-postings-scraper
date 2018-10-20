from BasicCrawl import BasicCrawl
from PrintHelper import PrintHelper

# Zume = BasicCrawl('Zume', 'https://zumepizza.com/careers', 'job-item')
# print(Zume.text)
#
# BuildingConnected = BasicCrawl('Building Connected', 'https://www.buildingconnected.com/jobs/', 'css-12xrnu5')
# print(BuildingConnected.text)

VideoAmp = BasicCrawl('VideoAmp', 'https://jobs.lever.co/videoamp.com', 'posting')
print(PrintHelper(VideoAmp.text).removeAPPLY().removeFULLTIME().text)

