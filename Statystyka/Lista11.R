mieszkania <- read.csv2("D:\\lab\\profiles\\macsko6154\\Studia\\Statystyka\\mieszkania.csv")

k <- 6
p <- 1/k * rep(1, times = k)
m <- c(171, 200, 168, 213, 226, 222)
n <- sum(m)

me <- n * p

t <- sum((m - me)^ 2 / me) 
wp <- 1 - pchisq(t, k - 1)

alpha <- 0.007
# odrzucamy bo wp jest mniejsze niz 0.007 mamy mocne dowody na to że kostak nie jest sprawiedliwa

p0 <- 1/k * rep(1, times = k)

chisq.test(m,p = p0 )





