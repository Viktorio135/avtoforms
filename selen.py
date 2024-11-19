import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://imex-service.ru/booking/'
length = 13.6
width = 2.5
height = 4
weight_transport = 8000
weight_kon = 2100
mail = 'cheravto@mail.ru'


   
def main(inn, surname, name, number_phone, brand, model, color, gos_number):
        
        start = time.time()
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
        driver = webdriver.Chrome(options=options)
        driver.get(url=url)



        def page_up(num):
            scroll_vаlue = -num
            scroll_by = f'window.scrollBy(0, {scroll_vаlue});'
            driver.execute_script(scroll_by)

        def page_down(num):
            scroll_vаlue = num
            scroll_by = f'window.scrollBy(0, {scroll_vаlue});'
            driver.execute_script(scroll_by)


        driver.implicitly_wait(10)

        #step1 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/div/div[2]/div/select/option[13]').click()#выбор типа транспорта
        step1 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/div/div[2]/div/select/option[11]'))
        )
        
        
        
        step1.click()
        #step2 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/div/div[4]/select/option[1]').click()#кол-во пассажиров
        #step2 = WebDriverWait(driver, 10).until(
            #EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/div/div[2]/div/select/option[1]'))
        #)
        #step2.click()
        #step3 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div[2]/div[3]/div/form/button').click()#продолжить
        step3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/main/div[2]/div[3]/div/div/button'))
        )
        step3.click()
        #step4 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input')#марка
        step4 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div/div/form/div[2]/div/div[1]/div/input'))
        )
        step4.send_keys(brand)

        #step5 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[2]/input').send_keys(model)#модель
        step5 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div/div/form/div[2]/div/div[2]/div/input'))
        )
        step5.send_keys(model)

        #step6 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[3]/input').send_keys(color)#цвет
        step6 = WebDriverWait(driver,10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[3]/div[1]/input'))
        )
        step6.send_keys(color)
   
        #step7 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[4]/input').send_keys(gos_number)#гос номер
        step7 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[4]/div[1]/input'))
        )
        step7.send_keys(gos_number)
        
        page_down(4000)
       
        #step8 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[1]/div/input').send_keys(length)#длина
        step8 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[1]/div[1]/input'))
        )
        step8.send_keys(length)

        #step9 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[2]/div/input').send_keys(width)#ширина
        step9 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[2]/div[1]/input'))
        )
        step9.send_keys(width)
        
        #step10 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[3]/div/input').send_keys(height)#высота
        step10 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[3]/div[1]/input'))
        )
        step10.send_keys(height)
        
        #step11 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[4]/div[1]/input').send_keys(weight_transport)#вес транспорта
        step11 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[5]/div/div/div/div[4]/div[1]/input'))
        )
        step11.send_keys(weight_transport)
        
        page_down(1000)
        #step12 = driver.find_element(By.XPATH, '//*[@id="form"]/div/form/div[2]/div/div[6]/div/div[1]')#есть ли груз
        time.sleep(1)
        step12 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div/form/div[2]/div/div[6]/div/div[1]'))
        )
        
        step12.click()
        
        #step13 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[7]/input').send_keys('стройматериалы')# название груза
        step13 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[7]/input'))
        )
        step13.send_keys('стройматериалы')

        #step14 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[9]/div/input')
        step14 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[9]/div[1]/input'))# вес груза
        )

        step14.send_keys(Keys.LEFT)
        step14.send_keys(weight_kon)


        page_up(4500)
        
        time.sleep(.5)
        #step15 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div[2]/div[2]/div/div[1]/ul/li[4]/a').click()# кнопка данные
        step15 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/main/div[2]/div[2]/div/div[1]/ul/li[4]/a'))
        )
        time.sleep(.5)
        step15.click()
        
        
        #step16 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[1]/div[2]/label').click()#юр лицо
        step16 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[1]/div[2]/label'))
        )
        step16.click()

        
        #step17 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[2]/div[1]/input').send_keys(inn)#инн
        step17 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[2]/div[1]/input'))
        )
        step17.send_keys(inn)

        
        #step18 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[2]/div/button').click()#заполнить
        step18 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[2]/div/button'))
        )
        step18.click()

        #step19 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[7]/div/div/div/div[1]/input').send_keys('логист')#должность
        step19 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[7]/div/div/div/div[1]/input'))
        )
        step19.send_keys('логист')
        
        #step20 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[7]/div/div/div/div[2]/input').send_keys(surname)#фамилия
        step20 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[7]/div/div/div/div[2]/input'))
        )
        step20.send_keys(surname)
        
        #step21 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[7]/div/div/div/div[3]/input').send_keys(name)#имя
        step21 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[7]/div/div/div/div[3]/input'))
        )
        step21.send_keys(name)
        
        #step22 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[8]/div/div/div/div[1]/input').send_keys(number_phone)#номер телефона
        step22 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[8]/div/div/div/div[1]/input'))
        )
        step22.send_keys(number_phone)
        
        #step23 = driver.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/form/form[1]/div/div[2]/div/div[8]/div/div/div/div[2]/input').send_keys(mail)#маил
        step23 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/div[2]/div[1]/form[1]/div/div[2]/div/div[8]/div/div/div/div[2]/input'))
        )
        step23.send_keys(mail)

        page_down(1000)
        time.sleep(.4)

        #step24 = driver.find_element(By.XPATH, '//*[@id="matchPayer-Отправитель"]').click()#совп с плат
        step24 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '//*[@id="matchPayer-Отправитель"]'))
        )
        time.sleep(.4)
        step24.click()

        #step25 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div[2]/div/div[2]/form/form[3]/div/div/div/label').click()#совп с плат
        step25 = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, '//*[@id="matchPayer-Получатель"]'))
        )
        step25.click()

        page_down(300)
        time.sleep(.3)

        #step26 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div[2]/div/div[2]/div/div/div[2]/label').click()#счет на оплату

        print(time.time() - start)
        
        page_up(1000)
        time.sleep(40)


        

