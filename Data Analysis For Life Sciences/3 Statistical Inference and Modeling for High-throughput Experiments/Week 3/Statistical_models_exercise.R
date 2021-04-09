#Question 1
dbinom(2,4,0.49)

#Question 2
dbinom(4,10,0.49)

#Question 3
1-pbinom(10,20,0.4)

#Question 4
1 - dbinom(0,189000000,p=1/175223510)

#Question 5
1 - pbinom(1,189000000,p=1/175223510)

#Question 6 Normal approximation
pbinom(9,20,0.4)-pbinom(7,20,0.4)

#Question 7
b = (9-20*0.4)/sqrt(20*0.4*0.6)
a = (7-20*0.4)/sqrt(20*0.4*0.6)
pnorm(b)-pnorm(a)

#Question 8 
exact = pbinom(450,1000,0.4)-pbinom(350,1000,0.4)
d = (450-1000*0.4)/sqrt(1000*0.4*0.6)
c = (350-1000*0.4)/sqrt(1000*0.4*0.6)
approx = pnorm(d)-pnorm(c)
abs(exact-approx)

#Question 9
Ns <- c(5,10,30,100)
ps <- c(0.01,0.10,0.5,0.9,0.99)
library(rafalib)
mypar(4,5)
for(N in Ns){
  ks <- 1:(N-1)
  for(p in ps){
    exact = dbinom(ks,N,p)
    a = (ks+0.5 - N*p)/sqrt(N*p*(1-p))
    b = (ks-0.5 - N*p)/sqrt(N*p*(1-p))
    approx = pnorm(a) - pnorm(b)
    LIM <- range(c(approx,exact))
    plot(exact,approx,main=paste("N =",N," p = ",p),xlim=LIM,ylim=LIM,col=1,pch=16)
    abline(0,1)
  }
}

#Question 10 using binomial to approx prob exactly 2 people winning
N <- 189000000
p <- 1/175223510
dbinom(2,N,p)

#If we use normal approx, we would overestimate since p breaks down
a <- (2+0.5 - N*p)/sqrt(N*p*(1-p))
b <- (2-0.5 - N*p)/sqrt(N*p*(1-p))
pnorm(a) - pnorm(b) #WRONG

#Hence, use Poisson approx with rate lambda = Np(no. tickets per 189000000 that win lottery)
dpois(2,N*p)

#Poisson approx prob two or more tickets winning(works like pbinom but for poisson)
soln = 1 - ppois(1,N*p)
soln
