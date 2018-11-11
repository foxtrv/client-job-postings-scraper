from BasicCrawl import BasicCrawl
from PrintHelper import PrintHelper

# Zume = BasicCrawl('Zume', 'https://zumepizza.com/careers', 'job-item').performCrawl()
# print(Zume.text)
#
# BuildingConnected = BasicCrawl('Building Connected', 'https://www.buildingconnected.com/jobs/', 'css-12xrnu5').performCrawl()
# print(BuildingConnected.text)

# VideoAmp = BasicCrawl('VideoAmp', 'https://jobs.lever.co/videoamp.com', 'posting').performCrawl()
# print(PrintHelper(VideoAmp.text).removeAPPLY().removeFULLTIME().text)

# Procore = BasicCrawl('Procore', 'https://www.procore.com/jobs/openings', 'c-filter-items').performCrawl()
# print(PrintHelper(Procore.text).removeAPPLY().text)

# Honor = BasicCrawl('Honor', 'https://www.joinhonor.com/careers', 'src-components-CareersPage----OpenPositions-module---positionLink---1js-q').performCrawl()
# print(PrintHelper(Honor.text).removeAPPLY().text)

# Counsyl = BasicCrawl('Counsyl', 'https://www.counsyl.com/about-counsyl/careers/#open-positions', 'careers__item').performCrawl()
# print(PrintHelper(Counsyl.text).removeAPPLY().text)

# Asana = BasicCrawl('Asana', 'https://asana.com/jobs/all', 'jobs-listing').performCrawl()
# print(PrintHelper(Asana.text).removeAPPLY().text)

Cloudian = BasicCrawl('Cloudian', 'https://cloudian.com/company/careers/', 'jv-job-list-name').performExtraStepsCrawl('jv-job-list', 'jv-job-list-name', 'jv-job-list-location')
print(PrintHelper(Cloudian.text).removeAPPLY().text)




# should prob set filter for class-name or <tag> or something else.. for these wacky js-generated classnames...

# output text to file for each website, and perform a "diff" call on the text files (or just some code or something...), if new file diff from other one, create add text to file of different roles.