# importing libraries
import csv
from bs4 import BeautifulSoup
import requests

jumiaurl='https://www.jumia.co.ke/'

 
def get_categories(URL):
    # opening our output file in append mode
    File = open("categories.csv", "a")
 
    # specifying user agent, You can use other user agents
    # available on the internet
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
 
    # Making the HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
 
    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
 
    # retrieving categories
    categoryDict={}
    categories=soup.findAll("a",attrs={"class":'itm',"role": 'menuitem'})
    sub_categories=soup.findAll("a", attrs={"class":'tit', "role":'menuitem'})
    for category in categories: 
        try:
            category_value= category.span.string
            # Category as a string value
            category_string = category_value.strip().replace(',', '')

            sub_categoriesdict={}
            for sub_category in sub_categories:
                try:
                    sub_category_value=sub_categories.string
                    sub_category_string = sub_category_value.strip().replace(',', '')
                except AttributeError:
                    sub_category_string="NA"
                categoryDict[category_string]=sub_categoriesdict[sub_category_string]
                
                  
                                

        except AttributeError:
            category_string = "NA"
           
        
        


        print(categoryDict)
    
        # saving the category in the file
        # File.write(f"{category_string},")

        # closing the file
    File.close()

get_categories(jumiaurl)