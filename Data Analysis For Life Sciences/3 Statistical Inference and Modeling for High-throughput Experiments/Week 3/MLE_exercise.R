#In this assessment we are going to try to answer the question: 
#is there a section of the human cytomegalovirus genome in which the rate of palindromes is higher than expected?
library(devtools)
install_github("genomicsclass/dagdata")
library(dagdata)
data(hcmv) #palindrome data

#Locations of palindromes on the genome of virus. p is small hence rare.
library(rafalib)
mypar()
plot(locations,rep(1,length(locations)),ylab="",yaxt="n")

#Break genome into bins of 4000 base epairs then we have Np, not so small we might be able to use
#Poisson to model the no of palindromes in each bin. 
breaks=seq(0,4000*round(max(locations)/4000),4000)
tmp=cut(locations,breaks)
counts=as.numeric(table(tmp))

#If model is correct, counts should follow Poisson distribution:
hist(counts) #Pretty good

#lambda = 4 
probs <- dpois(counts,4)
likelihood <- prod(probs)
likelihood #tiny number. More convenient to compute log-likelihoods

logprobs <- dpois(counts,4,log=TRUE)
loglikelihood <- sum(logprobs)
loglikelihood

#Question 1
loglikelihood = function(lambda,x){
  sum(dpois(x,lambda,log=TRUE))
}
lambdas = seq(1,15,len=300)
l = sapply(lambdas,function(lambda) loglikelihood(lambda,counts))
plot(lambdas,l)
mle=lambdas[which.max(l)]
abline(v=mle)
print(mle)
#or just mean(counts)

#Question 2
breaks=seq(0,4000*round(max(locations)/4000),4000)
tmp=cut(locations,breaks)
counts=as.numeric(table(tmp))
binLocation=(breaks[-1]+breaks[-length(breaks)])/2
plot(binLocation,counts,type="l",xlab=)
binLocation[which.max(counts)]

#Question 3
max(counts)

#Question 4 probability of seeing a count 14 or more where rate is lambda:
lambda = mean(counts[ - which.max(counts) ])
pval = 1 - ppois(13,lambda)

#Question 6 bonferroni guarantee FWER of 0.05
0.05/57

#Question 7
ps <- (seq(along=counts) - 0.5)/length(counts)
lambda <- mean( counts[ -which.max(counts)])
poisq <- qpois(ps,lambda)
qqplot(poisq,counts)
abline(0,1)

