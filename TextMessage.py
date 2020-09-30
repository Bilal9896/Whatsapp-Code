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
#filepath = 'C:\\Users\\Administrator.WIN-AAMH43Q2IFP\\Desktop\\Whatsapp\\July 27\\MessageImage.jpg'
message_text = ""
filename="Verified_Numbers 27July.csv"
f = open(filename, "a")
#f.write("Hello Worl")
#f.close()

with codecs.open('Message27.txt', 'r') as message_file:
    for text in message_file:
        message_text+=text
    str(message_text)
    print(message_text)
no_of_message = 1
with open('Compaign 27July.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
                      for row in csv.reader(csvfile, delimiter=';')]
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(20)
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
    except Exception as e:
        print("Invailid phone no :" + str(phone_no))
def main():
    for moblie_no in moblie_no_list:
        try:
            send_whatsapp_msg(phone_no=moblie_no, text=message_text)
        except Exception as e:
            sleep(10)
            is_connected()
        #try:
        #    send_whatsapp_msg(phone_no=moblie_no, text=message_text)
        #except Exception as e:
        #    sleep(10)
        #    is_connected()
        try:
            send_whatsapp_image(phone_no=moblie_no, image=filepath,text=message_text)
        except Exception as e:
            sleep(10)
            is_connected()
if __name__ == '__main__':
    main()