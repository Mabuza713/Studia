def CreateDict():
    qwertyDict = {}
    listOfRows1 = []
    listOfRows2 = []
    listOfRows3= []
    row0 = "               "
    listOfRows1.append(row0)
    listOfRows2.append(row0)
    row1 = " `1234567890-=  "
    listOfRows1.append(row1);
    row1v2 = " ~!@#$%^&*()_+ "
    listOfRows2.append(row1v2)
    row2 = "  qwertyuiop[]  "
    listOfRows1.append(row2)
    row2v2 = "  QWERTYUIOP{}  "
    listOfRows2.append(row2v2)
    row3 = "  asdfghjkl;'   "
    listOfRows1.append(row3)
    row3v2 = "  ASDFGHJKL:\"   "
    listOfRows2.append(row3v2)
    row4 = "  zxcvbnm,./    "
    listOfRows1.append(row4)
    row4v2 = "  ZXCVBNM<>?    "
    listOfRows2.append(row4v2)
    row5 = "               "
    row1v3 = " `1234567890-=  "
    row2v3 = "  qwęrty€ióp[] "
    row3v3 = "  ąśdfghjkł;'   "
    row4v3 = "  żźćvbńm,./    "

    listOfRows3.append(row0)
    listOfRows3.append(row1v3)
    listOfRows3.append(row2v3)
    listOfRows3.append(row3v3)
    listOfRows3.append(row4v3)

    listOfRows3.append(row5)
    listOfRows1.append(row5)
    listOfRows2.append(row5)

    for i in range(1, len(listOfRows1) - 1):
        for j in range(1, len(listOfRows1[i]) - 1):
            if listOfRows1[i][j] != " ":
                listToAppend = []
                if listOfRows1[i][j - 1] != " ":
                    listToAppend.append(listOfRows1[i][j - 1])
                if listOfRows1[i][j + 1] != " ":
                    listToAppend.append(listOfRows1[i][j + 1])
                if listOfRows1[i + 1][j] != " ":
                    listToAppend.append(listOfRows1[i + 1][j])
                if listOfRows1[i - 1][j] != " ":
                    listToAppend.append(listOfRows1[i - 1][j])
                if listOfRows1[i - 1][j - 1] != " ":
                    listToAppend.append(listOfRows1[i - 1][j - 1])
                if listOfRows1[i - 1][j + 1] != " ":
                    listToAppend.append(listOfRows1[i - 1][j + 1])
                if listOfRows1[i + 1][j + 1] != " ":
                    listToAppend.append(listOfRows1[i + 1][j + 1])
                if listOfRows1[i + 1][j - 1] != " ":
                    listToAppend.append(listOfRows1[i + 1][j - 1])


            if listOfRows2[i][j] != " ":
                listToAppend2 = []
                if listOfRows2[i][j - 1] != " ":
                    listToAppend2.append(listOfRows2[i][j - 1])
                if listOfRows2[i][j + 1] != " ":
                    listToAppend2.append(listOfRows2[i][j + 1])
                if listOfRows2[i + 1][j] != " ":
                    listToAppend2.append(listOfRows2[i + 1][j])
                if listOfRows2[i - 1][j] != " ":
                    listToAppend2.append(listOfRows2[i - 1][j])
                if listOfRows2[i - 1][j - 1] != " ":
                    listToAppend2.append(listOfRows2[i - 1][j - 1])
                if listOfRows2[i - 1][j + 1] != " ":
                    listToAppend2.append(listOfRows2[i - 1][j + 1])
                if listOfRows2[i + 1][j + 1] != " ":
                    listToAppend2.append(listOfRows2[i + 1][j + 1])
                if listOfRows2[i + 1][j - 1] != " ":
                    listToAppend2.append(listOfRows2[i + 1][j - 1])

            if listOfRows3[i][j] != " ":
                listToAppend3 = []
                if listOfRows3[i][j - 1] != " ":
                    listToAppend3.append(listOfRows3[i][j - 1])
                if listOfRows3[i][j + 1] != " ":
                    listToAppend3.append(listOfRows3[i][j + 1])
                if listOfRows3[i + 1][j] != " ":
                    listToAppend3.append(listOfRows3[i + 1][j])
                if listOfRows3[i - 1][j] != " ":
                    listToAppend3.append(listOfRows3[i - 1][j])
                if listOfRows3[i - 1][j - 1] != " ":
                    listToAppend3.append(listOfRows3[i - 1][j - 1])
                if listOfRows3[i - 1][j + 1] != " ":
                    listToAppend3.append(listOfRows3[i - 1][j + 1])
                if listOfRows3[i + 1][j + 1] != " ":
                    listToAppend3.append(listOfRows3[i + 1][j + 1])
                if listOfRows3[i + 1][j - 1] != " ":
                    listToAppend3.append(listOfRows3[i + 1][j - 1])
            finalList = []
            for k in range(0,len(listToAppend)):
                finalList.append(listToAppend[k])
                finalList.append(listToAppend2[k])
                finalList.append(listToAppend3[k])
            finalList = list(set(finalList))
            finalList.sort()
            qwertyDict[listOfRows1[i][j]] = finalList
            qwertyDict[listOfRows2[i][j]] = finalList
            qwertyDict[listOfRows3[i][j]] = finalList
    return qwertyDict

