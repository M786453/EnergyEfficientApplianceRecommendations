from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def home_view(request):

    return render(request, 'home.html')

def products_view(request):

    if request.method == "POST":
        appliance = request.POST.get('appliance')
        budget = request.POST.get('budget')
        products = requests.get(f'https://shoumi-eear.hf.space/?appliance={appliance}&budget={budget}')
        products = json.loads(products.text)[0]
    
        new_products = []
        for prod in products:
            details = prod.split("\n")
            products_dict = {}
            for d in details:
                key = d.split(":")[0]
                value = d.split(":")[-1].strip()
                if key == "Description":
                    value = value[:100]
                if key == "Voltage":
                    value = value.split("v")[0]
                products_dict[key] = value
            
            if appliance.lower() in products_dict["Name"].lower():
                new_products.append(products_dict)
        
        return render(request, 'products.html', context={'products' :new_products})
    else:
        return redirect('home')