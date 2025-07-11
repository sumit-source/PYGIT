import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://workspace.zencecrm.com/Auth/Login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='emailInput']").send_keys("sagar@easyrewardz.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Dummy@123")
driver.find_element(By.XPATH,"//button[@id='loginButton']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='erreportingdemo-program-div']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[@id='tabSpan2']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex justify-between mt-2 gap-2 items-center ']//div[@class='w-[100%]']").click()
time.sleep(2)
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
#search_input.clear()  # Optional: clear existing text
search_input.send_keys("India")
search_input.send_keys(Keys.RETURN)
time.sleep(4)
driver.find_element(By.XPATH, "(//*[@alt='View'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@class='w-[30px] cursor-pointer'][1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//label[normalize-space()='Select All']").click()
driver.find_element(By.XPATH, "//*[@class='absolute right-[15px] cursor-pointer'][1]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Title']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Title']").send_keys("E-Invoice")
driver.find_element(By.XPATH, "//*[@class='absolute right-[15px] cursor-pointer'][1]").click()
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C:\\Users\\sumit.dubey\\Downloads\\logo 1.png")
driver.find_element(By.XPATH, "(//*[@class='absolute right-[15px] cursor-pointer'])[2]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Tagline']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Tagline']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Tagline']").send_keys("From Acquisition to Retention Automation")
driver.find_element(By.XPATH, "(//*[@class='absolute right-[15px] cursor-pointer'])[2]").click()


# if "Zence" in
#driver.find_element(By.XPATH, "//img[@class='w-[30px] cursor-pointer']").click()
