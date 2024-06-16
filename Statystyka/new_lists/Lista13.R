dane <- read.csv2('C:\\Users\\mabuza\\Desktop\\mieszkania.csv')

#zadanie 1
# Dane egzaminacyjne
analiza <- c(28, 26, 23, 18, 14, 12)
algebra <- c(25, 27, 20, 24, 16, 13)

# Korelacja Pearsona
a_per <- cor(analiza, algebra, method = "pearson")

# Korelacja Spearmana
a_sper <- cor(analiza, algebra, method = "spearman")

# Korelacja Kendalla
a_ken <- cor(analiza, algebra, method = "kendall")

# Testy hipotezy H0: ρXY = 0
a_per_test <- cor.test(analiza, algebra, method = "pearson")
a_sper_test <- cor.test(analiza, algebra, method = "spearman")
a_ken_test <- cor.test(analiza, algebra, method = "kendall")



#zadanie 2
#wygenerowanie 100 par liczb
n <- 100
x <- rnorm(n)
y <- rnorm(n)

#obliczenie współczynnika korelacji
b_pear <- cor(x,y,method = 'pearson')
b_pear_test <- cor.test(x,y,method = 'pearson')


b_spear <- cor(x,y,method = 'spearman')
b_spear_test <- cor.test(x,y,method = 'spearman')


b_kend <- cor(x,y,method = 'kendall')
b_kend_test <- cor.test(x,y,method = 'kendall')
# jezeli p-value < alfy to odrzucamy na poziomie

#test permutacyjny 
perm_test <- function(x, y, method = "pearson", B = 1000) {
  n <- length(x)
  orig_cor <- cor(x, y, method = method)
  perm_cor <- numeric(B)
  for (i in 1:B) {
    perm_y <- sample(y)
    perm_cor[i] <- cor(x, perm_y, method = method)
  }
  p_value <- mean(abs(perm_cor) >= abs(orig_cor))
  return(list(original_correlation = orig_cor, p_value = p_value))
}
b_perm_sper <- perm_test(x,y,method = "spearman")
b_perm_pers <- perm_test(x,y,method = "pearson")
b_perm_kend <- perm_test(x,y,method = "kendall")

# Bootstrap 
bootstrap_cor <- function(x, y, R = 1000) {
  n <- length(x)
  boot_cor <- numeric(R)
  for (i in 1:R) {
    indices <- sample(1:n, n, replace = TRUE)
    boot_cor[i] <- cor(x[indices], y[indices])
  }
  conf_interval <- quantile(boot_cor, c(0.025, 0.975))
  return(list(bootstrap_correlations = boot_cor, conf_interval = conf_interval))
}

bootstrap_results <- bootstrap_cor(x, y, R = 1000)
bootstrap_results$conf_interval
# Plotowanei rozrzutu danych na wykresie

plot(x,y,main = 'Rozrzut zmiennych x i y',xlab = 'x', ylab = 'y')
grid()
abline(lm(x ~ y), col = 'red')

# Zadanie 3

# Generowanie par X,V
V <- 0.2 * x + 0.96 * y

#jezeli bedzie trzeba wyliczyc odzielna korealcje dla różnich metod poprostu method = np. pearson
corXV <- cor(x, V)

#testy
test_pearson_XV <- cor.test(x, V, method = "pearson")
test_spearman_XV <- cor.test(x, V, method = "spearman")
test_kendall_XV <- cor.test(x, V, method = "kendall")

#zadanie 4
# generowanie 100 realizacji par
n <- 100
x <- rnorm(n)
y <- rnorm(n)

# punkt a
rho <- 0.7
V <- rho * x + sqrt(1-rho * rho) * y

#punkt b
H <- 170 + 12 * x
W <- 65 + 10 * V

#obliczanie srednich
srednia_H <- mean(H)
srednia_W <- mean(W)

#obliczanie odchylen
sd_H <- sd(H)
sd_W <- sd(W)

#wspolczynnik korelacji persona
cor_pers <- cor(H, W, method = "pearson")
cor_spear <- cor(H, W, method = "spearman")
cor_kend <- cor(H, W, method = "kendall")

# estymator gęstości
plot(density(H),main = 'Estymator h', xlab = 'h', ylab = 'density')
curve(dnorm(x,mean = srednia_H, sd = sd_H), col = 'blue', lty = 1, add = TRUE)
legend('topright',legend = c('estymator','rozkład normalny'),
       col = c('black','blue'),lty = 1, cex = 0.4)

plot(density(W),main = 'Estymator w', xlab = 'w', ylab = 'density')
curve(dnorm(x,mean = srednia_W, sd = sd_W), col = 'purple', add = TRUE)
legend('topleft',legend = c('estymator','rozkład normalny'),
       col = c('black','purple'),lty = 1, cex = 0.4)

# test czy pochodza z rozkladu normalnego
shapiro_test_H <- shapiro.test(H)
shapiro_test_W <- shapiro.test(W)

#rozrzut zmiennych
plot(H,W,main = 'Rozrzut zmiennych H i W',xlab = 'H', ylab = 'W')
grid()
abline(lm(H ~ W), col = 'red')


#zadanie 5

#korelacja dla macierzy persona spearmana i kenalada 
dane$m2 <- dane$Cena/dane$Metraz
dane_data_frame <- data.frame(dane)[, c("Metraz", "Cena", "m2", "Pokoje")]
cor_pearson_matrix <- cor(dane_data_frame, method = "pearson")
cor_spearman_matrix <- cor(dane_data_frame, method = "spearman")
cor_kendall_matrix <- cor(dane_data_frame, method = "kendall")


#test hipotezy
e5_pear <- cor.test(dane$Metraz,dane$m2,method = 'pearson')
e5_spear <- cor.test(dane$Metraz,dane$m2,method = 'spearman')
e5_kend <- cor.test(dane$Metraz,dane$m2,method = 'kendall')

