from selenium import webdriver
from selenium. webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import pandas as pd

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
brower=webdriver.Chrome("C:/Users/boyin/OneDrive/Desktop/project 127 byjus/chromedriver.exe")
browser.get(start_url)
time.sleep(10)
scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source, "html.parcel")
    bright_star_table=soup.find("table",attrs={"class","wikitable"})
    table_body=bright_star_table.find('tbody')
    table_rows=table_body.find_all("tr")
    for row in table_rows:
        table_cols= row.find_all("td")
        temp_list=[]
        for col_data in table_cols:
            data=col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)

scrape()

stars_data=[]
for i in range(0,len(scraped_data)):
    star_names=scraped_data[i][1]
    distance=scraped_data[i][3]
    mass=scraped_data[i][5]
    radius=scraped_data[i][6]
    lum=scraped_data[i][7]
    required_data=[Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
print (stars_data)
headers=['Star_name','Distance', 'Dass', 'Radius', 'Luminosity']
star_df_1=pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")

