library(tissuesGeneExpression)
data(tissuesGeneExpression)

colind = tissue%in%c("kidney","liver","colon")
mat = e[,colind]
ftissue = factor(tissue[colind])
dim(mat)

#Compute SVD on subset of the matrix (only 99 columns cus only 3 tissues)
#To find columns with most variability
s = svd(mat - rowMeans(mat)) #Remove means because dont want differences in means to contribute to variability
#When you compute distance between two columns the mean of the genes doesnt come in. They cancel out when
#you subtrack them from one another. 

#Construct z matrix with 2D
z = diag(s$d[1:2])%*%t(s$v[,1:2]) #Can change 1,2 to anything to view different sources of variability
dim(z)
z = t(z)
plot(z)
#If we want to know distance between 2 columns of mat--these are 22 dimension vectors so its not easy
#Instead in visualization above, the idea is the distance is approximated by the distance of points in this plot

library(rafalib)
mypar(1,1)
plot(z)

#Add color to tissues 
plot(z[,1],z[,2],bg=as.numeric(ftissue),pch=21,xlab="First dimension",ylab="Second dimension")
legend("bottomright",levels(ftissue),col=seq(along=levels(ftissue)),pch=15)

#Function called CMD in R: multidimensional scaling plot:
d = dist(t(mat))
mds = cmdscale(d) #Value k can be included here to change dimensions eg: d,k=4
plot(mds[,1],mds[,2],bg=as.numeric(ftissue),pch=21,xlab="First dimension",ylab="Second dimension")
legend("bottomleft",levels(ftissue),col=seq(along=levels(ftissue),pch=15))
