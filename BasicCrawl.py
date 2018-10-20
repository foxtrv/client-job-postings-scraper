# couldn't use BeautifulSoup library because webpage is rendered dynamically with javascript
from selenium import webdriver
from colors import colors


class BasicCrawl:

    text = ''

    def __init__(self, company, url, class_name):
        self.company= company
        self.url = url
        self.class_name = class_name
        self.performCrawl(url, class_name)

    def performCrawl(self, url, class_name):
        print(colors.red + 'Crawling ' + self.company + '...' + colors.black)
        webDriver = webdriver.Chrome('/Users/trevorfox/Desktop/client-job-postings-scraper/chromedriver')
        webDriver.get(url)
        for count, i in enumerate(webDriver.find_elements_by_class_name(class_name)):
            self.text += (str(count+1) + '. ' + i.text.replace('\n',' ').replace('VIEW', '')) + "\n"
        webDriver.close()
        # print(self.text) - have to strip certain elements from diff websites postings

# class to strip certain text from 'text' variable .. such as "APPLY" "FULL-TIME",
# store output as CSV? to upload to a google sheets file