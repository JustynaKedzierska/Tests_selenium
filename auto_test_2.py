from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/home/justyna/TestFiles/chromedriver')
driver.get('https://saved.io')
title1 = driver.title
print(title1)
assert title1 == "Saved.io - simple online bookmarks"
driver.quit()