# <username> => insert your username
# <password> => insert your password


from lib2to3.pgen2 import driver
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys





def click():
    pass


class InstaBot:
    def get_names1(self):
        sleep(5)
        scroll_box = self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        last_ht, ht = 0, 1

        while last_ht != ht:
            last_ht = ht
            sleep(2)

            ht = self.driver.execute_script("""
                                   arguments[0].scrollTo(0 , arguments[0].scrollHeight);
                                   return arguments[0].scrollHeight ;
                                   """, scroll_box)

        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        sleep(3)
        p = self.driver.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
        p.click()

        return names

    def get_names2(self):
        sleep(5)
        scroll_box = self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        last_ht, ht = 0, 1

        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                                   arguments[0].scrollTo(0 , arguments[0].scrollHeight);
                                   return arguments[0].scrollHeight ;
                                   """, scroll_box)

        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        sleep(3)
        p = self.driver.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
        p.click()


        return names


    def __init__(self, username, password):
        self.driver = webdriver.Chrome()

        self.username = username
        self.password = password

        self.driver.get("https://www.instagram.com/")

        
        self.driver.find_element(by="name", value="username").send_keys(self.username)
        self.driver.find_element(by="name", value="password").send_keys(self.password)
        self.driver.find_element(by="name", value="password").send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Not Now')]").click()

        sleep(5)
        self.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Not Now')]").click()
        sleep(5)

        
        
        self.driver.get("https://www.instagram.com/<username>/")
        

       
        self.driver.get("https://www.instagram.com/<username>/followers/")
        sleep(1)
        followers = self.get_names1()

        self.driver.get("https://www.instagram.com/<username>/following/")
        sleep(1)
        following = self.get_names2()

        not_follows = [user for user in following if user not in followers]
        print()
        for item in not_follows :
            print('https://www.instagram.com/'+item+'/')


        sleep(1000)






my_bot = InstaBot(<username>, <password>) 
