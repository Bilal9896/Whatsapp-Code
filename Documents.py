from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv
import codecs
filepath1 = 'C:\\Users\\Administrator.WIN-AAMH43Q2IFP\\Desktop\Whatsapp\\Routines\\Moj Brochere.pdf'
filepath2 = 'C:\\Users\\Administrator.WIN-AAMH43Q2IFP\\Desktop\Whatsapp\\Routines\\MOJ 2 Year Price Plan.pdf'
filepath3 = 'C:\\Users\\Administrator.WIN-AAMH43Q2IFP\\Desktop\Whatsapp\\Routines\\Price Plan Moj 1.pdf'
message_text = ""
filename="Verified_Numbers 27July.csv"
f = open(filename, "a")
#f.write("Hello Worl")
#f.close()

with codecs.open('Message.txt', 'r') as message_file:
    for text in message_file:
        message_text+=text
    str(message_text)
    print(message_text)
no_of_message = 1
with open('office_numbers.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
                      for row in csv.reader(csvfile, delimiter=';')]
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(30)
##name = 'fb38f2fe Me'
#input('Enter anything after scanning QR code')
def send_whatsapp_msg(phone_no, text):
    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
    )
    sleep(30)
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass
    try:
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")
            sleep (10)
    except Exception as e:
        print("Invailid phone no :" + str(phone_no))
def send_whatsapp_image(phone_no, doc1,doc2,doc3):
    filename="Verified_Numbers 27July.csv"
    f = open(filename, "a")
    try:
        driver.get(
            "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
        )
        sleep(30)
        #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        #user.click()
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()
        image_box = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(doc1)
        #add_more=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[2]/div/span')
        #add_more.click()
        image_box.send_keys(doc2)
        #add_more=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[2]/div/span')
        #add_more.click()
        image_box.send_keys(doc3)
        sleep(3)
        #text_box=driver.find_element_by_xpath(
        #    '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')
        send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        #text_box.send_keys(text)
        #sleep(5)
        send_button.click()
        sleep(10)
        #sleep(10)
        status="Verified"
        print(status)
        
       #f.write(str(phone_no))
       # f.close()
        f.write(str(phone_no)+"\n")
        f.close()
       # f.write(status)
        #f.close()
        print("Send")
        sleep(2)
        #sleep(5)
    except Exception as e:
       print("Invailid phone no :" + str(phone_no)) 
def main():
    for moblie_no in moblie_no_list:
        try:
            send_whatsapp_image(phone_no=moblie_no, doc1=filepath1,doc2=filepath2,doc3=filepath3)
        except Exception as e:
            sleep(10)
            is_connected()
        try:
          send_whatsapp_msg(phone_no=moblie_no, text=message_text)
        except Exception as e:
            sleep(10)
            is_connected()
if __name__ == '__main__':
    main()