import glob
import json

# -----------------------------------
#  validate json
# -----------------------------------

def removeQuotes(string):
    pass

def validate(salary):
    try:
        key = salary["sid"] 
        key = salary["id"] 
        key = salary["position"]  
        key = salary["created_at"]  
        key = salary["created_meta"]  
        key = salary["updated_at"] 
        key = salary["updated_meta"] 
        key = salary["meta"] 
        key = salary["name"]  
        key = salary["title"]  
        key = salary["department_name"] 
        key = salary["regular"] 
        key = salary["retro"] 
        key = salary["other"] 
        key = salary["overtime"]  
        key = salary["injured"]  
        key = salary["detail"]  
        key = salary["quinn"]  
        key = salary["total_earnings"] 
        key = salary["zip"]
    except Exception as e: 
        return False
    return True 
# -----------------------------------
#  parse json function
# -----------------------------------

def readJson(file):
    with open(file) as p: 
        return json.load(p)

# -----------------------------------
#  loop through files, parse json
# ---------------------------------



pattern = '/Users/arielattias/Desktop/Dropbox/MIT/Classes/1.001/read-parse-validate/01_read_json/data/*/*.json'
data = []

for file in glob.glob(pattern):
    data.append(file)


for file in data: 
    salaries = readJson(file)

for salary in salaries: 
    print('file:', file, '-validation', validate(salary))
