library(GSE5859Subset)
data(GSE5859Subset)

#Question 2
#A
s = svd(geneExpression)
s$d[1]
#B
s$d[1]^2/sum(s$d^2)

#C
m = rowMeans(geneExpression)
m = as.vector(m)
cor(m,s$u[,1])

#Question 4
y = geneExpression - rowMeans(geneExpression)
#A
s = svd(y)
s$d[1]
#B
s$d[1]^2/sum(s$d^2)
#C
sum(s$d^2/sum(s$d^2)>0.05)
#D
sum(s$d[1:10]^2/sum(s$d^2))

#Question 5 
y2 = s$u %*% diag(s$d) %*% t(s$v)
resid = y2-y
max(abs(resid))

#Question 6
z = s$d*t(s$v)
#A
sqrt(crossprod(geneExpression[,1]-geneExpression[,2]))
#B
sqrt(crossprod(y2[,1]-y2[,2]))
#C
sqrt(crossprod(z[,1]-z[,2]))
#D
z2 = z[1:10,1:10]
sqrt(crossprod(z2[,1]-z2[,2]))
#OR sqrt(crossprod(z[1:10,1]-z[1:10,2]))

#Question 7 
d = dist(t(geneExpression))
mds = cmdscale(d,k=2)
fdate = factor(sampleInfo$date)
plot(mds,col=fdate)
