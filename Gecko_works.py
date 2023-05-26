
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

    
driver=uc.Chrome(user_data_dir="c:\\temp\\freeman")#reating user profile

driver.get('https://www.coingecko.com/') #loading coingeckko site



class sign_in:

    print("hello gecko signing")\
    
    def __init__(self):
        pass

    
    def login(self, email, password ):

        self.email = email
        self.password = password

            
        try:
            #login section
            time.sleep(45)
            self.user=driver.find_element(By.CSS_SELECTOR,"[class='mr-3 text-black tw-text-sm tw-cursor-pointer hover:tw-text-primary-450']")
            self.user.click()
            print(f'logging {self.email} Gecko account')

            #email section
            time.sleep(45)
            self.email_log=driver.find_element(By.ID,"signInEmail")
            self.email_log.clear()
            self.email_log.send_keys(self.email)
            print('Email successfully inputed')

            #password section
            time.sleep(45)
            self.password_log=driver.find_element(By.ID,"signInPassword")
            self.password_log.clear()
            self.password_log.send_keys(self.password)
            print('password successfully inputed')

            #submit section
            time.sleep(45)
            self.submit=driver.find_element(By.ID,'sign-in-button')
            self.submit.click()
            print('Login credential successfully submitted')
            time.sleep(3)
            print(f'{self.email} coingecko acount is logged in.')
        except:
            print(f'{self.email} account already signed in')
            pass




class candy:

    #locating and clicking the candy 

    def candy_click(self):

        self.candy_notify=driver.find_element(By.CSS_SELECTOR,"[class ='mr-3 candy-notification-icon-section']")
        self.candy_notify.click()
        time.sleep(25)

        try:
            #clicking on candy button
            self.candy_collect=driver.find_element(By.CSS_SELECTOR,"[class='col-12 px-3']")
            self.candy_collect.click()
            print('candy collected')
        except:
            print('already colleected')

        


class signout: #signing out user 
   
    def logout(self, email):
            self.email = email
            
            self.hover_element=driver.find_element(By.CSS_SELECTOR,"[class='dropdown mr-3']")

            #locating the dropdown for signing out
            ActionChains(driver).move_to_element(self.hover_element).perform()
            time.sleep(25)
            self.appearing_ele=driver.find_element(By.CSS_SELECTOR,"[class='dropdown-item py-2 tw-text-sm']")
            self.appearing_ele.click()
            print(f'{self.email} coingecko account successfully signed out')
            time.sleep(20)
            driver.close()

        