#zaddanie 1
#punkt a
n <- 100
mean_iq <- 109
var <- 225

blad_standardowy =sqrt(var / n)
mi <- 105
t = (mean_iq - mi) / blad_standardowy
p = 2 * (1 - pnorm(abs(t)))
# p < 0.05 nie przyjmujemy  mocne dowody przeciwko

#punk b
dystrybuanta_stud <- n - 1

test_stud <- 2 * (1 - pt(abs(t), dystrybuanta_stud))
# 0.001 < p < 0.01 mamy silne dowody przeciwko h0


#zadanie 3
dane <- read.csv2("C://users//mabuza//Desktop//waga1.csv")
wzrost_m = dane[dane$plec == "0", "Wzrost"]
sredni_wzrost <- mean(wzrost_m)
sd <- sd(wzrost_m)
mi <- 172

t <- (mi - sredni_wzrost)/sd * sqrt(length(wzrost_m))
p <- 2 * (1 - pnorm(abs(t)))


#test studenta

p <- 2 * (1 - pt(abs(t),length(wzrost_m) - 1))

# t.test()
t_test <- t.test(dane[dane$plec==0, "Wzrost"], mu = mi, alternative = "two.sided")



#zadanie 4
roznica <- dane["Waga_po"] - dane["Waga_przed"]
srednia <- mean(roznica[, "Waga_po"])
sd <- sd(roznica[, "Waga_po"])
blad_standardowy = sd / sqrt(nrow(dane))
mi <- 2

t <- (srednia - mi) / blad_standardowy
#test z
p <- 2 * (1 - pnorm(abs(t)))

#test studenta
p <- 2 * (1 - pt(abs(t), nrow(dane) - 1))

#t.test()
t.test(roznica, mu = mi, alternative ="two.sided")

# mozna dowody przeciwko
