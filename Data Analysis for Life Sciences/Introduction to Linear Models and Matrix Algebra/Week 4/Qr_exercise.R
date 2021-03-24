spider = read.csv("spider_wolff_gorb_2013.csv",skip=1)

fit = lm(friction~type+leg,data=spider)
betahat = coef(fit) #What we want to solve
#matrix work
Y = matrix(spider$friction,ncol=1)
X = model.matrix(~type+leg,data=spider)

#Exercise 1 
QR = qr(X)
Q = qr.Q(QR)
Q[1,1]

#Exercise 2
R = qr.R(QR)
R[1,1]

#Exercise 3 
Z = crossprod(Q,Y)
Z[1,1]

#Convince myself that QR gives the least squares solution
#R^-1(Q^T Y) compared to betahat
first = diag(R)*Z
betahat = backsolve(R,crossprod(Q,Y))
