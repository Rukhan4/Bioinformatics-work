#imitate heights for men(0) and women(1)
n = 10000
RNGkind(sample.kind = "Rounding")
set.seed(1)
men = rnorm(n,176,7) #height in centimeters
women = rnorm(n,162,7) #height in centimeters
y = c(rep(0,n),rep(1,n))
x = round(c(men,women))
##mix it up
ind = sample(seq(along=y))
y = y[ind]
x = x[ind]

RNGkind(sample.kind = "Rounding")
set.seed(5)
N = 250
ind = sample(length(y),N)
Y = y[ind]
X = x[ind]

#Question 1 Use LOESS to estimate f(x)=E(Y|X=x) 
fit = loess(Y~X)
predict(fit,newdata=data.frame(X=168))

##Here is a plot
xs = seq(160,178)
Pr =sapply(xs,function(x0) mean(Y[X==x0]))
plot(xs,Pr)
fitted=predict(fit,newdata=data.frame(X=xs))
lines(xs,fitted)

#Question 2
RNGkind(sample.kind = "Rounding")
set.seed(5)
B = 1000
newfit = replicate(B,{
  ind = sample(length(y),N)
  Y = y[ind]
  X = x[ind]
  fit = loess(Y~X)
  predict(fit,newdata=data.frame(X=168))
})
popsd(newfit)  
