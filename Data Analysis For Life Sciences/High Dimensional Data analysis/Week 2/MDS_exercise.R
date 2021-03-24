library(tissuesGeneExpression)
data(tissuesGeneExpression)

#Question 1 relationship between SVD and output of cmdscale() the function in R that performs MDS
#Using z we computed in SVD_exercise question 4:
y = e - rowMeans(e)
s = svd(y)
z = s$d*t(s$v)

#Make mds plot
library(rafalib)
ftissue = factor(tissue)
mypar(1,1)
plot(z[1,],z[2,],col=as.numeric(ftissue))
legend("topleft",levels(ftissue),col=seq_along(ftissue),pch=1)

#Now with cmdscale on original data:
d = dist(t(e))
mds = cmdscale(d)

cor(z[1,],mds[,1])

#Question 2

cor(z[2,],mds[,2])

#Question 3
#Note MDS plot is not the same:
library(rafalib)
ftissue = factor(tissue)
mypar(1,2)
plot(z[1,],z[2,],col=as.numeric(ftissue))
legend("topleft",levels(ftissue),col=seq_along(ftissue),pch=1)
plot(mds[,1],mds[,2],col=as.numeric(ftissue))

#Question 4 dimension of z highest correlation with outcome of sampleInfo$group
library(GSE5859Subset)
data(GSE5859Subset)
#Compute svd and z:
s = svd(geneExpression-rowMeans(geneExpression))
z = s$d*t(s$v)

which.max(cor(t(z),sampleInfo$group))

#Question 5 max correlation
max(cor(t(z),sampleInfo$group))

#Question 6 second highest correlation 
which.max(cor(t(z),sampleInfo$group)[-1])+1

#Question 7 
#Extract months from sampleInfo$date:
month = format( sampleInfo$date, "%m")
month = factor( month)

#z with highest correlation with outcome of month
which.max(cor(as.numeric(month),t(z)))

#Value of correlation
max(cor(as.numeric(month),t(z)))
#Note same dimension is correlated with group and the date. These are correlated:
table(sampleInfo$group,month)
#In this first dimension related directly to group or is it related only through the month?
#Correlation with month is higher. This is related to "batch effects"

#Question 8 
result = split(s$u[,6],geneAnnotation$CHR)
result = result[which(names(result)!="chrUn")]
boxplot(result,range=0)
boxplot(result,range=0,ylim=c(-0.025,0.025))
medians = sapply(result,median)
names(result)[which.max(abs(medians))]
