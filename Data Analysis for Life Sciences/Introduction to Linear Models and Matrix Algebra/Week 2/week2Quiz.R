#Question 1 
X = matrix(c(1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1),nrow=6)
rownames(X) = c("a","a","b","b","c","c")
beta = c(10,3,-3)

fitted = X%*%beta
fitted[3:4,]

#Question 2 

fitted[5:6,]

#Question 3 HOW TO USE REPLICATE - MONTE CARLO----------------------------------------------------------
library(UsingR)
x = father.son$fheight
y = father.son$sheight
n = length(y)
set.seed(1)
N =  50
rang = 10000
index = sample(n,N)

#ONE TERM
N =  50
index = sample(n,N)
sampledat = father.son[index,]
x = sampledat$fheight
y = sampledat$sheight
betahat =  lm(y~x)$coef

#REPLICATE WITH MONTE CARLO
betahat = replicate(rang,{
  index = sample(n,N)
  sampledat = father.son[index,]
  x = sampledat$fheight
  y = sampledat$sheight
  lm(y~x)$coef[2]
})
sqrt ( mean( (betahat - mean(betahat) )^2 ))
sd(betahat)
#Same-ish answer ^^^^^


#Question 4 COVARIANCE
x = father.son$fheight
y = father.son$sheight
covariance = mean((y - mean(y))*(x-mean(x)))
