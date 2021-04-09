#When data is binary, probability and expectations are the same thing:
n = 1000
y = rbinom(n,1,0.25)
##Proportion of 1s Pr(Y)
sum(y==1)/length(y)
##Expectation of Y
mean(y)
#Same answers

#Question 1 
#imitate heights for men(0) and women(1)
n = 10000
set.seed(1)
men = rnorm(n,176,7) #height in centimeters
women = rnorm(n,162,7) #height in centimeters
y = c(rep(0,n),rep(1,n))
x = round(c(men,women))
##mix it up
ind = sample(seq(along=y))
y = y[ind]
x = x[ind]
#probability if someone is 176cm tall, if they are a woman
mean(y[x=="176"])

#Question 2 largest height predicted for female
xs = seq(160,178)
pr = sapply(xs,function(x0)mean(y[x==x0]))
plot(xs,pr)              
abline(h=0.5) #above half
abline(v=168) #the exact hit



