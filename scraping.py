import sqlite3

import requests
from bs4 import BeautifulSoup
import pandas
import argparse


def connect(db):
    conn=sqlite3.connect(db)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT)")
    print("Table has been created successfully...")
    conn.close()
    

def insert_row(db, values):
    conn= sqlite3.connect(db)
    insert_val= "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE) VALUES (?, ?, ?)"
    conn.execute(insert_val, values)
    conn.connect()
    conn.close()
    
    
def get_info(db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
        
parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse: ", type=str)
parser.add_argument("--name", help="Enter the name of the database: ", type=str)
args=parser.parse_args()

oyo_url= "https://www.oyorooms.com/hotels-in-bangalore/?page="
MAX_page=args.page_num_max
scrapped_info_list=[]
connect(args.name)

for page in range(1,MAX_page):
    req==requests.get(oyo_url + str(page))
    soup = BeautifulSoup(content, "html.parser")
    hotel_list = soup.find_all("div", {"class": "hotelCardListing"})
    
    for hotel in hotel_list:
        hotel_dict={}
        hotel_dict["NAME"]=hotel.find("h3", {"class": "ListingHotelDescription"}).text
        hotel_dict["ADDRESS"]=hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["PRICE"]=hotel.find("span", {"class": "listingPrice__finalPrice"}).text
        scrapped_info_list.append(hotel_dict)
        insert_row(args.name, tuple(hotel_dict.values()))
        
        
dataFrame = pandas.DataFrame(scrapped_info_list)
dataFrame.to_csv("webscraping.csv")
get_info(args.name)
        
    
            
        
        
    