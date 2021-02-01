RNGkind()

#Question 1

x <- read.csv("femaleControlsPopulation.csv")
x<-unlist(x)
set.seed(1)
n <- 1000
averages50 <- vector("numeric",n)
for (i in 1:n){
  X <- sample(x,50)
  averages50[i] <- mean(X)
}
mean(abs(averages50-mean(x))>1)

#Question 2 

library(gapminder)
data("gapminder")
head(gapminder)
dat1952 <- gapminder[gapminder$year=="1952",]
x = dat1952$lifeExp
mean(x<=60)- mean(x<=40)
