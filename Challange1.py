import json
MyJSONfile = open('ENTERYOURPATH.json','r')
jsondata=MyJSONfile.read()
obj=json.loads(jsondata)
list=obj
for i in range(len(list)):
    print(list[i].get("model"))
    


