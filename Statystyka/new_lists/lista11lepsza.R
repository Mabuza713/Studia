#zadanie 1
frekwencja = c(171, 200, 168, 213, 226, 222)
rzuty = data.frame(Wynik = c(1, 2, 3, 4, 5, 6),
                   Frekwencja = frekwencja)

# h0 = kostka jest symetyczna
#wyznaczamy oczekiwana frekwencje
oczekiwana_frekwencja = sum(frekwencja) / 6
oczekiwane_rzuty = data.frame(Wynik = c(1, 2, 3, 4, 5, 6),
                              Oczekiwana_frekwencja = oczekiwana_frekwencja)

chi_kwadrat = sum((frekwencja - oczekiwana_frekwencja)^2/oczekiwana_frekwencja)

#sprawdzenie hipotezy
p =  1 - pchisq(chi_kwadrat, 6 - 1)

#inny sposob sprawdzenia
chisq.test(frekwencja)


#zadanie 2

n = 2
m = 2
wyksztalcenie = matrix(c(200, 300, 150, 350), nrow = n, byrow = TRUE)

#tworze tabele oczekiwanych wartosci przy zalozeniu iz nie sa powiazane suma wierza i i suma kolumny j pomnozona
oczekiwane = matrix(0, nrow = n, ncol = m)
for (i in 1:n) {
  for (j in 1:n) {
    oczekiwane[i, j] = (rowSums(wyksztalcenie)[i] * colSums(wyksztalcenie)[j]) /
      sum(wyksztalcenie)
  }
}

chi_kw <- sum((oczekiwane - wyksztalcenie)^2 / oczekiwane)
p <- 1 - pchisq(chi_kw, (m - 1) * (n - 1))
chi_kw_test <- chisq.test(wyksztalcenie)
fisher.test(wyksztalcenie) # dokladny test

#odrzucamy bo mniejsze niz alfa

#zadanie 3
dane <- read.csv2("/home/maciek/Desktop/mieszkania.csv")
tabela_rozdzielcza = table(dane$Dzielnica, dane$Pokoje)

dane$DuzoPokoi = ifelse(dane$Pokoje >= 4, 4, dane$Pokoje)
tabela_rozdzielcza = table(dane$Dzielnica, dane$DuzoPokoi)
chisq.test(tabela_rozdzielcza)
# p-value = 0.001728 < 0.05 wiec odrzucamy

#zadanie 4
dane$cenam2 = dane$Cena / dane$Metraz
dane$Drogie = ifelse(dane$cenam2 > 6000, TRUE, FALSE)

# test
tabela_rodzielcza = table(dane$Dzielnica, dane$Drogie)
chisq.test(tabela_rodzielcza)
#p-val okolo 0 wiec odrzucamy

#zadanie 5
shapiro.test(dane$cenam2)
plot(density(dane$cenam2), main = "Estymator gęstości [CENA / M2]", xlab = "[CENA / M2]", ylab = "Wartość")

srodmiesice = dane[dane$Dzielnica == "Srodmiescie", ]
shapiro.test(srodmiesice$Metraz)
plot(density(srodmiesice$Metraz), main = "Estymator gęstości [CENA / M2]", xlab = "[CENA / M2]", ylab = "Wartość")

#zadanie 6
#punkt a1
rozklad_wyk <- rexp(1000, 1)
test <- ks.test(rozklad_wyk, "pnorm", 1, 1)
#odrzucamy

#punkt a2
test2 <- ks.test(rozklad_wyk, 'pexp', 1)
#zostawiamy

# punkt b
rozkl_gamma <- rgamma(1000, 100, 1)
testb1 <- ks.test(rozkl_gamma, "pnorm", 100, 10)
testb2 <- ks.test(rozkl_gamma, "pgamma", 100, 1)

#przyjmujemy oba

