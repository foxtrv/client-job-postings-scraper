# couldn't use BeautifulSoup library because webpage is rendered dynamically with javascript
from selenium import webdriver

webDriver = webdriver.Chrome('/Users/trevorfox/PycharmProjects/zumeScraper/chromedriver')
webDriver.get('https://zumepizza.com/careers')

for count, i in enumerate(webDriver.find_elements_by_class_name("job-item")):
    print(str(count+1) + '. ' + i.text.replace('\n',' ').replace('VIEW', ''))

webDriver.close()