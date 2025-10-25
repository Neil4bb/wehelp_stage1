貝吉塔 = { "cara":"貝吉塔", "x": -4, "y":- 1, "z": 0 }; # 貝吉塔
辛巴 = { "cara":"辛巴", "x": -3, "y": 3, "z": 0 }; # 辛巴
丁滿 = { "cara":"丁滿", "x": -1, "y": 4, "z": 1 }; # 丁滿 
悟空 = { "cara":"悟空", "x": 0, "y": 0, "z": 0 }; # 悟空
特南克斯 = { "cara":"特南克斯", "x": 1, "y": -2, "z": 0 }; # 特南克斯
弗利沙 = { "cara":"弗利沙", "x": 4, "y": -1, "z": 1 }; 

list = [貝吉塔, 辛巴, 丁滿, 悟空, 特南克斯, 弗利沙]

map = {
   "貝吉塔": 貝吉塔,
    "辛巴": 辛巴,
    "丁滿": 丁滿,
    "悟空": 悟空,
    "特南克斯": 特南克斯,
    "弗利沙": 弗利沙
    }


def func1(name): 
 # your code here 
    target = map.get(name)
    a = target["x"]
    b = target["y"]
    c = target["z"]
    n = ""; f = ""
    min = float('inf'); max = 0

    for i in range(6):
        dis = abs(list[i]["x"]-a) + abs(list[i]["y"]-b)

        if c!= list[i]["z"]:
          dis += 2

        if dis == 0 :
            continue
        elif dis > max:
            max = dis
            f = list[i]["cara"]
        elif dis == max:
            f += "、"+list[i]["cara"]

        if dis < min:
            min = dis
            n = list[i]["cara"]
        elif dis == min:
            n += "、"+ list[i]["cara"]

    print ("最遠" + f + ";最近" + n)
         
 
 
func1("辛巴")  # print 最遠弗利沙；最近丁滿、⾙吉塔
 
func1("悟空")  # print 最遠丁滿、弗利沙；最近特南克斯
 
func1("弗利沙")  # print 最遠辛巴，最近特南克斯
 
func1("特南克斯")  # print 最遠丁滿，最近悟空


print("------------task 2------------")

# your code here, maybe 
import re #引入re模組 以便使用正則表達式

bookings = {"S1": [], "S2": [], "S3": []}

def isAvailable(service, start, end):
    for b in bookings[service]:
        if ( not (end <= b["start"] or start >= b["end"])):
            return False
    return True



def func2(ss, start, end, criteria): 
# your code here 

    if "name" in criteria:
        splits = criteria.split("=")
    else:
        splits = re.split(r'(>=|<=)',criteria) #r'' 避免python把反斜線 \ 當成跳脫字元（escape character）


    if splits[0] == "name":

        flag = False

        for i in range(3):
            if (services[i]["name"]==splits[1] and isAvailable(services[i]["name"], start, end) ):
                bookings[services[i]["name"]].append({"start": start, "end": end})
                print(services[i]["name"])
                flag = True
                break

        if not flag:
            print("Sorry")

    elif splits[0] == "r":  #r的情況

        ava = None; gap = float('inf')

        if splits[1] == "<=":  #<=的情況
            for i in range(3):
                if (services[i]["r"] <= float(splits[2]) and abs(services[i]["r"] - float(splits[2])) < gap):
                    if isAvailable(services[i]["name"], start, end):
                        ava = services[i]["name"]
                        gap = abs(services[i]["r"] - float(splits[2]))

        else: #>=的情況
            for i in range(3):
                if (services[i]["r"] >= float(splits[2]) and abs(services[i]["r"] - float(splits[2])) < gap):
                    if isAvailable(services[i]["name"], start, end):
                        ava = services[i]["name"]
                        gap = abs(services[i]["r"] - float(splits[2]))

        if ava == None:
            print("Sorry")
        else:
            bookings[ava].append({"start": start, "end": end})
            print(ava)

    else: #c的情況

        ava = None; gap = float('inf')

        if splits[1] == "<=":  #<=的情況
            for i in range(3):
                if (services[i]["c"] <= float(splits[2]) and abs(services[i]["c"] - float(splits[2])) < gap):
                    if isAvailable(services[i]["name"], start, end):
                        ava = services[i]["name"]
                        gap = abs(services[i]["c"] - float(splits[2]))

        else: #>=的情況
            for i in range(3):
                if (services[i]["c"] >= float(splits[2]) and abs(services[i]["c"] - float(splits[2])) < gap):
                    if isAvailable(services[i]["name"], start, end):
                        ava = services[i]["name"]
                        gap = abs(services[i]["c"] - float(splits[2]))

        if ava == None:
            print("Sorry")
        else:
            bookings[ava].append({"start": start, "end": end})
            print(ava)
            




services=[ 
{"name":"S1", "r":4.5, "c":1000}, 
{"name":"S2", "r":3, "c":1200}, 
{"name":"S3", "r":3.8, "c":800} 
] 
func2(services, 15, 17, "c>=800")  # S3 
func2(services, 11, 13, "r<=4")  # S3 
func2(services, 10, 12, "name=S3")  # Sorry 
func2(services, 15, 18, "r>=4.5")  # S1 
func2(services, 16, 18, "r>=4")  # Sorry 
func2(services, 13, 17, "name=S1")  # Sorry 
func2(services, 8, 9, "c<=1500")  # S2 
func2(services, 8, 9, "c<=1500")  # S1 新增條件




print("------------task 3------------")

import math

def func3(index): 
 # your code here 
    rem = index % 4
    result = index / 4
    quo = math.floor(result)
    num = None

    if rem == 0:
        num = (-2)*quo + 25
    elif rem == 1:
        num = (-2)*quo + 23
    elif rem == 2:
        num = (-2)*quo + 20
    else:
        num = (-2)*quo + 21

    print(num)


func3(1)  # print 23 
func3(5)  # print 21 
func3(10)  # print 16 
func3(30)  # print 6


print("------------task 4------------")

def func4(sp, stat, n): 
 # your code here 
    car = None; gap = float('inf')

    for i in range(len(sp)):
        if not float(stat[i]):
            if (abs(sp[i]-n) < gap):
                gap = abs(sp[i]-n)
                car = i
    
    print(car)

 
func4([3, 1, 5, 4, 3, 2], "101000", 2)  # print 5 
func4([1, 0, 5, 1, 3], "10100", 4)  # print 4 
func4([4, 6, 5, 8], "1000", 4)  # print 2