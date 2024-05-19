import random
import numpy
from DictCreator import CreateDict
import requests
qwertyDict = CreateDict()

def OdlegloscHamminga(lista1, lista2):
    if type(lista1) is int:
        lista1 = str(lista1)

    if type(lista2) is int:
        lista2 = str(lista2)

    if len(lista1) != len(lista2):
        return "listy różnią się ilością elementów"
    odleglosc = 0
    for i in range(0, len(lista1)):
        if lista1[i] != lista2[i]:
            odleglosc += 1

    return odleglosc

def OdlegloscHammingaMod(lista1,lista2):

    if type(lista1) is int:
        lista1 = str(lista1)

    if type(lista2) is int:
        lista2 = str(lista2)

    if len(lista1) != len(lista2):
        return "listy różnią się ilością elementów"
    odleglosc = 0
    for i in range(0, len(lista1)):
        if lista1[i] != lista2[i]:
            if qwertyDict[lista1[i]].count(lista2[i]) > 0:
                odleglosc += 1
            else:
                odleglosc += 2

    return odleglosc

def CreateListOfRandomWords(amount):
    response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    wordList = response.content.split()
    outputList = numpy.random.choice(wordList, size = (1,amount)).tolist()[0]
    outputList = [[f"{len(byte.decode('utf-8'))}",byte.decode('utf-8')] for byte in outputList]
    return outputList

print(OdlegloscHammingaMod("mama","kawa"))
def OdlegloscHammingaMod2(wyraz):
    wordList = CreateListOfRandomWords(1000)
    Dict = {}
    for i in range(0,len(wordList)):
        keys = list(Dict.keys())
        if keys.count(wordList[i][0]) == 0:
            Dict[wordList[i][0]] = [wordList[i][1]]
        else:
            Dict[wordList[i][0]].append(wordList[i][1])

    if Dict[str(len(wyraz))].count(wyraz) > 0:
        return "OK"
    else:
        listOfWords = Dict[str(len(wyraz))]
        top3Words = [(OdlegloscHamminga(wyraz,wyrazZListy),wyrazZListy) for wyrazZListy in listOfWords]
        top3Words.sort()
        return top3Words[:3]
    return Dict



print("zadanie 1")
slowo1 = input("podaj pierwsze slowo: ")
slowo2 = input("podaj drugie slowo: ")
print(OdlegloscHamminga(slowo1, slowo2))

print()
print("zadanie 2")
slowo1 = input("podaj pierwsze slowo: ")
slowo2 = input("podaj drugie slowo: ")
print(OdlegloscHammingaMod(slowo1, slowo2))


print("zadanie 3")
slowo = input("podaj slowo: ")
print(OdlegloscHammingaMod2(slowo))