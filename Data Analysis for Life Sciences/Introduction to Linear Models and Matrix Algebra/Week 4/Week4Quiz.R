#Question 1 idk
spider = read.csv("spider_wolff_gorb_2013.csv",skip=1)
x = model.matrix(~type+leg,data=spider)
fit = lm(friction~leg+type,data=spider)
C = matrix(c(0,0,-1,0,1),1,5)
Sigma = sum(fit$residuals^2)/(nrow(x)-ncol(x)*solve(t(x)%*%x))
Sigma[3,5]

#Question 2

#In this last question, we will use Monte Carlo techniques to observe the distribution of the ANOVA's 
#"F-value" under the null hypothesis, that there are no differences between groups.
#Suppose we have 4 groups, and 10 samples per group, so 40 samples overall:
N <- 40
p <- 4
group <- factor(rep(1:p,each=N/p))
X <- model.matrix(~ group)

#F value is mean sum of squares of terms of interest(explanatory power) / mean sum of squares of residual model(leftover variance)
#If F value is large it means the group variable explains a lot of the variance in the data
#compared to the amount of variance left in the data after using group information.
#We will calculate these values exactly here:

#First generate some random, null data, where the mean is the same for all groups:
Y <- rnorm(N,mean=42,7)

#The base model we wil compare against is simply Y-hat = mean(Y), which we will call mu0, 
#and the initial sum of squares is the Y values minus mu0:
mu0 = mean(Y)
initial.ss = sum((Y-mu0)^2)

#We then need to calculate the fitted values for each group, which is simply the mean of each group, 
#and the residuals from this model, which we will call after.group.ss for the sum of squares 
#after using the group information:
s <- split(Y, group)
after.group.ss <- sum(sapply(s, function(X) sum((X - mean(X))^2)))

#Then the explanatory power of the group variable is the 
#initial sum of squares minus the residual sum of squares:
(group.ss <- initial.ss - after.group.ss)

#We calculate the mean of these values, but we divide by terms which remove the number of fitted parameters. 
#For the group sum of squares, this is number of parameters used to fit the groups (3, because the intercept is in the initial model). 
#For the after group sum of squares, this is the number of samples minus the number of parameters total (So N - 4, including the intercept).
group.ms <- group.ss / (p - 1)
after.group.ms <- after.group.ss / (N - p)

#The F-value is simply the ratio of these mean sum of squares.
f.value <- group.ms / after.group.ms
f.value

#MONTE CARLO SET UP TO GET A MORE ACCURATE f.value
set.seed(1)
Fs = replicate(1000, {
  Y = rnorm(N,mean=42,7)
  mu0 = mean(Y)
  initial.ss = sum((Y - mu0)^2)
  s = split(Y, group)
  after.group.ss = sum(sapply(s, function(x) sum((x - mean(x))^2)))
  (group.ss = initial.ss - after.group.ss)
  group.ms = group.ss / (p - 1)
  after.group.ms = after.group.ss / (N - p)
  f.value = group.ms / after.group.ms
  return(f.value)
})
mean(Fs)

hist(Fs, col="grey", border="white", breaks=50, freq=FALSE)
xs <- seq(from=0,to=6,length=100)
lines(xs, df(xs, df1 = p - 1, df2 = N - p), col="red")
