dane <- read.csv2("D:\\lab\\profiles\\macsko6154\\Studia\\Statystyka\\waga1.csv")
mieszkania <- read.csv2("D:\\lab\\profiles\\macsko6154\\Studia\\Statystyka\\mieszkania.csv")



ns <- 1000
n <- length(dane$plec)

nm <- length(which(dane$plec ==0))
xnm <- length(which(dane$plec ==0 & dane$Waga_po >70))

nk <- length(which(dane$plec ==1))
xnk <- length(which(dane$plec ==1& dane$Waga_po > 70))


#proporcje
pm <- 20/nm
pk<- 8/nk

alpha <- 0.05

od <- ns * alpha / 2


