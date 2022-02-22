# ---------------------------------------------
# import package to read json
# ---------------------------------------------
import json


# ---------------------------------------------
#  write function to load file and parse json
# ---------------------------------------------

def readJson(file):
    with open(file) as p:
        return json.load(p)

# ---------------------------------------------
#  call 'readJson', load salaries
# ---------------------------------------------

salaries = readJson('/Users/arielattias/Desktop/Dropbox/MIT/Classes/1.001/read-parse-validate/01_read_json/data.json')
print(salaries)

# ---------------------------------------------
#  print all salaries
# ---------------------------------------------

for salary in salaries['data']:
    print(salary[18])
# ---------------------------------------------
# loop through list, only print salary field
# ---------------------------------------------


# ---------------------------------------------
#  add all salaries
# ---------------------------------------------