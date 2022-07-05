import sys
import csv
import json
import os.path

def dict_append(data, key, value):
    keys = key.split('/')
    
    i=0
    for key in keys:
            
        if key.isnumeric():
            
            if not type(data[keys[i-1]]) == list:
                data[keys[i-1]]=[]
            data=data[keys[i-1]]
            i+=1
            continue
        
        if type(data) == list:

            if len(data)-1<int(keys[i-1]):
                data.append({})
            
            if key not in data[int(keys[i-1])]:    
                data[int(keys[i-1])][key]={}
                if i==len(keys)-1:
                    data[int(keys[i-1])][key]=value
                    break
            data=data[int(keys[i-1])][key]
            i+=1
            continue
                
            
        
        if not key in data:    
            data[key] = {}
        
        if i==len(keys)-1:
            data[key]=value

        if not (i+1<=len(keys)-1 and keys[i+1].isnumeric()):
            data=data[key]
        
        i+=1
        
        
        
fileName= sys.argv[1]
path=  (sys.argv[2]+r"\\") if len(sys.argv)>=3 else ""

with open(fileName, 'r') as f:
    
    ans = {}
    
    f_reader = csv.reader(f)
    
    try:
        for i in f_reader:
            key = i[0].strip()
            value = i[1].strip()
            dict_append(ans, key, value)
        with open(r"{}{}.json".format(path,ans['compatible_device_type']), 'w') as f1:
            f1.write(json.dumps(ans, indent=1))
                
    except Exception as e:
        print(e)
        
        

