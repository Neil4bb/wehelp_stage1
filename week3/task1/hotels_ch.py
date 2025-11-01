import urllib.request, json

url_ch = " https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"

with urllib.request.urlopen(url_ch) as response:
        data_ch = json.load(response)

hotels = data_ch if isinstance(data_ch, list) else data_ch["list"]

print(len(hotels))

#print(json.dumps(hotels[:3], ensure_ascii = False, indent=2))

sample = hotels[0]
print(sample.keys())
        

     