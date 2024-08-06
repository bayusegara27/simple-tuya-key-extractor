import xml.etree.ElementTree as ET
import json

def json_to_dict(json_str):
    return json.loads(json_str.replace('&quot;', '"').replace('&amp;', '&'))

tree = ET.parse('file.xml')
root = tree.getroot()

s_home_data = root.find(".//string[@name='s_home_data172959811']")

with open('output.txt', 'w') as file:
    if s_home_data is not None:
        json_text = s_home_data.text

        data_dict = json_to_dict(json_text)

        device_list = data_dict.get('deviceRespBeen', [])
        for device in device_list:
            device_id = device.get('devId', 'Not Found')
            local_key = device.get('localKey', 'Not Found')
            file.write(f"Device ID: {device_id}\n")
            file.write(f"Local Key: {local_key}\n")
    else:
        print("Element 's_home_data172959811' was not found in the XML file.")
