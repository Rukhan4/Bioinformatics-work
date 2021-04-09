#MATRIX ALGEBRA IN PRACTISE 1 -----------------------------------------------------------

g = 9.8 #gravitational acceleration
n = 25 #observations
tt = seq(0,3.4,len=n) #timeframe
f = 56.67 + 0*tt -0.5*g*tt^2 #56.67 is height of tower of piza
y = f + rnorm(n,sd=1) #Observational error
plot(tt,y,xlab="Time in seconds",ylab = "Distance in Metres") #What we got
lines(tt,f,col=2) #What we expected

#Define function for residual sum of squares
rss = function(Beta0,Beta1,Beta2){
  r = y - (Beta0+Beta1*tt+Beta2*tt^2)
  sum (r^2)
}

Beta2s = seq(-10,0,len=100)
RSS = sapply(Beta2s,rss,Beta0=55,Beta1=0) #Beta are guesses
plot(Beta2s,RSS,type="l")

#OR simply just do:

tt2 = tt^2
fit = lm(y~tt+tt2)
summary(fit)

#MATRIX ALGEBRA IN PRACTISE 2 ----------------------------------------------------------
#Obtain least square estimate

#1 create X matrix with covariates as functions
X = cbind(1,tt,tt^2)

#2 Define an arbitrary Beta
Beta = matrix(c(55,0,5),3,1)

#3 do obs error - X times Beta using matrix operation to find residuals
r =y - X%*%Beta

#4 get RSS
RSS = t(r)%*%r
RSS
rss(55,0,5)
#using crossprod
RSS2 = crossprod(r)
RSS2

#5 get least squares estimates
Betahat = solve(t(X)%*%X)%*%t(X)%*%y
Betahat
#using crossprod
betahat = solve(crossprod(X))%*%crossprod(X,y)
betahat

#alternative to solve since it is unstable
QR = qr(X)
Q = qr.Q(QR)
R = qr.R(QR)
backsolve(R,crossprod(Q,y))
