import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from navigation import autofill_login
from navigation import click_forgot_password

# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


#TC01: Đổi mật khẩu thành công
def test_forgot_password(driver):
    autofill_login(driver, "alexson6060@gmail.com", "45439")
    click_forgot_password(driver)
    time.sleep(5)
    
    # In ra thông báo để nhập mã xác minh
    print("Nhập mã xác minh từ email:", flush=True)  # Đảm bảo in ra ngay lập tức
    time.sleep(10)  # Thêm một chút thời gian để chắc chắn dòng chữ hiển thị
    
    # Tạm dừng để nhập mã xác minh thủ công
    verification_code = input("Nhập mã xác minh từ email: ", flush=True)
    
    #nhập pass
    driver.find_element(By.ID, "np").send_keys("12345")
    driver.find_element(By.ID, "rnp").send_keys("12345")
    
    #Nhập mã xác minh
    driver.find_element(By.ID, "vcode").send_keys(verification_code)
    
    #Nhấn nút đổi mật khẩu
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(3)

