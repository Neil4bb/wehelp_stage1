import urllib.request, json

url_en = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

with urllib.request.urlopen(url_en) as response:
        data = json.load(response)

hotels = data if isinstance(data, list) else data["list"]
if isinstance(hotels, list):
        print("list表單是一個list")
else:
        print("list其實是個dict")

#print(len(hotels))

#print(json.dumps(hotels[:3], ensure_ascii = False, indent=2))

#sample = hotels[0]
#print(sample.keys())
        
