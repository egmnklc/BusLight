import urllib.request, json, pprint
from urllib.request import urlopen
from tabulate import tabulate
from prettytable import PrettyTable
import time


with urllib.request.urlopen('http://www.crucoding.com/frame/data.json') as url:
    data = json.loads(url.read().decode())
    url.close()
    
bus_STR1 = data["Bus_#"][0]["Bus_#1"]
bus_STR2 = data["Bus_#"][0]["Bus_#2"]
bus_STR3 = data["Bus_#"][0]["Bus_#3"]
bus_STR4 = data["Bus_#"][0]["Bus_#4"]

bus_INT1 = data["Bus_#Int"][0]["Bus_#1_Intesity"]
bus_INT2 = data["Bus_#Int"][0]["Bus_#2_Intesity"]
bus_INT3 = data["Bus_#Int"][0]["Bus_#3_Intesity"]
bus_INT4 = data["Bus_#Int"][0]["Bus_#4_Intesity"]

bus_INT1_INT = int(bus_INT1)
bus_INT2_INT = int(bus_INT2)
bus_INT3_INT = int(bus_INT3)
bus_INT4_INT = int(bus_INT4)

bus_STR_R1 = data["Routes"][0]["Route_#1"]
bus_STR_R2 = data["Routes"][0]["Route_#2"]
bus_STR_R3 = data["Routes"][0]["Route_#3"]
bus_STR_R4 = data["Routes"][0]["Route_#4"]

bus_STR_RINT1 = data["Routes_Int"][0]["Route_#1_Intensity"]
bus_STR_RINT2 = data["Routes_Int"][0]["Route_#2_Intensity"]
bus_STR_RINT3 = data["Routes_Int"][0]["Route_#3_Intensity"]
bus_STR_RINT4 = data["Routes_Int"][0]["Route_#4_Intensity"]


light1_STR1 = data["TLDS1R"][0]["Light1_#S1"]
light1_STR2 = data["TLDS1Y"][0]["Light1_#S2"]
light1_STR3 = data["TLDS1G"][0]["Light1_#S3"]

light2_STR1 = data["TLDS2R"][0]["Light2_#S1"]
light2_STR2 = data["TLDS2Y"][0]["Light2_#S2"]
light2_STR3 = data["TLDS2G"][0]["Light2_#S3"]

light3_STR1 = data["TLDS3R"][0]["Light3_#S1"]
light3_STR2 = data["TLDS3Y"][0]["Light3_#S2"]
light3_STR3 = data["TLDS3G"][0]["Light3_#S3"]

light4_STR1 = data["TLDS4R"][0]["Light4_#S1"]
light4_STR2 = data["TLDS4Y"][0]["Light4_#S2"]
light4_STR3 = data["TLDS4G"][0]["Light4_#S3"]



def Real_Time_Connection():
    time.sleep(0.5)
    with urllib.request.urlopen('http://www.crucoding.com/frame/data.json') as url:
        global data
        data = json.loads(url.read().decode())
        url.close()


def normalConditions():
    l = [bus_INT4_INT, bus_INT3_INT, bus_INT1_INT, bus_INT2_INT]
    bus_INT1_str = "Intensity of Bus_#1 is: {}".format(data["Bus_#Int"][0]["Bus_#1_Intesity"])
    bus_INT2_str = "Intensity of Bus_#2 is: {}".format(data["Bus_#Int"][0]["Bus_#2_Intesity"])
    bus_INT3_str = "Intensity of Bus_#3 is: {}".format(data["Bus_#Int"][0]["Bus_#3_Intesity"])
    bus_INT4_str = "Intensity of Bus_#4 is: {}".format(data["Bus_#Int"][0]["Bus_#4_Intesity"])
    print("This function has been set to give priority to the bus that has greatest intensity.")
    print("Intensity of Bus_#1 is: {}".format(data["Bus_#Int"][0]["Bus_#1_Intesity"]))
    print("Intensity of Bus_#2 is: {}".format(data["Bus_#Int"][0]["Bus_#2_Intesity"]))
    print("Intensity of Bus_#3 is: {}".format(data["Bus_#Int"][0]["Bus_#3_Intesity"]))
    print("Intensity of Bus_#4 is: {}".format(data["Bus_#Int"][0]["Bus_#4_Intesity"]))
    print("When the integers are compared, it's obvious that {} > {} > {} > {}".format(l[3],l[2],l[1],l[0]))
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

