# couldn't use BeautifulSoup library because webpage is rendered dynamically with javascript
from selenium import webdriver
from colors import colors


class BasicCrawl:

    text = ''

    def __init__(self, company, url, class_name):
        self.company= company
        self.url = url
        self.class_name = class_name

    def performCrawl(self):
        print(colors.red + 'Crawling ' + self.company + '...' + colors.black)
        webDriver = webdriver.Chrome('/Users/trevorfox/Desktop/client-job-postings-scraper/chromedriver')
        webDriver.get(self.url)
        for count, i in enumerate(webDriver.find_elements_by_class_name(self.class_name)):
            self.text += (str(count+1) + '. ' + i.text.replace('\n',' ')) + "\n"
        webDriver.close()
        return self
        # print(self.text) - have to strip certain elements from diff websites postings

    def performExtraStepsCrawl(self, table_class_name, class_name_one, class_name_two):
        print(colors.red + 'Crawling ' + self.company + '...' + colors.black)
        webDriver = webdriver.Chrome('/Users/trevorfox/Desktop/client-job-postings-scraper/chromedriver')
        webDriver.get(self.url)
        for obj in webDriver.find_elements_by_class_name(table_class_name):
            for count, i in enumerate(obj.find_elements_by_class_name(class_name_one)):
                self.text += (str(count+1) + '. ' + i.text.replace('\n',' ')) + "\n"
            for count, i in enumerate(obj.find_elements_by_class_name(class_name_two)):
                self.text += (str(count + 1) + '. ' + i.text.replace('\n', ' ')) + "\n"
        webDriver.close()
        return self
        # print(self.text) - have to strip certain elements from diff websites postings


# store output as CSV? to upload to a google sheets file