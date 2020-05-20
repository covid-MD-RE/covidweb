# Read file in
fi = open("04-21-2020.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

# loop through all rows in the csv file
provs = []
numdeaths = []
for line in datarows:
    templist = line.split(",")
    prov = templist[2].lower()
    country = templist[3].lower()
    confirmed = templist[7]
    deaths = templist[8]
    recover = templist[9]
    lat = templist[5]
    lon = templist[6]

    if (country == "us"):
        if (provs.count(prov) == 0):
            provs.append(prov)
            numdeaths.append(deaths)
        else:
            try:
                i = provs.index(prov)
                existing = int(numdeaths[i])
                numdeaths[i] = existing + int(deaths)
            except:
                print("can not find " + prov)
            
print(provs)
print(numdeaths)

import json

with open('us_states.geojson') as f:
  data = json.load(f)

f.close()

for prov in data["features"]:
    name = prov["properties"]["name"].lower()
    try:
        i = provs.index(name)
        prov["properties"]["deaths"] = numdeaths[i]
        #print(prov["properties"])
    except:
        print(name + " not found")
        prov["properties"]["deaths"] =0

with open('cloropleth2.geojson', 'w') as json_file:
  json.dump(data, json_file)

json_file.close()

