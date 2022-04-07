class Server:

    def __init__(self,name, type, cpu, ram, network, price):
        self.type = type
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.network = network
        self.price = price

    def inizialize_list(list_of_server):
        list_of_server.append(Server("c6g.medium","Compute", 1, 2, 10000, 0.034))
        list_of_server.append(Server("c5.large","Compute", 2, 4, 10000, 0.085))
        list_of_server.append(Server("c4.2xlarge","Compute", 8, 15, 1000, 0.398))
        list_of_server.append(Server("c6gd.4xlarge","Compute", 16, 32, 10000, 0.6144))
        list_of_server.append(Server("c5d.12xlarge","Compute", 48, 96, 25000, 2.304))
        list_of_server.append(Server("c5d.xlarge","Compute", 4, 8, 10000, 0.192))
        list_of_server.append(Server("c6i.large","Compute", 2, 4, 125000, 0.085))
        list_of_server.append(Server("c5n.large","Compute", 2, 5.25, 25000, 0.108))
        list_of_server.append(Server("t2.micro","General", 1, 1, 65, 0.0116))
        list_of_server.append(Server("m4.10xlarge","General", 40, 160, 10000, 2))
        list_of_server.append(Server("a1.medium","General", 1, 2, 10000, 0.0255))
        list_of_server.append(Server("a1.metal","General", 16, 32, 10000, 0.408))
        list_of_server.append(Server("t4g.medium","General", 2, 4, 5000, 0.0336))
        list_of_server.append(Server("t4g.xlarge","General", 4, 16, 5000, 0.1344))
        list_of_server.append(Server("m6g.medium","General", 1, 4, 10000, 0.0375))
        list_of_server.append(Server("m5.2xlarge","General", 8, 32, 10000, 0.384))
        return list_of_server

    def Sort(self,category,direction,list = []):
        # 1 bigger to smaller // 2 smaller to bigger
        if(category == "cpu"):
            list.sort(key=lambda x: x.cpu)
        elif(category == "ram"):
            list.sort(key=lambda x: x.ram)
        elif (category == "net"):
            list.sort(key=lambda x: x.network)
        elif (category == "price"):
            list.sort(key=lambda x: x.price)
        if(direction == 2):
            list.reverse()

    def FindByName(list,name):
        for one in list:
            if one.name == name:
                return one