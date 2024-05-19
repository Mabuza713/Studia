import numpy as np


class EditingLength:
    ############## Knuth-Morris-Pratt algo
    def CPF(P):
        pi = [0]
        for j in range(1, len(P)):
            k = pi[j - 1]
            while k > 0 and P[k] != P[j]:
                k = pi[k - 1]
            pi.append(k + 1 if P[k] == P[j] else k)
        return pi

    def KMP(T, P):
        pi = EditingLength.CPF(P)
        counter, maximum = 0, 0
        j = 0
        for i in range(0, len(T)):
            while j > 0 and P[j] != T[i]:
                j = pi[j - 1]
            if P[j] == T[i]:
                j += 1
            if j == len(P):
                return j
        return False

    ###############################################################################
    def FindAllSubText(P):
        listOfWords = []
        for i in range(0, len(P)):
            for j in range(0, len(P)):
                wordToAppend = P[i:len(P) - j]
                if wordToAppend != "":
                    listOfWords.append(wordToAppend)
        listOfWords = list(set(listOfWords))
        return listOfWords

    def FindLongestSeries(T, P):
        listOfWords = EditingLength.FindAllSubText(P)
        longest = 0
        remembered = ""
        for word in listOfWords:
            current = EditingLength.KMP(T, word)
            if current == len(P):
                return current
            elif current > longest:
                longest = current
                remembered = word
        return longest, remembered


print(EditingLength.FindLongestSeries("konwalia", "zawalina"))


def FindSubset(P,T):
    amount = 0
    T = [char for char in T]
    listOfLetters = [char for char in P]
    for j in range(0,len(listOfLetters)):
        for i in range(0,len(T)):
            if T[i] == listOfLetters[j]:
                T[i] = T[i].upper()
                listOfLetters[j] = listOfLetters[j].upper()
                amount += 1
                break
    return "".join(T), "".join(listOfLetters), amount
print(FindSubset("apqbcrdsefa","tabucvdaewxfyz"))