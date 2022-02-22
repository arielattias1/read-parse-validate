# -------------------------------------
# import package to read json
# import package to walk file system
# -------------------------------------
from asyncore import read
import json 
import glob

# -----------------------------------
#  list all files
# -----------------------------------

data = []

pattern = '/Users/arielattias/Desktop/Dropbox/MIT/Classes/1.001/read-parse-validate/01_read_json/data/*/*.json'
for file in glob.glob(pattern):
    data.append(file)

print(data)
# -----------------------------------
#  loop through files, parse json
# ---------------------------------

def readJson(file):
    with open(file) as p: 
        return json.load(p)

for file in data: 
    banana = readJson(file)
    print(banana)