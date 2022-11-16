from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import random 
import os,sys, stat,json
import subprocess
from utilities import *
import regex as re
from datetime import datetime
# from xvfbwrapper import Xvfb






# print(subprocess.Popen("npm install chromium-version@77",shell=True,stdout=subprocess.PIPE).communicate()[0])
# chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())

# print(subprocess.Popen("npm install xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])




# print(subprocess.Popen("yum localinstall google-chrome-stable.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("yum -y install xorg-x11-server-Xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# vdisplay = Xvfb()
# vdisplay.start()
chrome_path=r"/usr/bin/google-chrome-stable"
os.environ['CHROME_PATH']=chrome_path
path=r"chrome/chromedriver"
path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
# options.binary_location =binary_path
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_extension(os.getcwd()+"/chrome/utubehits.crx")

options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
# options.add_extension('chrome/vpn.crx')


# try:
#     driver = webdriver.Chrome(executable_path=path,chrome_options=options)
# except Exception as e:
#     print(e)


# driver.get("https://www.youtube.com")
# time.sleep(3)


# # print(json.dumps(driver.get_cookies()))
# set_driver_cookies(driver)
# driver.refresh()

# driver.execute_script("window.open('');")
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(3)

# driver.get("chrome-extension://khpcbjppaikkkfnpgbbkjgnbponddmbe/popup.html")

# time.sleep(2)

# try:
#     driver.execute_script('return document.querySelectorAll("input")[0].value="betagamma2064@gmail.com"')
#     time.sleep(1.5)
#     driver.execute_script('return document.querySelectorAll("input")[1].value="gamma2064beta"')
#     time.sleep(2)
#     driver.execute_script('return document.querySelectorAll("button#connect")[0].click()')

#     time.sleep(1)
#     driver.refresh()
#     time.sleep(3)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#start'))).click()
#     # driver.execute_script('return document.querySelectorAll("button#start")[0].click()')
# except Exception as e:
#     print(e)


try:
    driver1 = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)

# turn_on_vpn(driver1)

driver1.get("https://www.youtube.com")
time.sleep(3)


# print(json.dumps(driver.get_cookies()))
set_driver_cookies(driver1)
driver1.refresh()


try:
    driver1.get("https://utubehits.com/#dashboard")
    driver1.execute_script("""return document.querySelectorAll("a[onclick^=signin]")[0].click()""")
    time.sleep(4)
    driver1.execute_script("""return document.querySelectorAll("input")[0].value="betagamma2064@gmail.com" """)
    time.sleep(1)
    driver1.execute_script("""return document.querySelectorAll("input")[1].value="gamma2064beta" """)
    time.sleep(1.5)
    driver1.execute_script("""return document.querySelectorAll("span#connect")[0].click()""")
    time.sleep(5)
    driver1.get("https://utubehits.com/#exchange#like")
    main_window=driver1.window_handles[-1]
    time.sleep(5)
    likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")[0].children""")
    print(likes,len(likes))
    time_start=datetime.now()
    k=1
    while((datetime.now()-time_start).seconds<1300):
        driver1.save_screenshot("vinay2210974_main.png")
        upload_basic("vinay2210974_main.png",'16R8tV95HZpZiUWdMmWUAvU2lJOHAvUSa')
        time.sleep(20)

        try:
            try:
                if k>25 and k<28:
                    driver1.switch_to.window(main_window)
                    driver1.get("https://utubehits.com/#dashboard")
                    if driver.execute_script("""return document.querySelectorAll("a[onclick^=check]")[1].attributes["class"].value.includes("disabled")""") == False:
                        driver.execute_script("""return document.querySelectorAll("a[onclick^=check]")[1].click()""")
                    driver1.get("https://utubehits.com/#exchange#like")
                    time.sleep(3)
            except:
                driver1.get("https://utubehits.com/#exchange#like")
                time.sleep(3)

            if len(driver1.window_handles)>1:
                driver1.switch_to.window(driver1.window_handles[-1])
                driver1.close()    
                driver1.switch_to.window(main_window)
            driver1.execute_script("""return document.querySelectorAll("div#getpoints")[0].children[1].querySelectorAll("a[onclick^=click]")[0].click()""".format(1))
            
            time.sleep(6)
            print(driver1.window_handles)
            driver1.switch_to.window(driver1.window_handles[-1])
            try:
                print(driver1.execute_script("""return document.querySelectorAll("#segmented-like-button > ytd-toggle-button-renderer > yt-button-shape > button")[0].ariaPressed"""))
                if driver1.execute_script("""return document.querySelectorAll("#segmented-like-button > ytd-toggle-button-renderer > yt-button-shape > button")[0].ariaPressed""")=='false':
                    driver1.execute_script("""return document.querySelectorAll("#segmented-like-button > ytd-toggle-button-renderer > yt-button-shape > button")[0].click()""")
                print(driver1.execute_script("""return document.querySelectorAll("button[aria-label^=like]")[0].ariaPressed"""))
                if driver1.execute_script("""return document.querySelectorAll("button[aria-label^=like]")[0].ariaPressed""")=='false':
                    driver1.execute_script("""return document.querySelectorAll("button[aria-label^=like]")[0].click()""")
            except Exception as e:
                print(e)
                if driver1.execute_script("""return document.querySelectorAll("button[aria-label^=like]")[0].ariaPressed""")=='false':
                    driver1.execute_script("""return document.querySelectorAll("button[aria-label^=like]")[0].click()""")
            time.sleep(2)
            driver1.close()
            driver1.switch_to.window(main_window)
            time.sleep(4)
            k=k+1
            if k%10==0:
                driver1.switch_to.window(main_window)
                driver1.get("https://utubehits.com/#exchange#like")
                likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")[0].children""")
                print("in",len(likes))
                if len(likes)<=1:
                    driver1.switch_to.window(main_window)
                    driver1.get("https://utubehits.com/#exchange#like")
                    likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")""")
                    print("inner",len(likes))
                    if len(likes)<=1:
                        break



        except Exception as e:
            print(e)
            driver1.switch_to.window(main_window)
            driver1.get("https://utubehits.com/#exchange#like")
            time.sleep(5)
            likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")""")
            print("inner",len(likes))
            if len(likes)<=1:
                break
    k=1
    driver1.switch_to.window(main_window)
    driver1.get("https://utubehits.com/#exchange#subscribe")
    time.sleep(7)
    while((datetime.now()-time_start).seconds<1300):
        time.sleep(20)
        try:
            try:
                if k>25 and k<28:
                    driver1.switch_to.window(main_window)
                    driver1.get("https://utubehits.com/#dashboard")
                    if driver.execute_script("""return document.querySelectorAll("a[onclick^=check]")[2].attributes["class"].value.includes("disabled")""") == False:
                        driver.execute_script("""return document.querySelectorAll("a[onclick^=check]")[2].click()""")
                    driver1.switch_to.window(main_window)
                    driver1.get("https://utubehits.com/#exchange#subscribe")
                    time.sleep(3)
            except:
                driver1.switch_to.window(main_window)
                driver1.get("https://utubehits.com/#exchange#subscribe")
                time.sleep(3)


            if len(driver1.window_handles)>1:
                driver1.switch_to.window(driver1.window_handles[-1])
                driver1.close()    
                driver1.switch_to.window(main_window)
            driver1.execute_script("""return document.querySelectorAll("div#getpoints")[0].children[1].querySelectorAll("a[onclick^=click]")[0].click()""".format(1))
            
            time.sleep(6)
            print(driver1.window_handles)
            driver1.switch_to.window(driver1.window_handles[-1])
            try:
                if len(driver1.execute_script("""return document.querySelectorAll("#subscribe-button > ytd-subscribe-button-renderer > tp-yt-paper-button[aria-label^=Subscribe]")""")) !=0:
                    driver1.execute_script("""return document.querySelectorAll("#subscribe-button > ytd-subscribe-button-renderer > tp-yt-paper-button[aria-label^=Subscribe]")[0].click()""")
            except:
                pass
            time.sleep(5)
            driver1.close()
            driver1.switch_to.window(main_window)
            time.sleep(4)
            k=k+1
            if k%10==0:
                driver1.get("https://utubehits.com/#exchange#subscribe")
                likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")[0].children""")
                if len(likes)<=1:
                    driver1.get("https://utubehits.com/#exchange#subscribe")
                    likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")""")
                    if len(likes)<=1:
                        break


        except Exception as e:
            print(e)
            driver1.get("https://utubehits.com/#exchange#subscribe")
            likes=driver1.execute_script("""return document.querySelectorAll("div#getpoints")""")
            if len(likes)==0:
                break







except Exception as e:
    print("utubehits main login error",e)




time.sleep(3000)




driver1.quit()
# vdisplay.stop()