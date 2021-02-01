
#Question 1

alphas <- seq(0,0.25,0.01)
m = 1:10000
bonferroni = alphas/m
sidak = 1-(1 - alphas)**(1/m)
library(rafalib)
mypar(1,2)
plot(m, sidak, col = "red", ylab = "k", pch = 20)
plot(m, bonferroni, col = "green", pch = 20)

alphas <- seq(0,0.25,0.01)
par(mfrow=c(2,2))
for(m in c(2,10,100,1000)){
  plot(alphas,alphas/m - (1-(1-alphas)^(1/m)),type="l")
  abline(h=0,col=2,lty=2)
}

#Question 2
set.seed(1)
B = 10000
m = 8793
pvals <- matrix(runif(B*m,0,1),B,m)
k = alpha/m
mistakes = rowSums(pvals<k)
mean(mistakes>0)

#Question 3
set.seed(1)
B = 10000
m = 8793
pvals <- matrix(runif(B*m,0,1),B,m)
k = (1-(1-alpha)^(1/m))
mistakes = rowSums(pvals<k)
mean(mistakes>0)
