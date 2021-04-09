library(SpikeInSubset)
data(mas133)

#Question 1  make plot of first 2 samples and compute correlation
e <- exprs(mas133)
plot(e[,1],e[,2],main=paste0("corr=",signif(cor(e[,1],e[,2]),3)),cex=0.5)
k <- 3000 #Defines inside box
b <- 1000 #a buffer
polygon(c(-b,k,k,-b),c(-b,-b,k,k),col="red",density=0,border="red")
#which genes below k for both samples
mean(e[,1]<k & e[,2]<k)

#Question 2 same as 1 but with logs
library(rafalib)
mypar(1,2)
plot(log2(e[,1]),log2(e[,2]),main=paste0("corr=",signif(cor(log2(e[,1]),log2(e[,2])),2)),cex=0.5)
k <- log2(3000)
b <- log2(0.5)
polygon(c(b,k,k,b),c(b,b,k,k),col="red",density=0,border="red")
#tails do not dominate the plot ie: 95% of data is no longer in a tiny section of plot

#Question 3
e = log2(exprs(mas133))
plot((e[,1]+e[,2])/2,e[,2]-e[,1],cex=0.5)
sd(e[,2]-e[,1])

#Question 4
#Fold change of 2 relates to differences of 1(in abs value). Count the occurances:
sum(abs(e[,2]-e[,1])>1)
