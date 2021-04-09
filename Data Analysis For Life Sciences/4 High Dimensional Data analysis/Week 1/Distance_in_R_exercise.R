library(tissuesGeneExpression)
data(tissuesGeneExpression)
head(e)
head(tissue)
table(tissue)

#Question 1:
sum(tissue=="hippocampus")

#Question 2: samples
d = dist(t(e))
as.matrix(d)[3,45]

#OR
#sqrt( crossprod(e[,3]-e[,45]) )
#sqrt( sum((e[,3]-e[,45])^2 ))

#Question 3 features
which(rownames(e)=="210486_at")
which(rownames(e)=="200805_at")
sqrt(crossprod(e[9961,]-e[333,]))

#OR
#sqrt( crossprod(e["210486_at",]-e["200805_at",]) )

#Question 4
nrow(e)^2

#Question 5
length(d)
ncol(e)*(ncol(e)-1)/2
