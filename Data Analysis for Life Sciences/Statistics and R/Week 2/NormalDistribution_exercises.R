x<- read.csv("femaleControlsPopulation.csv")
x <- unlist(x)
#Make averages5
set.seed(1)
n<-1000
averages5 <- vector("numeric",n)
for (i in 1:n){
  X <- sample(x,5)
  averages5[i] <-mean(X)
}

#Make averages50
set.seed(1)
n<-1000
averages50 <- vector("numeric",n)
for (i in 1:n){
  X <- sample(x,50)
  averages50[i]<-mean(X)
}

#question 1
library(rafalib)
mypar(1,2)
hist(averages5)
hist(averages50)

#question 2
mean(averages50<25 & averages50>23)

#question 3 
first = pnorm(23,23.9,0.43)
second = pnorm(25,23.9,0.43)
abs(mean(first-second))
