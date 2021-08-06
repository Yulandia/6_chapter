from selenium import webdriver
from selenium.webdriver.support.color import Color


driver = webdriver.Chrome(executable_path='drivers/chromedriver')
# to start Firefox use the line below
#driver = webdriver.Firefox(executable_path='drivers/geckodriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()  #m aximizing the browser window

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

#getting the background color of the button
backround_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("John")

lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Smith")

email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("tyakina88@yahoo.com")

telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("7736729773")

continue_btn = driver.find_element_by_xpath("//input[@value='Continue']")

#getting the background color of the Continue button
backround_color = continue_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgba == 'rgba(34, 154, 200, 1)'
continue_btn.click()

driver.quit()