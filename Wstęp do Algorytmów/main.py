import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.drawing.nx_pydot import write_dot
import graphviz
from networkx.drawing.nx_agraph import graphviz_layout
from IPython.display import display_png
from math import *


class Node:
    def __init__(self, x, y, connections, data):
        self.x = x
        self.y = y
        self.data = data
        self.connections = []


class Graph:
    def MakeAConnection(self, Node1, Node2):
        Node1.connections.append(Node2)
        Node2.connections.append(Node1)
        Node1.connections = list(set(Node1.connections))
        Node2.connections = list(set(Node2.connections))

    def CreateGraph(self, nodeAmount, maxAmountOfConnections):
        xmax, ymax = 0, 0
        valuesX = [x for x in range(0, nodeAmount)];
        valuesY = [x for x in range(0, nodeAmount)]

        nodeArray = []
        for i in range(0, nodeAmount):
            xval = random.choice(valuesX);
            if xval > xmax: xmax = xval

            yval = random.choice(valuesY)
            if yval > ymax: ymax = yval

            valuesX.remove(xval);
            valuesY.remove(yval)
            newNode = Node(xval, yval, [], i)
            nodeArray.append(newNode)

        for node1 in nodeArray:
            listOfRandomNodes = random.choices(nodeArray, k=random.randint(0, nodeAmount))
            while len(listOfRandomNodes) > maxAmountOfConnections:
                listOfRandomNodes.pop()
            for node2 in listOfRandomNodes:
                Graph.MakeAConnection(self, node1, node2)

        return nodeArray

    def Visualize(self, array):
        G = nx.Graph()
        points = []
        for node in array:
            G.add_node(node.data, pos=(node.x, node.y))
            points.append((node.x, node.y))
        for node1 in array:
            conections = node1.connections
            for node2 in conections:
                x1, y1 = node1.x, node1.y
                x2, y2 = node2.x, node2.y
                weight = int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

                G.add_weighted_edges_from([(node1.data, node2.data, weight)])
        plt.figure(figsize=(20, 20))
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G, pos, with_labels=True)

        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def RemoveConnection(self, array, node1, node2):
        found1 = None; found2 = None
        for node in array:
            if node.data == int(node1):
                found1 = node
            elif node.data == int(node2):
                found2 = node
        if found1 is None or found2 is None:
            return "podano zle nody"
        else:
            rememb1 = -1
            rememb2 = -1
            for i in range(0, len(found1.connections)):
                if found1.connections[i].data == found2.data:
                    rememb1 = i
            for i in range(0,len(found2.connections)):
                if found2.connections[i].data == found1.data:
                    rememb2 = i
            if rememb2 == -1 or rememb1 == -1:
                return "cos poszlo nie tak"
            else:
                found1.connections.pop(rememb1)
                found2.connections.pop(rememb2)
                return

    def DeleteWhileNotInterupted(self, array):
        HowManyDel = 0
        node1 = input(f"{HowManyDel}. Podaj pierwszy: ")
        node2 = input(f"{HowManyDel}. Podaj drugi: ")
        while node1 != "" or node2 != "":
            Graph.RemoveConnection(self=None, array=array, node1=int(node1), node2=int(node2))
            Graph.Visualize(self=None, array=array)
            HowManyDel += 1
            node1 = int(input(f"{HowManyDel}. Podaj pierwszy: "))
            node2 = int(input(f"{HowManyDel}. Podaj drugi: "))


array = Graph.CreateGraph(self=None, nodeAmount=5, maxAmountOfConnections=10)cd
Graph.Visualize(self=None, array=array)
node1 = int(input("podaj pierwszy: "))
node2 = int(input("podaj drugi: "))
Graph.RemoveConnection(self=None, array=array, node1=node1, node2=node2)
Graph.Visualize(self=None, array=array)
Graph.DeleteWhileNotInterupted(self= None,array = array)