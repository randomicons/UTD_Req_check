from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def get_classes(userid_str, password_str):
    driver = webdriver.Firefox()
    url = "https://www.utdallas.edu/orion/"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != url)
    print(driver.title, driver.current_url)

    username = driver.find_element_by_id("netid")
    password = driver.find_element_by_id("password")
    username.clear()
    password.clear()
    username.send_keys(userid_str)
    password.send_keys(password_str)
    password.send_keys(Keys.RETURN)

    url = driver.current_url
    wait.until(lambda driver: "utsystem.edu" in driver.current_url)
    driver.get(
        "https://dacs-prd.utshare.utsystem.edu/psc/DACSPRD/EMPLOYEE/CSUTD/c/SA_LEARNER_SERVICES.SSS_MY_ACAD.GBL?Page=SSS_MY_ACAD&Action=U"
    )

    url = driver.current_url
    wait.until(
        lambda driver: driver.find_element_by_id("DERIVED_SSSACA2_SSS_ACAD_HISTORY")
    )
    print(driver.title)

    elem = driver.find_element_by_id("DERIVED_SSSACA2_SSS_ACAD_HISTORY")
    elem.click()

    wait.until(
        lambda driver: driver.find_element_by_id("ACE_DERIVED_SSS_HST_$64$"))

    elem = driver.find_element_by_id("ACE_DERIVED_SSS_HST_$64$")

    print(elem.text)