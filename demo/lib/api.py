import requests

URL = 'http://localhost:5000/api/contacts'

def fetch_contacts():
    ''' Call to API of contacts '''
    req = requests.get(URL)
    data = req.json()
    # for data in req.json():
    #     print(data, 1)
    return data

def fetch_contact(id):
    '''Call to api for specific contact'''
    req = requests.get(URL + f'/{id}')
    data = req.json()
    # for data in req.json():
    #     print(data, 1)
    return data

def delete_contact(id):
    requests.delete(URL + f'/{id}')
    
def fetch_add_contact(contact):
    req = requests.post(URL, json = contact)
