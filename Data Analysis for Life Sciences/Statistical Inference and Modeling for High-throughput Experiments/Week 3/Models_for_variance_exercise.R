library(devtools)
install_github("genomicsclass/tissuesGeneExpression")
library(tissuesGeneExpression)

data("tissuesGeneExpression")
library(genefilter)
y = e[,which(tissue=="endometrium")]

#Question 1
s2 <- rowVars(y)
library(rafalib)
mypar(1,2)
qqnorm(s2)
qqline(s2)
##To see the square root transformation does not help much:
qqnorm(sqrt(s2))
qqline(sqrt(s2))

#Question 2
library(BiocManager)
BiocManager::install("limma")
library(limma)
estimate = fitFDist(s2,14)
estimate$scale

#Question 3
ps <- (seq(along=s2)-0.5)/length(s2)
theoretical<- qf(ps,14,estimate$df2)*estimate$scale 
LIM <- sqrt( range(c(theoretical,s2)) )
mypar(1,2)
qqplot(sqrt( theoretical ), sqrt( s2 ),ylim=LIM,xlim=LIM)
abline(0,1)

#EXCLUDE UPPER 5% VARIANCE GENES
k= sqrt(quantile(s2,0.95))
qqplot(sqrt(theoretical),sqrt(s2),ylim=c(0,k),xlim=c(0,k))
abline(0,1)
