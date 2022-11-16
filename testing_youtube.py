from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import os,sys, stat,json
import subprocess
from utilities import *








path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")




try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)



# driver.get("https://www.youtube.com")
# time.sleep(3)


# try:

#     c3_eles= driver.execute_script("return document.getElementsByClassName('c3-material-button-button')")
#     print("c3 eles",len(c3_eles))
#     if len(c3_eles)>0:
#         for i in range(0,len(c3_eles)):
#             if 'Accept' in driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"):
#                 time.sleep(5)
#                 driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].click()")
#                 print("c3 click")
#             else:
#                 print("c3 change",driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"))
#     else:
#         print("No c3 buttons")
# except Exception as e:
#     print("c3 error",e)
#     pass



# # video_url,channel_url=get_random_video()

driver.get("https://www.youtube.com")
time.sleep(3)



# set_driver_cookies(driver)
# driver.refresh()
time.sleep(30)
print(json.dumps(driver.get_cookies()))

driver.get("https://www.viewgrip.net/")
time.sleep(100)

print(json.dumps(driver.get_cookies()))

set_view_grip_cookies(driver)
# driver.refresh()
time.sleep(2)

driver.get("https://www.viewgrip.net/worker_session.php")
time.sleep(2)


driver.quit()


