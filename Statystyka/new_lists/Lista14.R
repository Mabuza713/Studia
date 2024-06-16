#zadanie 1
dane <- read.csv2('C:\\Users\\mabuza\\Desktop\\mieszkania.csv')
dane$m2 <- dane$Cena / dane$Metraz
reglin <- lm(formula=m2~Metraz, data = dane)
summary(reglin)


dane$reszty <- dane$m2 - (7510.254 - 23.704 * dane$Metraz)
#punkt a
# psie pole to grupa referencyjna bo jest największa. Dlatego nie ma dla niego dzielP
# dodanie dzielnic i pieter
dane$dzielF <- ifelse(dane$Dzielnica == "Fabryczna", 1, 0)
dane$dzielK <- ifelse(dane$Dzielnica == "Krzyki", 1, 0)
dane$dzielS <- ifelse(dane$Dzielnica == "Srodmiescie", 1, 0)
dane$dzielM <- ifelse(dane$Dzielnica == "Stare Miasto", 1, 0)
dane$Pietro4 <- ifelse(dane$Pietro > 4, 1, 0)

reglin2 <- lm(formula=m2~Metraz+Pietro4+dzielF+dzielK+dzielS+dzielM, data = dane)
summary(reglin2)

# na dzielK kosztuje 396.23 więcej niż na psim polu. w starym mieście 1200 więcej niż na krzykach (1601 - 396 = 1200)
# dzielF nie jest istotna (nie ma *) (nie ma istotnych różnic między cenami na farbycznej i psim polu)

# wyrzucamy dzielF z mdoelu bo nie jest istotne
reglin2 <- lm(formula=m2~Metraz+Pietro4+dzielK+dzielS+dzielM, data = dane)
summary(reglin2)

#punkt b idk
model_step <- step(reglin2, direction = "backward")

#odczytujemy z summary estimatei od intercept dokonujemy dzialan
# bi
# x = 80, p4 = 1, k=s=m=0
7203 - 22.7*80 - 337.6 * 1

# bii
# x = 65, k = 1, p=s=m=0
7203 - 22.7 * 65 + 432.3


#reziduła
# Wyznaczenie reszt
reszty <- residuals(model_step)

# Test normalności reszt
shapiro.test(reszty)


reglin3 <- lm(formula=Cena~Metraz+Pietro4+dzielF+dzielK+dzielS+dzielM, data = dane)
summary(reglin3)

reglin3 <- lm(formula=Cena~Metraz+Pietro4+dzielK+dzielS+dzielM, data = dane)
summary(reglin3)

# b
# 57780.1 + 4791.6*x - 18444.7 * p +24010.5*k + 18521.3*s + 77373.6*m
# bi
57780.1 + 4791.6*80 - 18444.7
# bii
57780.1 + 4791.6*65 + 24010.5


# a
bakteria <- dane <- read.csv2('C:\\Users\\mabuza\\Desktop\\Bakteria.csv')
plot(bakteria$czas, bakteria$masa)

# b
reglinB <- lm(formula= masa~czas, data = bakteria)
summary(reglinB)

# c
bakteria$logarytm <- log(bakteria$masa)
reglinB2 <- lm(formula<- logarytm~czas, data = bakteria)
