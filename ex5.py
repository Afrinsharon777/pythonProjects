import json
with (open("ex5.json","r") as f):
  data = json.load(f)

for donut in data:
    if donut ["name"] == "Old Fashioned":
        donut["batters"]["batter"].append({"id":"1003","type":"tea"})
        break

with open("ex5.json","w") as f:
    json.dump(data,f,indent=4)