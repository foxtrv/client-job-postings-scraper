# couldn't use BeautifulSoup library because webpage is rendered dynamically with javascript
from selenium import webdriver
from colors import colors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasicCrawl:

    text = ''

    def __init__(self, company, url, class_name):
        self.company= company
        self.url = url
        self.class_name = class_name


    def waitForElementToLoad(self, webDriver, element):
        try:
            return WebDriverWait(webDriver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
        except:
            print('Crawl did not parse correctly. (Find-by element was not found on page)')
            return self

    def performCrawl(self):
        print(colors.red + 'Crawling ' + self.company + '...' + colors.black)
        webDriver = webdriver.Chrome('/Users/trevorfox/Desktop/client-job-postings-scraper/chromedriver')
        webDriver.get(self.url)
        # wait a moment for the website to finish loading
        try:
            self.waitForElementToLoad(webDriver, self.class_name)
        except:
            webDriver.close()
            return self # do not write null results to output. exit, essentially

        for count, i in enumerate(webDriver.find_elements_by_class_name(self.class_name)):
            self.text += (str(count+1) + '. ' + i.text.replace('\n',' ')) + "\n"
        webDriver.close()
        return self
        # print(self.text) - have to strip certain elements from diff websites postings




    def performCrawlWithExtraClicksAndScrollTo(self, scroll_to):
        print(colors.red + 'Crawling ' + self.company + '...' + colors.black)
        webDriver = webdriver.Chrome('/Users/trevorfox/Desktop/client-job-postings-scraper/chromedriver')
        webDriver.get(self.url)
        # wait a moment for the website to finish loading
        try:
            self.waitForElementToLoad(webDriver, self.class_name)
        except:
            webDriver.close()
            return self # do not write null results to output. exit, essentially

        for box in webDriver.find_elements(By.CLASS_NAME, scroll_to):
            # scroll to item, then click on item
            element = box
            webDriver.execute_script('arguments[0].scrollIntoView(true);', element)
            # scroll up slightly, because for some reason box is out of view
            webDriver.execute_script('window.scrollBy(0,-100)')
            try:
                element.click()
            except:
                print('Crawl did not parse correctly. (Could not click on element)')
                webDriver.close()
                return self

            for count, i in enumerate(webDriver.find_elements_by_class_name(self.class_name)):
                if i.text != '':
                    self.text += (str(count+1) + '. ' + i.text.replace('\n',' ')) + "\n"

        webDriver.close()
        return self
        # print(self.text) - have to strip certain elements from diff websites postings







    def performExtraStepsCrawl(self, table_class_name, class_name_one, class_name_two):
        print(colors.red + 'Crawling ' + self.company + '...' + colors.black)
        webDriver = webdriver.Chrome('/Users/trevorfox/Desktop/client-job-postings-scraper/chromedriver')
        webDriver.get(self.url)
        # wait a moment for the website to finish loading
        try:
            self.waitForElementToLoad(webDriver, self.class_name)
        except:
            webDriver.close()
            return self # do not write null results to output. exit, essentially

        for obj in webDriver.find_elements_by_class_name(table_class_name):
            for count, i in enumerate(obj.find_elements_by_class_name(class_name_one)):
                self.text += (str(count+1) + '. ' + i.text.replace('\n',' ')) + "\n"
            for count, i in enumerate(obj.find_elements_by_class_name(class_name_two)):
                self.text += (str(count + 1) + '. ' + i.text.replace('\n', ' ')) + "\n"
        webDriver.close()
        return self
        # print(self.text) - have to strip certain elements from diff websites postings


# store output as CSV? to upload to a google sheets file