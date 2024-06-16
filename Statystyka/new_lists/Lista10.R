#zadanie 1
#punkt a

n <- 1000
h0 <- 0.4
ile_ludzi <- 385
proporcja = ile_ludzi/n

SE <- sqrt(proporcja * (1 - proporcja)/n)
t = (proporcja - h0)/SE
p =  2 * (1 - pnorm(abs(t)))
#poniewaz p > 0.05 nie odrzucamy

#punk b
ile_m <- 480
ile_k <-520

prop_m = 165/480
prop_k = 220/520

SE = sqrt(prop_m * (1 - prop_m)/ile_m + prop_k*(1- prop_k)/ile_k)
t = (prop_m - prop_k)/SE
p = 2 * (1 - pnorm(abs(t)))
# odrzucamy p na poziomie 0.05

prop.test(x = c(165, 220), n = c(480, 520))

# punkt c
mean_k <- 166
sd_k <- 10
ile_k <- 520


mean_m <- 174
sd_m <- 11
ile_m <- 480

SE <- sqrt(sd_m/ile_m + sd_k/ile_k)
Z = (mean_m - mean_k)/SE
p = 2 * (1 - pnorm(abs(Z)))
#p ~ okolo 0 wiec < 0.05 wiec odrzucamy

#zadanie 2
dane <- read.csv2('C:\\Users\\mabuza\\Desktop\\dane1.csv')
n = nrow(dane)

h0 = 0.5 #proporcja kobiet wsrod studentow

ile_k = nrow(dane[dane$plec == "1", ])
ile_m = n - ile_k

prop_m = ile_m/n
prop_k = ile_k/n

SE = sqrt(h0*(1 - h0)/ n)
z = (prop_k - h0)/SE
p = 2 * (1 - pnorm(abs(z))) 

# nie odrzucamy bo p > alfa 

prop.test(ile_k, n, p= 0.5)


#zadanie 3

srednia_dane_po_k = mean(dane[dane$plec == "1", "Waga_po"])
srednia_dane_po_m = mean(dane[dane$plec == "0", "Waga_po"])

wariacja_k = sd(dane[dane$plec == "1", "Waga_po"])^2
wariacja_m = sd(dane[dane$plec == "0", "Waga_po"])^2

SE = sqrt(wariacja_k/ile_k + wariacja_m/ile_m)

Z =  (srednia_dane_po_k - srednia_dane_po_m)/SE
p = 2 * (1 - pnorm(abs(Z)))
t.test(dane[dane$plec == "1", "Waga_po"], dane[dane$plec == "0", "Waga_po"], paired = FALSE)

#odrzycamy bo p < 0.05

#zadanie 4
dane_po_k = dane[dane$plec == "1", ]
dane_po_m = dane[dane$plec == "0", ]


dane_po_k_70 = dane_po_k[dane_po_k$dane_po > 70, "Waga_po"]
dane_po_m_70 = dane_po_m[dane_po_m$dane_po > 70, "Waga_po"]



srednia_dane_po_k_70 = mean(dane_po_k[dane_po_k$dane_po > 70, "Waga_po"])
srednia_dane_po_m_70 = mean(dane_po_m[dane_po_m$dane_po > 70, "Waga_po"])
ile_k = length(dane_po_k_70)
ile_m = length(dane_po_m_70)

prop_k = ile_k / nrow(dane_po_k)
prop_m = ile_m / nrow(dane_po_m)

SE = sqrt(prop_k * (1 - prop_k) / nrow(dane_po_k) + prop_m * (1 - prop_m) / nrow(dane_po_m))

t = (prop_k - prop_m) / SE
p <- 2 * (1 - pnorm(abs(t)))
# p mneijsze od 0.05 wiec odrzucamy

#zadanie 5


k = 5
sredni_mezczyzna = mean(dane[dane$plec==0, "Wzrost"])
srednia_kobieta = mean(dane[dane$plec==1, "Wzrost"])
wariancja_mezczyzna = sd(dane[dane$plec==0, "Wzrost"])^2
wariancja_kobieta = sd(dane[dane$plec==1, "Wzrost"])^2
kobiety = sum(dane[dane$plec==1, "plec"])
mezczyzni = nrow(dane) - kobiety

SE = sqrt(wariancja_mezczyzna/mezczyzni + wariancja_kobieta/kobiety)
Z = ((sredni_mezczyzna - srednia_kobieta) - k ) / SE
p = 2 * (1 - pnorm(abs(Z)))
p



#zadanei 6

# h0 = 80% studentów przybiera na wadze w trakcie studiów
h0 = 0.8
wzrost_wagi = dane["Waga_po"] - dane["Waga_przed"]
n = nrow(dane)
przytyl = wzrost_wagi>0
przytyl = sum(przytyl)
prop.test(przytyl, n, p=0.8)

SE = sqrt(h0 * (1 - h0) / n)
prop = przytyl / n
t = (prop - h0) / SE

z = 2 * (1 - pnorm(abs(t)))
# p = 0.053 więc h0 jest na granicy bycia odrzuconą dla punktu istotnosci 0.05 mamy podstawy do odrzucenia