library(UsingR)
x1 = father.son$fheight
y1 = father.son$sheight
n = length(y1)
N = 50
set.seed(1)
index = sample(n,N) #Up to 50
sampledat = father.son[index,] #Size 50 cus N is 50
x = sampledat$fheight
y = sampledat$sheight
betahat = lm(y~x)$coef

#Exercise 1 (sum of squared residuals)
fit = lm(y ~ x)
sumri = sum((y - fit$fitted.values)^2)

#Exercise 2
sigma2 = sumri/(N-2)
X = cbind(rep(1,N),x)
soln = solve(t(X)%*%X)
soln[1,1]

#Exercise 3
diagonal = diag(soln)
ex3 = sigma2*diagonal
sqrt(ex3)
#First answer is standard error for intercept, second is standard error for slope 