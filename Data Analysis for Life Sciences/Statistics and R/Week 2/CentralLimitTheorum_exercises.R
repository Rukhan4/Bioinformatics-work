library(dplyr)
library(rafalib)
dat <- read.csv("mice_pheno.csv")
dat <- na.omit(dat)
?pnorm

#Exercise 1 within 1 sd away from well approx. list of no. by normal distrib. population
pnorm(1)-pnorm(-1)

#Exercise 2
pnorm(2)-pnorm(-2)

#Exercise 3
pnorm(3)-pnorm(-3)

#Exercise 4 
y <- filter(dat,Sex=="M",Diet=="chow")%>%select(Bodyweight)%>%unlist
z <- (y-mean(y))/popsd(y) #Standard unit formula
mean(abs(z)<=1)

#Exercise 5 
mean(abs(z)<=2)

#Exercise 6
mean(abs(z)<=3)

#Exercise 8 
y <- filter(dat, Sex=="M" & Diet=="chow") %>% select(Bodyweight) %>% unlist
set.seed(1)
avgs <- replicate(10000, mean( sample(y, 25)))
mypar(1,2)
hist(avgs)
qqnorm(avgs)
qqline(avgs)
mean(avgs)
popsd(avgs)

