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
filepath = 'C:\\Users\\Administrator.WIN-AAMH43Q2IFP\\Desktop\\Whatsapp\\July 24\\Image24.jpeg'
message_text = ""
filename="Compain 24July.csv"
f = open(filename, "a")
#f.write("Hello Worl")
#f.close()


with open('Numbers List 24July.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
                      for row in csv.reader(csvfile, delimiter=';')]
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(30)
##name = 'fb38f2fe Me'
#input('Enter anything after scanning QR code')
def send_whatsapp_image(phone_no, image):
    try:
        filename="Compain 24July.csv"
        f = open(filename, "a")
        driver.get(
            "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
        )
        sleep(20)
        #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        #user.click()
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()
        image_box = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        sleep(3)
        send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        send_button.click()
        status="Verified"
        print(status)
        sleep(15)
       #f.write(str(phone_no))
       # f.close()
        f.write(str(phone_no)+"\n")
        f.close()
       # f.write(status)
        #f.close()
        print("Send")
        sleep(5)
    except Exception as e:
       print("Invailid phone no :" + str(phone_no)) 
def main():
    for moblie_no in moblie_no_list:
       # try:
        #    send_whatsapp_msg(phone_no=moblie_no, text=message_text)
        #except Exception as e:
        #    sleep(10)
        #    is_connected()
        #try:
        #    send_whatsapp_msg(phone_no=moblie_no, text=message_text)
        #except Exception as e:
        #    sleep(10)
        #    is_connected()
        try:
            send_whatsapp_image(phone_no=moblie_no, image=filepath)
        except Exception as e:
            sleep(10)
            is_connected()
if __name__ == '__main__':
    main()