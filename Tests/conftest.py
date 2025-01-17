import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome(executable_path="E:\chromedriver.exe")
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    #yield
    #driver.close()