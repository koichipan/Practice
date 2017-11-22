# import os
import json
# import urllib
import webbrowser
# from PIL import Image
# from pprint import pprint

""" This is parse home page "Gallery Wall" group's script"""

json_data = open('template.json').read()
template_data = json.loads(json_data)
i = 1

with open('result.html', 'w') as myFile:
    for key in template_data['data']['recommend'][0]['data']:
        for subkey in key:
            # print template_data['data']['recommend'][0]['data'][0][1]['pid']
            # print (subkey['pid'])
            myFile.write('<img src="' + str(subkey['thumbnail']["small"]) + '" width="8%">')

            if (i % 10 == 0):
                myFile.write('<BR>')

            i = i + 1
            # myFile.write('PID = ' + str(subkey['pid']) + '<blockquote></blockquote>')

# Open File
page = "file:///Users/koichipan/Practice/Charles_python_tool/result.html"
webbrowser.open(page)

# Practice
# webbrowser.open("http://s1.store.cmcm.com/small/pg/20170413/7819535743424921601704246907.jpg")
# webbrowser.open("http://s1.store.cmcm.com/small/pg/20170412/7547372304967925761304197312.jpg")

# write data
""" myurl = "http://s1.store.cmcm.com/small/pg/20170413/7819535743424921601704246907.jpg"
with open('result.html', 'w') as myFile:
    myFile.write('<img src="' + myurl + '">')
myFile.close() """

print("Test done")
