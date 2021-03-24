library(tissuesGeneExpression)
data(tissuesGeneExpression)
table(tissue)

#Compute distance
x = e[,1]
y = e[,2]
z = e[,87]

tissue[c(1,2,87)]

#Method 1
sqrt(sum((x-y)^2))
sqrt(sum((x-z)^2))

#Method of matrix
sqrt(crossprod(x-y))

#Distance between each pair of samples:
d = dist(t(e))
class(d) #Cant extract info from this, convert it to a matrix
as.matrix(d)[1,2]

#Visualize 
image(as.matrix(d))
