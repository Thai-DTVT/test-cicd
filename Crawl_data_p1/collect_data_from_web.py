import requests
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from db_connection import *
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import re
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from urllib3.exceptions import InsecureRequestWarning
from selenium.webdriver.chrome.options import Options

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
  


# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")


# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By.XPATH, '//button')



def get_total_new(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    total=0
    
    try:
        get_total_bat_dong_san = driver.find_elements(By.XPATH, "//span[@id ='count-number']")
        
    except NoSuchElementException as E:
        print(E)
        driver.close()
        return total
    if get_total_bat_dong_san:
        total = int(get_total_bat_dong_san[0].text.replace('.',''))
    driver.close()
    return total
def get_total_pages(total, limit):
    total_pages = int(total/limit) + 1
    return total

def check_exists_new(id_new):
    query = "SELECT * FROM news where id_news  = '"+ str(id_new) +"'"
    conn.execute(query)
    rows = conn.fetchall()
    if len(rows)>0:
        return 1
    else:
        return 0



def insert_all_link_new():
    

    for province in get_all_provinces():
        count = 0
        link_province_origin = province[2]
        total_pages = get_total_pages(get_total_new(link_province_origin),2)
        for i in range(1, total_pages):
            count +=1
            if count <23:
                links = link_province_origin.split('?')
                full_link = links[0] + '/p'+str(i) +'?'+links[1]
                #full_link ="https://batdongsan.com.vn/nha-dat-ban-ben-tre?sortValue=1"
                driver = webdriver.Chrome()
                driver.delete_all_cookies()
                try:
                    driver.set_page_load_timeout(10) 
            
                    driver.get(full_link)
                except TimeoutException as ex:
                    driver.close()
                    continue
                time.sleep(5)
                get_list_news = driver.find_elements(By.XPATH, "//a[@class ='js__product-link-for-product-id']")
                check_exists = 0
                for link_new in get_list_news:
                    if check_exists > 2:
                        break
                    else:
                        get_link_origin = link_new.get_attribute('href')
                        id_new = to_decimal(get_link_origin.split('-pr')[-1])
                        
                        if check_exists_new(id_new) == 1:
                            check_exists+=1
                            continue
                        else:
                            try:
                                query_insert('news', href= get_link_origin, id_provinces= str(province[0]), status=str(0), id_news = str(id_new))
                            
                            except mysql.connector.Error as err:
                                print("Something went wrong: {}".format(err))
            else:
                continue
            

def get_all_infor(url):
    
    dict_infor = dict()
    driver = webdriver.Chrome()
    
    try:
        
        driver.set_page_load_timeout(10) 
        driver.get(url)
           
    except TimeoutException as ex:
        #driver.close()
        return dict_infor
        
        #driver.execute_script("window.stop();")
        
    try:
        get_title = driver.find_element(By.XPATH, "//h1[@class ='re__pr-title pr-title js__pr-title']")
        dict_infor['title'] = get_title.text
    except NoSuchElementException:
        dict_infor['title'] = ''
        #driver.close()
        return dict_infor
            #dict_infor['title'] = get_title.text 
        
    
    #time.sleep(2)
    #get_title = driver.find_element(By.XPATH, "//h1[@class ='re__pr-title pr-title js__pr-title']")
    #if get_title ==[]:
        #dict_infor['title'] = ''
    #else:
    #try:
        #get_title = driver.find_element(By.XPATH, "//h1[@class ='re__pr-title pr-title js__pr-title']")
        #dict_infor['title'] = get_title.text

    #except NoSuchElementException:
            #dict_infor['title'] = ''
            #driver.close()
            #return dict_infor
    
    get_title = driver.find_element(By.XPATH, "//h1[@class ='re__pr-title pr-title js__pr-title']")
    dict_infor['title'] = get_title.text
    try:
        get_address = driver.find_element(By.XPATH, "//span[@class ='re__pr-short-description js__pr-address']")
        dict_infor['address'] = get_address.text
    except NoSuchElementException:
        pass
    short_description =  driver.find_elements(By.XPATH, "//div[@class ='re__pr-short-info-item js__pr-short-info-item']")
    for item in short_description:
        title = item.find_element(By.CLASS_NAME, 'title')
        value = item.find_element(By.CLASS_NAME, 'value')
        try:
            ext = item.find_element(By.CLASS_NAME, 'ext')
        except NoSuchElementException:
            pass
        dict_infor[title.text] = value.text
    div_description = driver.find_element(By.XPATH, "//div[@class ='re__section re__pr-description js__section js__li-description']")
    description = div_description.find_element(By.XPATH, "//div[@class ='re__section-body re__detail-content js__section-body js__pr-description js__tracking']")
    #div_other_infor =  driver.find_element(By.XPATH, "//div[@class ='re__pr-specs-content js__other-info']")
    div_other_infor_items = driver.find_elements(By.XPATH, "//div[@class ='re__pr-specs-content-item']")
    dict_infor['description'] = (description.text).replace("'",'"')
    #NAME POST
    person_post = None
    name_person_post = ''
    try:
        person_post = driver.find_element(By.XPATH, "//div[@class ='re__contact-name js_contact-name']")
        
    except NoSuchElementException:
        pass
    if person_post:
        name_person_post = person_post.get_attribute('title')
    
    #ID PERSON POST
    get_contact = driver.find_element(By.XPATH, "//div[@class ='re__sidebar-box re__contact-box js__contact-box']")
    person_post_2 = get_contact.find_element(By.TAG_NAME, "a")
    id_person_post = person_post_2.get_attribute('href').split('/p/')[1].split("?")[0]
    dict_infor['name_per'] = name_person_post
    dict_infor['id_per'] = id_person_post
    

    #INFOR OTHER
    for infor in div_other_infor_items:
        title = infor.find_element(By.CLASS_NAME, 're__pr-specs-content-item-title')
        value = infor.find_element(By.CLASS_NAME, 're__pr-specs-content-item-value')
        dict_infor[title.text] = value.text
        
        
    
    #IMAGE
    div_image = None
    dict_infor['images'] = None
    try:
        div_image =  driver.find_element(By.XPATH, "//div[@class ='re__pr-media-slide js__pr-media-slide']")
        
    except NoSuchElementException:
        pass
    if div_image:
        div_image_items = div_image.find_elements(By.TAG_NAME, "img")
        list_image = []
        for image in div_image_items:
            url_image = image.get_attribute('src')
            if url_image:
                list_image.append(url_image)
    #ADD IMAGE
        dict_infor['images'] = ",".join(list_image)
    

    #DATE
    get_date_div = driver.find_element(By.XPATH, "//div[@class ='re__pr-short-info re__pr-config js__pr-config']")
    get_date = get_date_div.find_elements(By.XPATH, "//div[@class ='re__pr-short-info-item js__pr-config-item']")
    #data_date = dict()
    for date in get_date:
        key = date.find_element(By.CLASS_NAME, 'title')
        
        value = date.find_element(By.CLASS_NAME, 'value') 
        change_format_date = value.text
        if key.text == 'Ngày đăng' or key.text == 'Ngày hết hạn': 
            change_format_date = datetime.strptime(value.text, '%d/%m/%Y').strftime('%Y-%m-%d')
        dict_infor[key.text] = change_format_date
        
    #PHONE NUMBER

    try:
        get_phone = driver.find_element(By.XPATH, "//a[@class ='re__btn re__btn-se-border--md js__zalo-chat']")
        phone_number = get_phone.get_attribute('data-href').split('/')[-1]
        dict_infor['phone'] = phone_number
    except NoSuchElementException:
        pass
    #the loai
    detailAdd = driver.find_elements(By.XPATH, "//div[@class='re__breadcrumb js__breadcrumb']")    
    if detailAdd ==[]:
        dict_infor['title_add'] = '' 
    else:       
        get_title_add = detailAdd[0].find_elements(By.XPATH, "//a[@level='4']") 
        title_add = get_title_add[0].text
        dict_infor['title_add'] = title_add
    #tinh
    detailAdd = driver.find_elements(By.XPATH, "//div[@class='re__breadcrumb js__breadcrumb']")    
    if detailAdd ==[]:
        dict_infor['title_provines'] = '' 
    else:       
        get_title_provines = detailAdd[0].find_elements(By.XPATH, "//a[@level='2']") 
        title_provines = get_title_provines[0].text
        dict_infor['title_provines'] = title_provines
    #HANDLE _UNIT
    fix_unit = dict()
    for key_handle, value_handle in dict_infor.items():
        if key_handle == 'Mức giá':
            
            value = value_handle
            fix_unit['price'] = to_decimal(value)
            
            if not fix_unit['price']:
                fix_unit['price'] = 'Thỏa thuận'
                fix_unit['unit_price'] = ''
            else:
                fix_unit['unit_price'] = to_unit(value_handle)
            
        if key_handle == 'Diện tích':
            value = to_decimal(value_handle)
            unit = to_unit(value_handle)
            
            fix_unit['unit_area'] = unit
            fix_unit['area'] = value
        if key_handle == 'Số phòng ngủ':
            value = to_decimal(value_handle)
            unit = to_unit(value_handle)
            fix_unit['bedroom'] = value
        if key_handle == 'Mặt tiền':
            value = to_decimal(value_handle)
            unit = to_unit(value_handle)
            fix_unit['face_first'] = value
        if key_handle == 'Đường vào':
            value = to_decimal(value_handle)
            unit = to_unit(value_handle)
            fix_unit['road'] = value
        if key_handle == 'Số tầng':
            value = to_decimal(value_handle)
            fix_unit['floor'] = value
        if key_handle == 'Số toilet':
            value = to_decimal(value_handle)
            unit = to_unit(value_handle)
            fix_unit['toilet'] = value
    dict_infor = Merge(dict_infor,fix_unit)
    
    #list_del = ['Mức giá','Diện tích' ,'Số phòng ngủ','Số toilet']
    
    return dict_infor
      
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
        
def to_decimal(str):
    filter = re.findall('-?\d+(?:\,\d+)?', str.replace(".",""))
    if filter:
        return filter[0]
    else:
        return None
   

def to_unit(str):
    return str.split(' ')[-1]



    


    
# url = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-phuong-tay-mo-prj-the-sakura-vinhomes-smart-city/cuc-re-3pn-dien-tich-82m2-chi-3-3-ty-ck-20-ban-cong-dn-nhan-nha-o-luon-mien-5-nam-dich-vu-pr37874458'
# get_all_infor(url) 





