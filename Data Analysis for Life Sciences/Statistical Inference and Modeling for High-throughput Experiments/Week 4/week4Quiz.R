#Question 1 in book 

#Question 2
library(tidyverse)
day21 = ChickWeight%>%filter(Time=="21")
#A
x = mean(day21$weight)
#B
y = sd(day21$weight)
#C
1-pnorm(300,x,y)

graph = qqnorm(day21$weight)
qqline(day21$weight)


#Question 3
library(dplyr)
#A
a = day21%>%filter(Diet=="3")
b = mean(a$weight)

#B
c = sd(a$weight)

#C
1-pnorm(300,b,c)

#Question 4
#A
Betas = c^2/(c^2+y^2)
exptweight = Betas*(x)+(1-Betas)*b

#B
SE = sqrt(1/(1/(c^2)+1/y^2))
exptweight/SE

#C

#Setup 6 - 8 
load("bottomly_eset.RData")
library(Biobase)
library(genefilter)
library(qvalue)



dat = exprs(bottomly.eset)    # gene expression matrix
strain = pData(bottomly.eset)$strain    # strain factor

results <- rowttests(dat,strain)
pvals <- results$p.value

set.seed(1)
permut = sample(strain)

#Questin 6 
rowtt = rowttests(dat,permut)$p.value
rowtt = na.omit(rowtt)
sum(rowtt<0.05)

#Question 7 
library(rafalib)
hist(pvals)
hist(rowtt)
