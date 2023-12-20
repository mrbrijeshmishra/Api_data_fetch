from django.shortcuts import render
import urllib.request
from urllib.error import URLError
from django.contrib import messages
import json


def home(request):
    source = urllib.request.urlopen("http://local.easyfreightlook.com/api/v1/all/invoice/details").read()
    data_list = json.loads(source)
    # print(source)
    # print("\n")
    # print(data_list)
    # data = {
    #         "id": str(data_list[0]["id"]),
    #         "company_Name": str(data_list[0]["bill_to"]["party_name"]),
    # }
    # data = {}
    # for i in range(5):
    #     # Use assignment (=) for variable assignment
    #     id_value = str(data_list[i]["id"])
    #     company_name_value = str(data_list[i]["bill_to"]["party_name"])

    #     # Use the variables to assign values to dictionary keys
    #     data[i] = {"id": id_value, "company_Name": company_name_value}
    # # print(data)

    table_data = [{'id': entry['id'],'party_name': entry['bill_to']['party_name']} for entry in data_list]

    # table_data = []
    # for entry in data_list:
    #     row = {'id': entry['id'], 'party_name': entry['bill_to']['party_name']}
    #     table_data.append(row)

    return render(request,"index.html",{'table_data': table_data})