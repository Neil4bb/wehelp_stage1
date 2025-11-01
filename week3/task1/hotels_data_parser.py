import urllib.request, json, csv

url_ch = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"

with urllib.request.urlopen(url_ch) as response_ch:
    data_ch = json.load(response_ch)
    hotels_ch = data_ch["list"]

url_en = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
    
with urllib.request.urlopen(url_en) as response_en:    
    data_en = json.load(response_en)
    hotels_en = data_en["list"]
    
print(data_ch.keys())

def safe_int (x, default= 0): #取整數值
     try:
          return int(str(x).strip())
     except:
          return default
     
def infer_district(y):
    start = y.find("市") + 1
    end = y.find("區") + 1
    result = y[start:end]
    return result

def normalize_ch(item):
        return {
                "_id": item.get("_id"),
                "name_ch": item.get("旅宿名稱","").strip(),
                "addr_ch": item.get("地址","").strip(),
                "phone": item.get("電話或手機號碼","").strip(),
                "rooms": safe_int(item.get("房間數",0)),
                "district": infer_district(item.get("地址","").strip()),
        }

def normalize_en(item):
        return {
                "_id": item.get("_id"),
                "name_en": item.get("hotel name","").strip(),
                "addr_en": item.get("adress","").strip()
        }

merged = []

#for ch_item, en_item in zip (hotels_ch, hotels_en):
#      ch = normalize_ch(ch_item)
#      en = normalize_en(en_item)
#      merged.append({**ch,**en})

en_by_id = {item["_id"]: normalize_en(item) for item in hotels_en}

for ch_item in hotels_ch:
    ch = normalize_ch(ch_item)
    en = en_by_id.get(ch["_id"], {})
    merged.append({**ch, **en})


#print(merged[:3])

with open("hotels.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name_ch", "name_en", "addr_ch", "addr_en", "phone", "rooms"],
        #fieldnames是欄位清單，決定輸出的key，也決定排列順序
        extrasaction="ignore",  # 忽略 dict 中多餘的鍵，避免報錯
        restval="" #缺值時補空字串
    )
    writer.writeheader()
    writer.writerows(merged)


stats = {}

for item in merged:
    district = item.get("district", "")
    rooms = item.get("rooms", 0)

    if district not in stats:
        stats[district] = {"count": 0, "rooms": 0}

    stats[district]["count"] += 1
    stats[district]["rooms"] += rooms

#print(stats)


with open("district.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["district", "count", "rooms"])
    writer.writeheader()
    for district, data in stats.items():  #用.items()同時取 key 和 value
        writer.writerow({
            "district": district,
            "count": data["count"],
            "rooms": data["rooms"]
        })
