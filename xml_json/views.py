import json

from django.shortcuts import render,redirect
import xml.etree.ElementTree as ET
import xmltodict
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES["document"]
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        tree = ET.parse(fs.path(uploaded_file.name))
        xml_data = tree.getroot()
        xmlstr = ET.tostring(xml_data,encoding="utf-8",method="xml")
        data_dict = dict(xmltodict.parse(xmlstr))
        customers = data_dict["Root"]["Customers"]["Customer"]
        orders = data_dict["Root"]["Orders"]["Order"]
        #print(json.dumps(data_dict,indent=2))
        #print(data_dict["Root"]["Customers"])
        context = {
            "customers":customers,
            "orders":orders,
        }

        return render("xml_json/tables.html",context)
    return render(request,"xml_json/upload.html",context)
