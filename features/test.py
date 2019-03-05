from selenium import webdriver

driver = webdriver.Chrome("D:\Install programs\Python and Selenium\chromedriver")
driver.get("https://wikipedia.org")

search_field = driver.find_element_by_id("searchInput")
search_field.send_keys("test text")

search_button = driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button")
search_button.click()

assert "test text" in driver.title



driver.quit()