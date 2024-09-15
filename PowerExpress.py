import requests
from bs4 import BeautifulSoup
import json

class Scraper:

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

# print(Scraper().scrape_product('https://powerhouseexpress.com.pk/products/total-random-tf2041506-rotary-sander'))
print(Scraper().scrape_product('https://powerhouseexpress.com.pk/products/decakila-kejb002w-stand-blender'))