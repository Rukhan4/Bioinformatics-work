dat <- read.csv("femaleMiceWeights.csv")

#Question 1 

set.seed(1)
n <- 100
dice <- 6
p <-1/dice 
zs <- replicate(10000,{
  x <- sample(1:dice,n,replace=TRUE) #Proportion of times we see a 6 when rolling n=100 dice
  (mean(x==6) - p) / sqrt(p*(1-p)/n)
})

mean(abs(zs)>2)
qqnorm(zs)
abline(0,1)

#Question 2 testing values
ps <- c(0.5,0.5,0.01,0.01)
ns <- c(5,30,30,100)
library(rafalib)
mypar(4,2)
for(i in 1:4){
  p <- ps[i]
  dice <- 1/p
  n <- ns[i]
  zs <- replicate(10000,{
    x <- sample(1:dice,n,replace=TRUE)
    (mean(x==1) - p) / sqrt(p*(1-p)/n)
  }) 
  hist(zs)
  qqnorm(zs)
  abline(0,1)
}

#Question 3 
library(dplyr)
X <- filter(dat,Diet=="chow")%>%select(Bodyweight)%>%unlist
mean(X)

#Question 6
sd(X)

#Question 7 (2 is the observed difference)
2 *(1-pnorm(2/sd(X)*sqrt(12)))

#Question 8
Y <- filter(dat,Diet=="hf")%>%select(Bodyweight)%>%unlist
sqrt((sd(X)^2/12)+(sd(Y)^2/12))

#Question 9 #observed/sd -> ( mean(Y) - mean(X) ) / sqrt( var(X)/12 + var(Y)/12)
ttest = t.test(Y,X)$stat
ttest

#Question 11 
Z <- ( mean(Y) - mean(X) ) / sqrt( var(X)/12 + var(Y)/12)
pvalue <- 2*(1-pnorm(Z))
pvalue

#Question 12
ttest2 = t.test(X,Y)$p.value
ttest2
