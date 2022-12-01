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


# create a post function
def post_data(dict_data, url, headers):
    r = requests.request("POST", url, data=json.dumps(dict_data), headers=headers)  # request


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  # header
# product_data json
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
# URL path of the product
product_url = "https://api.megaventory.com/v2017a/Product/ProductUpdate"
# post function
post_data(product_data, product_url, headers)  # and posting!
# client json data
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
# url
client_url = "https://api.megaventory.com/v2017a/SupplierClient/SupplierClientUpdate"
# post it
post_data(client_data, client_url, headers)
# same
inventory_location_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvInventoryLocation": {
        "InventoryLocationName": "Test Project Location",
        "InventoryLocationAbbreviation": "Test",
        "InventoryLocationAddress": "Example 20, Athens"
    },
    "mvRecordAction": "Insert"
}
# same as before, for location
location_url = "https://api.megaventory.com/v2017a/InventoryLocation/InventoryLocationUpdate"
post_data(inventory_location_data, location_url, headers)
# tax json data
tax_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvTax": {
        "TaxName": "VAT-2",
        "TaxDescription": "VAT GR",
        "TaxValue": 24
    },
    "mvRecordAction": "Insert"
}
# api path
tax_url = "https://api.megaventory.com/v2017a/Tax/TaxUpdate"
# post location
post_data(tax_data, tax_url, headers)

# discount json object
discount_data = {
    "APIKEY": "f7b3a5e056ed17d6@m137302",
    "mvDiscount": {

        "DiscountName": "Loyalty",
        "DiscountDescription": "Loyalty Customer Discount",
        "DiscountValue": 50
    },
    "mvRecordAction": "Insert"
}
# discount url
discount_url = "https://api.megaventory.com/v2017a/Discount/DiscountUpdate"
# post it
post_data(discount_data, discount_url, headers)


# get method function
def get_data(url, params):
    req = requests.request("GET", url, json=params)
    return req


# client data request
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
req = get_data(client_url, client_parameters)  # get the client data

response = req.json()  # json response

client_id = response['mvSupplierClients'][0]['SupplierClientID']  # try to extract informations

# location get data

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

location_req = get_data(location_url, location_parameters)

location_response = location_req.json()  # location response

location_id = location_response['mvInventoryLocations'][0]['InventoryLocationID']  # extract informations

# tax requesta data


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
tax_req = get_data(tax_url, tax_parameters)

tax_response = tax_req.json()  # tax.tojson

tax_id = tax_response['mvTaxes'][0]['TaxID']

# discount get json

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

discount_response = discount_req.json()

discount_id = discount_response['mvDiscounts']

# create a general order with data obtained
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
post_data(sales_order_data, sales_order_url, headers)  # posting the order data to the API path
