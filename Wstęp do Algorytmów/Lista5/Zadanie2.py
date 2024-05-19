import random
import matplotlib.pyplot as plt
import requests


def LetterCounterPercentage(string):
    dict = {}
    string = [char for char in string.strip()]
    suma = 0
    for n in string:
        if ord(n) >= 65 and ord(n) <= 90:
            n = n.lower()


        if ord(n) >= 97 and ord(n) <= 122:
            if n in dict.keys():
                dict[n] += 1
                suma += 1
            else:
                dict[n] = 1
                suma += 1
    for key in dict.keys():
        dict[key] = dict[key] / suma * 100
    return dict
def LetterCounterPercentageVowel(string):
    dict = {}
    string = [char for char in string.strip()]
    suma = 0
    vowel = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
    for n in string:
        if ord(n) >= 65 and ord(n) <= 90:
            n = n.lower()


        if ord(n) >= 97 and ord(n) <= 122 and vowel.count(n) > 0:
            if n in dict.keys():
                dict[n] += 1
                suma += 1
            else:
                dict[n] = 1
                suma += 1
    for key in dict.keys():
        dict[key] = dict[key] / suma * 100
    return dict
def StoryAll():
    responsENG = requests.get("https://gutenberg.net.au/ebooks01/0100021.txt"); decodedENG = responsENG.content.decode("utf-8")
    responsePL = requests.get("https://ii.uni.wroc.pl/~jmi/Dydaktyka/2010-linux/1984/1984.txt"); decodedPL = responsePL.content.decode("ISO 8859-2").replace("š", "a").replace("", "s").replace("ó","o").replace("ż","z").replace("ź", "z").replace("ł","l").replace("ń","n")
    responseDE = requests.get("https://archive.org/stream/Gorwellbeutew1/orwellbeutewelt1combi_djvu.txt"); decodedDE = responseDE.content.decode("utf-8")

    dictENG = LetterCounterPercentage(decodedENG)
    dictPL = LetterCounterPercentage(decodedPL)
    dictDE = LetterCounterPercentage(decodedDE)
    return [(dictENG, "English"), (dictPL,"Polish"), (dictDE,"Deutch")]
def StoryVowels():
    responsENG = requests.get("https://gutenberg.net.au/ebooks01/0100021.txt"); decodedENG = responsENG.content.decode("utf-8")
    responsePL = requests.get("https://ii.uni.wroc.pl/~jmi/Dydaktyka/2010-linux/1984/1984.txt"); decodedPL = responsePL.content.decode("ISO 8859-2").replace("š", "a").replace("", "s").replace("ó","o").replace("ż","z").replace("ź", "z").replace("ł","l").replace("ń","n")
    responseDE = requests.get("https://archive.org/stream/Gorwellbeutew1/orwellbeutewelt1combi_djvu.txt"); decodedDE = responseDE.content.decode("utf-8")

    dictENG = LetterCounterPercentageVowel(decodedENG)
    dictPL = LetterCounterPercentageVowel(decodedPL)
    dictDE = LetterCounterPercentageVowel(decodedDE)
    return [(dictENG, "English"), (dictPL,"Polish"), (dictDE,"Deutch")]
def CreatePlot(lista):
    result = lista
    fig, axs = plt.subplots(1,len(lista), figsize = (20,10))
    for k,i in enumerate(result):
        dictionary = dict(sorted(i[0].items()))
        axs[k].bar(dictionary.keys(), dictionary.values(),color = f"C{k + 1}")

        axs[k].set_title(i[1])
        axs[k].set_xlabel("Letters")
        axs[k].set_ylabel("Percentages")

        print(f"Check if percentages add up to 100: {sum(dictionary.values())} for {i[1]}")
        print()

        for i,value in enumerate(dictionary.values()):
            axs[k].text(i, value, f'{value:.1f}%', ha='center', va='bottom')
    plt.show()

def RandomSnippetOfText(length):
    StefanZeromskiSyzyfowePracePL = requests.get("https://wolnelektury.pl/media/book/txt/syzyfowe-prace.txt"); SyzyfowePracePL = StefanZeromskiSyzyfowePracePL.content.decode("utf-8").replace("š", "a").replace("", "s").replace("ó","o").replace("ż","z").replace("ź", "z").replace("ł","l").replace("ń","n").replace("ś",'s').replace("ą","a").replace("ę","e").replace("ć","c")
    HenrykSiekiewiczKrzyzacyPL = requests.get("https://wolnelektury.pl/media/book/txt/krzyzacy-tom-pierwszy.txt"); KrzyzacyPL = HenrykSiekiewiczKrzyzacyPL.content.decode("utf-8").replace("š", "a").replace("", "s").replace("ó","o").replace("ż","z").replace("ź", "z").replace("ł","l").replace("ń","n").replace("ś",'s').replace("ą","a").replace("ę","e").replace("ć","c")
    FranzKafkaTheTrialENG = requests.get("https://www.csd.uwo.ca/~oveksler/Courses/Winter2009/CS2210b/A4/KafkaTrial.txt"); TheTrialENG = FranzKafkaTheTrialENG.content.decode("ISO-8859-1")
    HermanMelvilleMobyDickENG = requests.get("https://conan.iwr.uni-heidelberg.de/data/teaching/ipk_ws2020/moby-dick.txt"); MobyDickENG = HermanMelvilleMobyDickENG.content.decode("utf-8")
    JakobWassermannCasparHauseroderDieTrägheitdesHerzensDE = requests.get("https://www.gutenberg.org/files/25721/25721-8.txt"); HerzensDE = JakobWassermannCasparHauseroderDieTrägheitdesHerzensDE.content.decode("ISO-8859-1")
    ksiazki = [SyzyfowePracePL, KrzyzacyPL, TheTrialENG, MobyDickENG, HerzensDE]

    randomBook = random.choice(ksiazki)
    randomNumber = random.randint(0, len(randomBook))
    while randomNumber + length >= len(randomBook):
        randomNumber = random.randint(0, len(randomBook))

    return randomBook[randomNumber:randomNumber + length]



def FindLanguage(tekst):
    checkedDict = LetterCounterPercentage(tekst)
    books = StoryAll()
    listOfDifferences = []
    for book in books:
        keys = checkedDict.keys()
        sumForBook = 0
        for key in keys:
            if list(book[0].keys()).count(key) > 0:
                sumForBook += abs(book[0][key] - checkedDict[key])
            else:
                sumForBook += checkedDict[key]
        listOfDifferences.append((sumForBook,book[1]))
    listOfDifferences.sort()
    dictIndex = {"English": 0,
                 "Polish": 1,
                 "Deutch": 2}
    predictedLanguage = listOfDifferences[0][1]
    CreatePlot([(checkedDict,predictedLanguage+ " data from input"),(books[dictIndex[predictedLanguage]][0],books[dictIndex[predictedLanguage]][1]+ " data from control set")])
    print(tekst)
def FindLanguageVowel(tekst):
    checkedDict = LetterCounterPercentageVowel(tekst)
    books = StoryVowels()
    listOfDifferences = []
    for book in books:
        keys = checkedDict.keys()
        sumForBook = 0
        for key in keys:
            if list(book[0].keys()).count(key) > 0:
                sumForBook += abs(book[0][key] - checkedDict[key])
            else:
                sumForBook += checkedDict[key]
        listOfDifferences.append((sumForBook,book[1]))
    listOfDifferences.sort()
    dictIndex = {"English": 0,
                 "Polish": 1,
                 "Deutch": 2}
    predictedLanguage = listOfDifferences[0][1]
    CreatePlot([(checkedDict,predictedLanguage+ " data from input vowels only"),(books[dictIndex[predictedLanguage]][0],books[dictIndex[predictedLanguage]][1]+ " data from control set vowels only")])
    print(tekst)
print("zadanie 1")
CreatePlot(StoryAll())

print("zadanie 2")
FindLanguage(RandomSnippetOfText(10000))
print("zadanie 3")
FindLanguageVowel(RandomSnippetOfText(10000))



