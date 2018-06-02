import urllib.request, json, pprint
from urllib.request import urlopen
from tabulate import tabulate
from prettytable import PrettyTable
import time


with urllib.request.urlopen('http://www.crucoding.com/frame/data.json') as url:
    data = json.loads(url.read().decode())
    url.close()
    


def Real_Time_Connection():
    time.sleep(0.5)
    with urllib.request.urlopen('http://www.crucoding.com/frame/data.json') as url:
        global data
        data = json.loads(url.read().decode())
        url.close()

#with urllib.request.urlopen("http://crucoding.com/frame/data.json") as url:
 #   data = json.loads(url.read().decode())
  #  for key, value in data.items():
   #     pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(value)


def normalConditions():
    bus_INT1_str = "Intensity of Bus_#1 is: {}".format(data["Bus_#Int"][0]["Bus_#1_Intesity"])
    bus_INT2_str = "Intensity of Bus_#2 is: {}".format(data["Bus_#Int"][0]["Bus_#2_Intesity"])
    bus_INT3_str = "Intensity of Bus_#3 is: {}".format(data["Bus_#Int"][0]["Bus_#3_Intesity"])
    bus_INT4_str = "Intensity of Bus_#4 is: {}".format(data["Bus_#Int"][0]["Bus_#4_Intesity"])
    print("This function has been set to give priority to the bus that has greatest intensity.")
    print("Intensity of Bus_#1 is: {}".format(data["Bus_#Int"][0]["Bus_#1_Intesity"]))
    print("Intensity of Bus_#2 is: {}".format(data["Bus_#Int"][0]["Bus_#2_Intesity"]))
    print("Intensity of Bus_#3 is: {}".format(data["Bus_#Int"][0]["Bus_#3_Intesity"]))
    print("Intensity of Bus_#4 is: {}".format(data["Bus_#Int"][0]["Bus_#4_Intesity"]))
    print("=======================================================================================")
    print("So if we sort the numbers from the biggest to lowest value, \nBus_#4 should pass first, \nThen Bus_#3, \nThen Bus_#2 and finally, \nBus_#1.")    
    if data["Bus_#Int"][0]["Bus_#4_Intesity"] > data["Bus_#Int"][0]["Bus_#3_Intesity"] and data["Bus_#Int"][0]["Bus_#2_Intesity"] and data["Bus_#Int"][0]["Bus_#1_Intesity"]:
        if data["Bus_#Int"][0]["Bus_#4_Intesity"] > data["Bus_#Int"][0]["Bus_#2_Intesity"] and data["Bus_#Int"][0]["Bus_#3_Intesity"] and data["Bus_#Int"][0]["Bus_#1_Intesity"]:
            print("{} should pass.".format(data["Bus_#"][0]["Bus_#4"]))
            print("Light setups should be like: " + "\nLight 1: " + data["TLDS1R"][0]["Light1_#S1"] + "\nLight 2: " + data["TLDS1R"][0]["Light1_#S1"] + "\nLight 3: " + data["TLDS1R"][0]["Light1_#S1"] + "\nLight 4: " + data["TLDS1R"][0]["Light1_#S1"])
            print("Result: " + data["Bus_#"][0]["Bus_#4"] + " passes.")
            Real_Time_Connection()
            normalConditions()
    elif data["Bus_#Int"][0]["Bus_#4_Intesity"] == data["Bus_#Int"][0]["Bus_#3_Intesity"]and data["Bus_#Int"][0]["Bus_#4_Intesity"] > data["Bus_#Int"][0]["Bus_#2_Intesity"] and data["Bus_#Int"][0]["Bus_#1_Intesity"]:
        print(data["Bus_#"][0]["Bus_#4"] + " has same intensty with " + data["Bus_#"][0]["Bus_#3"] + ". Route intensity has to be considered.") 
        Real_Time_Connection()
        normalConditions()
normalConditions()

