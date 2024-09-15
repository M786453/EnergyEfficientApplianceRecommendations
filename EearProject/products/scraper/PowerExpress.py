import requests
from bs4 import BeautifulSoup
import json
import django
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lowerparts.settings')

# # Initialize Django
django.setup()

from products.models import Appliance

class Scraper:

    def __init__(self):
        
        self.BASE_URL = "https://powerhouseexpress.com.pk"

    def scrape_product(self, product_url):

        product_dict = {"name": "", "description": "", "url": "", "image": "", "price": "", "availability": "", "power": "", "voltage": ""}

        try:
            
            response = requests.get(url=product_url)

            soup = BeautifulSoup(response.text, 'html.parser')

            raw_product_details = json.loads(soup.find_all('script', {'type': 'application/ld+json'})[-1].text)

            if "name" in raw_product_details:
                product_dict["name"] = raw_product_details["name"]

            if "description" in raw_product_details:
                product_dict["description"] = raw_product_details["description"]

            if "url" in raw_product_details:
                product_dict["url"] = raw_product_details["url"]

            if "image" in raw_product_details:
                product_dict["image"] = raw_product_details["image"][0]

            if "offers" in raw_product_details:

                if "price" in raw_product_details["offers"][0]:
                    product_dict["price"] = raw_product_details["offers"][0]["price"]

                if "availability" in raw_product_details["offers"][0]:
                    product_dict["availability"] = "In Stock" if raw_product_details["offers"][0]["availability"].endswith('InStock') else "Out of Stock"

            # Product Specification

            product_specifications = soup.find('table', {'class': 'product-spec'})

            specification_labels = [element.text.strip() for element in product_specifications.find_all('td', {'class': 'left'})]

            specification_values = [element.text.strip() for element in product_specifications.find_all('td', {'class': 'right'})]

            for index in range(len(specification_labels)):

                label = specification_labels[index]
                
                if 'power' in label or 'wattage' in label:

                    product_dict["power"] = specification_values[index]

                if "voltage" in label:

                    product_dict["voltage"] = specification_values[index]

        except Exception as e:

            print("Error @ scrape_product():", e)
        
        if product_dict["power"]:
            return product_dict
        else:
            return None
        
    def scrape_electrical_appliances(self):

        page_no = 1

        while True:

            try:

                print("Page#", page_no)
        
                ELECTRICAL_APPLIANCES_ENDPOINT = f"https://powerhouseexpress.com.pk/collections/electrical-appliances?page={page_no}"

                response = requests.get(ELECTRICAL_APPLIANCES_ENDPOINT)

                soup = BeautifulSoup(response.text, 'html.parser')

                products_links = soup.find_all('h3', {'class': 'pbm-title'})

                for product_lnk in products_links:

                    product_lnk = product_lnk.find('a').get('href')

                    product_data =self.scrape_product(product_url=self.BASE_URL + product_lnk)

                    if product_data:

                        Appliance(**product_data).save()

                        time.sleep(5)

                page_no += 1

            except Exception as e:

                print("Error @ scrape_electrical_appliances():", e)