import collections

import boto3
import pprint
import Servers
import GetInfo
from datetime import datetime



def statsByTimeStamp():
    serverPerTimeStamp = {}
    i = 0
    for element in avgNetwork.keys():
        list = []
        list.append(avgCpu.get(element))
        list.append(maxCpu.get(element))
        list.append(avgRAM.get(element))
        list.append(maxRAM.get(element))
        list.append(avgNetwork.get(element))
        list.append(networkBandwidthMax.get(element))
        list.append(element)
        serverPerTimeStamp[i] = list
        i += 1
    return serverPerTimeStamp


def remove(idanMap):  ##problem with the input
    for i in range(17):
        k, v = idanMap.popitem(0)
        i += 1


def findHigherInstance(cpu, timestamp, type):
    list_of_prices = []
    list_of_prices = Servers.Server.inizialize_list(list_of_prices)
    Servers.Server.Sort(Servers.Server, "price", 1, list_of_prices)
    for service in list_of_prices:
        if service.ram > Servers.Server.FindByName(list_of_prices, type).ram:
            print('At ', timestamp, ' Needed a larger instance.')
            print('New instance name: ', service.name)
            print('New pricing is ', service.price, ' per hour')
            break


def check_cpu_danger_zone(idanMap, ts, previous, typeins):
    # we'll check two time zones -> if the first time zone is 80% and the one after is higher w
    if idanMap.get(ts)[1] >= 90:
        findHigherInstance(idanMap.get(ts)[1], idanMap.get(ts)[6], typeins)
        return False
    if idanMap.get(ts)[1] > 80 and previous == False:
        return True
    if idanMap.get(ts)[1] < 80:
        return False
    if idanMap.get(ts)[1] > 85 and previous == True:
        findHigherInstance(idanMap.get(ts)[1], idanMap.get(ts)[6], typeins)
        return False


def underPreformingInstance(idanMap, ts, timeToRun):
    while timeToRun:
        if idanMap.get(ts)[1] > 50:
            return False
        timeToRun -= 1
    return True


def optimizeInstance(idanMap, type):  # checks if we use it less
    for key in range(0, len(idanMap) - 6):
        if underPreformingInstance(idanMap, key, 4):
            if underPreformingInstance(idanMap, key + 4, 2):
                findLowerInstance(idanMap.get(key)[1], idanMap.get(key)[6], type)


def findLowerInstance(cpu, timeStamp, type):
    list_of_prices = []
    list_of_prices = Servers.Server.inizialize_list(list_of_prices)
    Servers.Server.Sort(Servers.Server, "price", 2, list_of_prices)
    for service in list_of_prices:
        if service.ram < Servers.Server.FindByName(list_of_prices, type).ram:
            print('At ', timeStamp, ' found we can decrease to a smaller instance')
            print('New instance name: ', service.name)
            print('New pricing is ', service.price, ' per hour')
            print('We have saved ', Servers.Server.FindByName(list_of_prices, type).price - service.price, 'per hour')
            break


maxCpu = GetInfo.getCpuUtilizationMax()
maxCpu = collections.OrderedDict(sorted(maxCpu.items()))
remove(maxCpu)
avgCpu = GetInfo.getCpuUtilizationAverages()
avgCpu = collections.OrderedDict(sorted(avgCpu.items()))
remove(avgCpu)

maxRAM = GetInfo.maxMemUtilizationDict
maxRAM = collections.OrderedDict(sorted(maxRAM.items()))

avgRAM = GetInfo.getMemUtilizationAverages()
avgRAM = collections.OrderedDict(sorted(avgRAM.items()))

networkBandwidthMax = GetInfo.getNetworkUtilizationMax()
networkBandwidthMax = collections.OrderedDict(sorted(networkBandwidthMax.items()))
remove(networkBandwidthMax)

avgNetwork = GetInfo.getNetworkUtilizationAverages()
avgNetwork = collections.OrderedDict(sorted(avgNetwork.items()))
remove(avgNetwork)

serverPerTimeStamp = statsByTimeStamp()
insType = GetInfo.getInsType()
previous = False
for key in serverPerTimeStamp:
    previous = check_cpu_danger_zone(serverPerTimeStamp, key, previous, insType)
optimizeInstance(serverPerTimeStamp, insType)

# checks if the instance's storage runs on GP2 or GP3- changes to GP3 if not
GetInfo.checkIfGP2()
