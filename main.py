import pandas as pd
import json
import requests

'''1. Develop a simple web application that integrates with the following Megaventory entities using the Megaventory API:

a) Product

b) SupplierClient

c) InventoryLocation

d) Tax

e) Discount

f) SalesOrder
'''


def post_data(dict_data, url, headers):
    r = requests.request("POST", url, data=json.dumps(dict_data), headers=headers)  # simple API Post request


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  # defining the headers

product_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvProduct": {
        "ProductType": "TimeRestrictedService",
        "ProductSKU": "1112256",
        "ProductDescription": "Nike shoes",
        "ProductPurchasePrice": 44.99,
        "ProductSellingPrice": 99.99
    },
    "mvRecordAction": "Insert"
}

product_url = "https://api.megaventory.com/v2017a/Product/ProductUpdate"  # define the product url
post_data(product_data, product_url, headers)  # and posting!

client_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvSupplierClient": {
        "SupplierClientType": "Client",
        "SupplierClientName": "mbambis",
        "SupplierClientShippingAddress1": "Example 8, Athens",
        "SupplierClientPhone1": "3421614931",
        "SupplierClientEmail": "babis@exampletest.com "
    },
    "mvGrantPermissionsToAllUser": "true",
    "mvRecordAction": "Insert"
}

client_url = "https://api.megaventory.com/v2017a/SupplierClient/SupplierClientUpdate"  # ...also the url
post_data(client_data, client_url, headers)  # and of course, post it!
inventory_location_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvInventoryLocation": {
        "InventoryLocationName": "Test Project Location",
        "InventoryLocationAbbreviation": "Test",
        "InventoryLocationAddress": "Example 20, Athens"
    },
    "mvRecordAction": "Insert"
}

location_url = "https://api.megaventory.com/v2017a/InventoryLocation/InventoryLocationUpdate"  # once again, defining the specific URL in order to "contact" the API
post_data(inventory_location_data, location_url, headers)  # posting!
# tax data have to be defined
tax_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvTax": {
        "TaxName": "VAT-2",
        "TaxDescription": "VAT GR",
        "TaxValue": 24
    },
    "mvRecordAction": "Insert"
}

tax_url = "https://api.megaventory.com/v2017a/Tax/TaxUpdate"  # tax API/GET url definition
post_data(tax_data, tax_url, headers)

"""Discount - POST"""

# finally, following the same procedure for the discount entity
discount_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvDiscount": {

        "DiscountName": "Loyalty",
        "DiscountDescription": "Loyalty Customer Discount",
        "DiscountValue": 50
    },
    "mvRecordAction": "Insert"
}

discount_url = "https://api.megaventory.com/v2017a/Discount/DiscountUpdate"
post_data(discount_data, discount_url, headers)  # and posting it!


def get_data(url, params):
    req = requests.request("GET", url, json=params)  # a simple GET request to the API
    return req  # and of course return it


client_parameters = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "Filters": [
        {
            "FieldName": "SupplierClientType",
            "SearchOperator": "Equals",
            "SearchValue": "Client"
        },
        {
            "AndOr": "And",
            "FieldName": "SupplierClientName",
            "SearchOperator": "Contains",
            "SearchValue": "mbambis"
        }
    ]
}

client_url = "https://api.megaventory.com/v2017a/SupplierClient/SupplierClientGet"
req = get_data(client_url, client_parameters)  # fetching the data...

response = req.json()  # turning the response in a json file...
print('The response in JSON form looks like this:\n\n', response)  # let's print the response

client_id = response['mvSupplierClients'][0]['SupplierClientID']  # extracting the needed information

"""Inventory Location - GET"""

location_parameters = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "Filters": [
        {
            "FieldName": "InventoryLocationName",
            "SearchOperator": "Equals",
            "SearchValue": "Test Project Location"
        }
    ]
}

location_url = "https://api.megaventory.com/v2017a/InventoryLocation/InventoryLocationGet"
# location_req = requests.request("GET", url, json = location_parameters)
location_req = get_data(location_url, location_parameters)

location_response = location_req.json()
print('The response in JSON form looks like this:\n\n', location_response)

location_id = location_response['mvInventoryLocations'][0]['InventoryLocationID']


#Tax - GET


tax_parameters = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "Filters": [
        {
            "FieldName": "TaxName",
            "SearchOperator": "Equals",
            "SearchValue": "VAT-2"
        }
    ]
}

tax_url = "https://api.megaventory.com/v2017a/Tax/TaxGet"
# tax_req = requests.request("GET", url, json = tax_parameters)
tax_req = get_data(tax_url, tax_parameters)

tax_response = tax_req.json()
print('The response in JSON form looks like this:\n\n', tax_response)

tax_id = tax_response['mvTaxes'][0]['TaxID']

"""Discount - GET"""

discount_parameters = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    #   "Filters": [
    #     {
    #         "FieldName": "DiscountName",
    #         "SearchOperator": "Equals",
    #         "SearchValue": "Loyalty 2"
    #     }
    # ]
}

discount_url = "https://api.megaventory.com/v2017a/Discount/DiscountGet"
discount_req = requests.request("GET", discount_url, json=discount_parameters)
#discount_req = get_data(discount_url, discount_parameters)

discount_response = discount_req.json()
print('The response in JSON form looks like this:\n\n', discount_response)

discount_id = discount_response['mvDiscounts']
"""Last but not least, it is time to post the Sales Order data. I am following the API's documentation lead...
Sales Order - POST
"""

sales_order_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvSalesOrder": {
        "SalesOrderClientId": client_id,
        "SalesOrderTypeId": 3,
        "SalesOrderStatus": "Verified",
        "SalesOrderInventoryLocationID": location_id,
        "SalesOrderDetails": [
            {
                "SalesOrderRowProductSKU": "1112256-2",
                "SalesOrderRowQuantity": "10",
                "SalesOrderRowShippedQuantity": "1",
                "SalesOrderRowInvoicedQuantity": "1",
                "SalesOrderRowUnitPriceWithoutTaxOrDiscount": "99.99",
                "SalesOrderRowTaxID": tax_id,
                "SalesOrderRowDiscountID": discount_id
            }
        ]
    },
    "mvRecordAction": "Insert"
}

sales_order_url = "https://api.megaventory.com/v2017a/SalesOrder/SalesOrderUpdate"
post_data(sales_order_data, sales_order_url, headers)
