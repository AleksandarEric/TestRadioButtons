from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_radio():
    driver = Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.implicitly_wait(2)

    radio_button1 = driver.find_element(By.ID, "my-radio-1")
    radio_button1.click()
    driver.implicitly_wait(2)

    radio_button2 = driver.find_element(By.ID, "my-radio-2")
    radio_button2.click()
    driver.implicitly_wait(2)



    if radio_button1.is_selected():
        print("Checked radio is selected.")
    else:
        print("Checked radio is not selected.")

    
    if radio_button2.is_selected():
        print("Checked radio is selected.")
    else:
        print("Checked radio is not selected.")



    driver.quit()


        
    
    