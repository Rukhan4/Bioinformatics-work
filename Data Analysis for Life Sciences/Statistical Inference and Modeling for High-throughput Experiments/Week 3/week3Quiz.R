#Question 1
A = pbinom(0,30,0.1)
B = dbinom(3,30,0.1)
C = 1 - pbinom(9,30,0.1)

#Question 2
p = 2/1000000
N = 3000000
A = p*N
B = dpois(1,N*p)
C = 1 - ppois(10,N*p)

#Question 3
#binomial
b = (27-30*0.8)/sqrt(30*0.8*0.2)
a = (21-30*0.8)/sqrt(30*0.8*0.2)
A = pnorm(b)-pnorm(a)
#normal
B = pbinom(27,30,0.8) - pbinom(21,30,0.8)

C = abs(A-B)

#Question 4
set.seed(100)
pval_counts = replicate(1000,{
  pvals = replicate(30, {
    cases = rnorm(5,7.5,2.5)
    controls = rnorm(5,7.5,2.5)
    t.test(cases,controls)$p.value
  })
  sum(pvals < 0.05)
})
mean(pval_counts)

#A
counts = (pval_counts)
loglikelihood = function(lambda,x){
  sum(dpois(x,lambda,log=TRUE))
}
lambdas = seq(1,15,len=300)
l = sapply(lambdas,function(lambda) loglikelihood(lambda,counts))
plot(lambdas,l)
mle=lambdas[which.max(l)]
abline(v=mle)
print(mle)
mean(counts)

#B 
1-ppois(3,1.3)

#C 
Np = 30*0.05



#Question 5
x = rf(100,df1=8,df2=16)
set.seed(25)
library(limma)
estimate = fitFDist(x,8)
estimate$df2

#Question 6
#A
set.seed(28)
B = 1000
estimates = replicate(B,{
  xs = rf(100,df1=8,df2=16)
  estimates = fitFDist(xs,8)
  return(estimates$df2)
  })

median(estimates)

#B
mean((estimates<20)&(estimates>12)) 
boxplot(estimates)
summary(estimates)
#Question 7
set.seed(28)
B = 1000
estimates2 = replicate(B,{
  xs = rf(1000,df1=8,df2=16)
  estimates2 = fitFDist(xs,8)
  return(estimates2$df2)
})

median(estimates2)

#B
mean((estimates2<20)&(estimates2>12)) 
summary(estimates2)
boxplot(estimates2)
