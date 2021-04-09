RNGkind()

#Question 1
g = 9.8 ## meters per second
h0 = 56.67
v0 = 0
n = 25
tt = seq(0,3.4,len=n) ##time in secs, t is a base function
y = 56.67 + v0 *tt  - 0.5* g*tt^2 + rnorm(n,sd=1)

X = cbind(1,tt,tt^2)
A = solve(crossprod(X))%*%t(X)


#rewrite model:
b2 = g/-2
y = h0 + 0*tt + b2*tt^2+rnorm(n,sd=1)
-2*(A%*%y)[3]
#Answer is not 9.8 because LSE is a random variable. [3] gives coefficient for 
#3rd quadratic term which is -0.5*g. Multiply by 2 to get estimate of g

#Question 2

set.seed(1)
B = 100000
x = replicate(B,{
              b2 = g/-2
              y = h0 + 0*tt + b2*tt^2+rnorm(n,sd=1)
              g = -2*(A%*%y)[3]
})
sd(x)

#OR
set.seed(1)
B = 100000
g = 9.8 ## meters per second
n = 25
tt = seq(0,3.4,len=n) ##time in secs, t is a base function
X = cbind(1,tt,tt^2)
A = solve(crossprod(X))%*%t(X)

betahat = replicate(B,{
  y = 56.67  - 0.5*g*tt^2 + rnorm(n,sd=1)
  betahats = -2*A%*%y
  return(betahats[3])
})
sqrt(mean( (betahat-mean(betahat) )^2))
