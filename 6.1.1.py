from selenium import webdriver
from selenium.webdriver.support.color import Color


driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
# to start Firefox use the line below
#driver = webdriver.Firefox(executable_path='drivers/geckodriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()  #maximizing the browser window

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

#Enter the Password

password_field = driver.find_element_by_xpath("//div/div[2]")
password_field_class = password_field.get_attribute("class")

password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("hello123")

login_btn = driver.find_element_by_xpath("//input[@value='Login']")

#getting the background color of the button
background_color = login_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
converted_background_color.rgba == 'rgba(34, 154, 200, 1)'
login_btn.click()

driver.close()