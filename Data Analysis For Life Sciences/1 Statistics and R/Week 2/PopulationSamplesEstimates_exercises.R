dat <- read.csv("mice_pheno.csv")
#Remove lines that contain missing values 
dat<-na.omit(dat)
library(dplyr)

#Exercise 1 
x<- filter(dat,Sex=="M",Diet=="chow")%>%select(Bodyweight)%>%unlist
mean(x)

#Exercise 2
library(rafalib)
popsd(x)

#Exercise 3
set.seed(1)
X <- sample(x,25)
mean(X)

#Exercise 4
y<- filter(dat,Sex=="M",Diet=="hf")%>%select(Bodyweight)%>%unlist
mean(y)

#Exercise 5
popsd(y)

#Exercise 6
set.seed(1)
Y = sample(y,25)
mean(Y)

#Exercise 7
abs(((mean(y)-mean(x)))-(mean(Y)-mean(X)))

#Exercise 8
x<- filter(dat,Sex=="F",Diet=="chow")%>%select(Bodyweight)%>%unlist
mean(x)
set.seed(2)
X <- sample(x,25)
mean(X)

y<- filter(dat,Sex=="F",Diet=="hf")%>%select(Bodyweight)%>%unlist
mean(y)
set.seed(2)
Y <- sample(y,25)
mean(Y)

abs(((mean(y)-mean(x)))-(mean(Y)-mean(X)))

    