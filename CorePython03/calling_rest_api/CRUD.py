import sys
import requests # pip install requests
import json

url = "http://127.0.0.1:8000/customers/"

def insert_record(record):
    try:
        response = requests.post(url, json=record)
        # print(response.status_code)
        if response.status_code==201:
            print("Insert record successfully")
        else:
            print("Error to insert record")
    except:
        print("Error: ", sys.exc_info()[1])

def get_all():
    records = None
    try:
        response = requests.get(url)
        if response.status_code==200:
            records = json.loads(response.content)
    except:
        print("Error: ", sys.exc_info()[1])
    finally:
        return records

def get(pid):
    record = None
    try:
        # http://127.0.0.1:8000/customers/5/
        response = requests.get(url+str(pid))
        if response.status_code == 200:
            record = json.loads(response.content)
    except:
        print("Error: ", sys.exc_info()[1])
    finally:
        return record


def update_record(record):
    tmp_url = url+str(record['id'])+"/"
    response = requests.put(tmp_url, json=record)
    if response.status_code == 200:
        return True
    else:
        return False


def delete_record(pid):
    tmp_url = url + str(pid) + "/"
    response = requests.delete(tmp_url)
    if response.status_code == 204:
        return True
    else:
        return False

# Test

# Insert Record
"""
id = int(input("Enter id : "))
fullname = input("Enter name : ")
caddress  = input("Enter address : ")
record = {'id':id, 'fullname':fullname, 'address':caddress}
insert_record(record)
"""

# Retrieve Record
# records = get_all()
# print(records)

# Record Search
# record = get(9)
# print(record)

# Record Edit
# record = {'id':1, 'fullname':'Roshan', 'address':'BHK'}
# print(update_record(record))

# Record Delete
# print(delete_record(9))
