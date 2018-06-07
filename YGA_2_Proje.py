import urllib.request, json, pprint
from urllib.request import urlopen
from tabulate import tabulate
from prettytable import PrettyTable
import time
import os

with urllib.request.urlopen('http://www.crucoding.com/frame/data2.json') as url:
    data = json.loads(url.read().decode())
    url.close()
    

def Real_Time_Connection():
    time.sleep(0.5)
    with urllib.request.urlopen('http://www.crucoding.com/frame/data2.json') as url:
        global data
        data = json.loads(url.read().decode())
        url.close()


#with urllib.request.urlopen("http://crucoding.com/frame/data.json") as url:
 #   data = json.loads(url.read().decode())
  #  for key, value in data.items():
   #     pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(value)
ID_LIST = []
def normalConditions():
    time.sleep(1)
    if len(ID_LIST) == 4:
        del(ID_LIST[0])
    for key in data["Bus_#Int"]:
        pp = pprint.PrettyPrinter(indent = 2)
        pp.pprint(key)
    print("======================================================================")
    if data["Bus_#Int"][0]["Bus_#2_Intensity"] > data["Bus_#Int"][0]["Bus_#1_Intensity"] and data["Routes_Int"][0]["Route_#2_Intensity"] > data["Routes_Int"][0]["Route_#1_Intensity"]:#CHECK
            ID1 = 1
            ID_LIST.append(ID1)
            ID1_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print(data["Bus_#"][0]["Bus_#2"], ">", data["Bus_#"][0]["Bus_#1"])
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS2R"][0]["Light2_#S1"],"\nLight 2: ",data["TLDS1G"][0]["Light1_#S3"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#1_Intensity"] > data["Bus_#Int"][0]["Bus_#2_Intensity"] and data["Routes_Int"][0]["Route_#1_Intensity"] > data["Routes_Int"][0]["Route_#2_Intensity"]:#CHECK
            ID2 = 2
            ID_LIST.append(ID2)
            ID2_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1G"][0]["Light1_#S3"],"\nLight 2: ",data["TLDS2R"][0]["Light2_#S1"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#2_Intensity"] > data["Bus_#Int"][0]["Bus_#1_Intensity"] and data["Routes_Int"][0]["Route_#1_Intensity"] == data["Routes_Int"][0]["Route_#2_Intensity"]:#CHECK
            ID5 = 5
            ID_LIST.append(ID5)
            ID5_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1G"][0]["Light1_#S3"],"\nLight 2: ",data["TLDS2G"][0]["Light2_#S3"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#1_Intensity"] == data["Bus_#Int"][0]["Bus_#2_Intensity"] and data["Routes_Int"][0]["Route_#1_Intensity"] > data["Routes_Int"][0]["Route_#2_Intensity"]:#CHEKC
            ID6 = 6
            ID_LIST.append(ID6)
            ID6_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1G"][0]["Light1_#S3"],"\nLight 2: ",data["TLDS2R"][0]["Light2_#S1"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#1_Intensity"] == data["Bus_#Int"][0]["Bus_#2_Intensity"] and data["Routes_Int"][0]["Route_#2_Intensity"] > data["Routes_Int"][0]["Route_#1_Intensity"]:
            ID7 = 7
            ID_LIST.append(ID7)
            ID7_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1R"][0]["Light1_#S1"],"\nLight 2: ",data["TLDS1G"][0]["Light1_#S3"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#1"],"has same intensity with ",data["Bus_#"][0]["Bus_#2"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#1_Intensity"] > data["Bus_#Int"][0]["Bus_#2_Intensity"] and data["Routes_Int"][0]["Route_#2_Intensity"] == data["Routes_Int"][0]["Route_#1_Intensity"]:
            ID8 = 8
            ID8_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            ID_LIST.append(ID8)
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1G"][0]["Light1_#S3"],"\nLight 2: ",data["TLDS2R"][0]["Light2_#S1"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#1_Intensity"] > data["Bus_#Int"][0]["Bus_#2_Intensity"] and data["Routes_Int"][0]["Route_#2_Intensity"] > data["Routes_Int"][0]["Route_#1_Intensity"]:#CHECK
            ID9 = 9
            ID9_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            ID_LIST.append(ID9)
            print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            print(ID_LIST)
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#2_Intensity"] > data["Bus_#Int"][0]["Bus_#1_Intensity"] and data["Routes_Int"][0]["Route_#1_Intensity"] > data["Routes_Int"][0]["Route_#2_Intensity"]:#CHECK
            deltaPassIntensity = data["Bus_#Int"][0]["Bus_#2_Intensity"] - data["Bus_#Int"][0]["Bus_#1_Intensity"]
            deltaRouteIntensity = data["Routes_Int"][0]["Route_#1_Intensity"] - data["Routes_Int"][0]["Route_#2_Intensity"]
            print("this")
            if deltaPassIntensity > deltaRouteIntensity:
                ID10 = 10
                ID_LIST.append(ID10)
                ID10_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
                print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1R"][0]["Light1_#S1"],"\nLight 2: ",data["TLDS2G"][0]["Light2_#S3"])
                print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
                print(ID_LIST)
                Real_Time_Connection()
                normalConditions()
            elif deltaRouteIntensity > deltaPassIntensity:
                ID11 = 11
                ID_LIST.append(ID11)
                ID11_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
                print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1G"][0]["Light1_#S3"],"\nLight 2: ",data["TLDS2R"][0]["Light2_#S1"])
                print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
                print(ID_LIST)
                Real_Time_Connection()
                normalConditions()
            '''deltaPassIntensity = abs(data["Bus_#Int"][0]["Bus_#1_Intensity"] - data["Bus_#Int"][0]["Bus_#2_Intensity"])
            deltaRouteIntensity = abs(data["Routes_Int"][0]["Route_#2_Intensity"]) - int(data["Routes_Int"][0]["Route_#1_Intensity"])
            if deltaPassIntensity > deltaRouteIntensity:
                ID3 = 3
                ID_LIST.append(ID3)
                ID3_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
                print("\nResult: ",data["Bus_#"][0]["Bus_#1"]," passes.")
                print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1G"][0]["Light1_#S3"],"\nLight 2: ",data["TLDS2R"][0]["Light2_#S1"])
                print(ID_LIST)
                Real_Time_Connection()
                normalConditions()
            elif deltaRouteIntensity > deltaPassIntensity:
                ID4 = 4
                ID_LIST.append(ID4)
                ID4_1 = print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
                print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
                print("\nLight setups should be like: ","\nLight 1: ",data["TLDS2G"][0]["Light2_#S3"],"\nLight 2: ",data["TLDS1R"][0]["Light2_#S1"])
                print(ID_LIST)
                Real_Time_Connection()
                normalConditions() '''
    elif data["Bus_#Int"][0]["Bus_#1_Intensity"] == data["Bus_#Int"][0]["Bus_#2_Intensity"] and data["Routes_Int"][0]["Route_#2_Intensity"] == data["Routes_Int"][0]["Route_#1_Intensity"]:
            print("\nLight setups should be like: ","\nLight 1: ",data["TLDS1R"][0]["Light1_#S1"],"\nLight 2: ",data["TLDS1G"][0]["Light1_#S3"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#1"],"has same intensity with ",data["Bus_#"][0]["Bus_#2"])
            print("\nResult: ",data["Bus_#"][0]["Bus_#2"]," passes.")
            if ID_LIST[-1:] == 1:
                print(ID1_1)
            elif ID_LIST[-1:] == 2:
                print(ID2_1)
            elif ID_LIST[-1:] == 3:
                print(ID3_1)
            elif ID_LIST[-1:] == 4:
                print(ID4_1)
            elif ID_LIST[-1:] == 5:
                print(ID5_1)
            elif ID_LIST[-1:] == 6:
                print(ID6_1)
            elif ID_LIST[-1:] == 7:
                print(ID7_1)
            elif ID_LIST[-1:] == 8:
                print(ID8_1)
            elif ID_LIST[-1] == 9:
                print(ID9_1 )
            elif ID_LIST[-1:] == 10:
                print(ID10_1)
            elif ID_LIST[-1:] == 11:
                print(ID11_1)
            Real_Time_Connection()
            normalConditions()
normalConditions()

