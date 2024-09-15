import os
import django
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EearProject.settings')

# # Initialize Django
django.setup()

from products.models import Appliance

products = []

for product in Appliance.objects.all():

    products.append(f"Name: {product.name}\nDescription: {product.description}\nUrl: {product.url}\nImage: {product.image}\nPrice: {product.price}\nAvailability: {product.availability}\nPower: {product.power}\nVoltage: {product.voltage}")

with open('products.json', 'w') as f:

    f.write(json.dumps(products))