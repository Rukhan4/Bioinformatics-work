library(BiocManager)
BiocManager::install("qvalue")

#Question 1

library(GSE5859Subset)
data(GSE5859Subset)
library(genefilter)
g = factor(sampleInfo$group)
pvals = rowttests(geneExpression,g)$p.value
sum(pvals<0.05)

#Question 2 
k = 0.05/length(pvals)
sum(pvals<k)

#Question 3
fdr = p.adjust(pvals,method="fdr")
sum(fdr<0.05)

#Question 4
library(qvalue)
qval = qvalue(pvals)$qvalue
sum(qval<0.05)

#Question 5
qval2 = qvalue(pvals)$pi0
qval2

#Question 6
plot(qvalue(pvals)$qvalue/p.adjust(pvals,method="fdr"))
abline(h=qvalue(pvals)$pi0,col=2)

hist(pvals,breaks=seq(0,1,len=21))
expectedfreq <- length(pvals)/20 #per bin
abline(h=expectedfreq*qvalue(pvals)$pi0,col=2,lty=2)

#Setup for 7-12
set.seed(1)
n <- 24
m <- 8793
B = 1000
delta <- 2
positives <- 500
g = factor(rep(c(0,1),each=12))

#Question 7 FALSE POSITIVES
set.seed(1)
result = replicate(B,{
  mat <- matrix(rnorm(n*m),m,n)
  mat[1:positives,1:(n/2)] <- mat[1:positives,1:(n/2)]+delta
  pvals = rowttests(mat,g)$p.value
  #BONFERRONI
  FP1 = sum(pvals[-(1:positives)]<=0.05/m)
})
mean(result/(m-positives))

#Question 8 FALSE NEGATIVES
set.seed(1)
result = replicate(B,{
  mat <- matrix(rnorm(n*m),m,n)
  mat[1:positives,1:(n/2)] <- mat[1:positives,1:(n/2)]+delta
  pvals = rowttests(mat,g)$p.value
  #BONFERRONI
  FP1 = sum(pvals[-(1:positives)]<=0.05/m)
  FN1 = sum(pvals[1:positives]>=0.05/m)
  c(FP1,FN1)
})
mean(result[2,]/(positives))

#Question 9 FALSE POSITIVES
set.seed(1)
result <- replicate(B,{
  mat <- matrix(rnorm(n*m),m,n)
  mat[1:positives,1:(n/2)] <- mat[1:positives,1:(n/2)]+delta
  pvals = rowttests(mat,g)$p.val
  ##Bonferroni
  FP1 <- sum(pvals[-(1:positives)]<=0.05/m)  
  FN1 <- sum(pvals[1:positives]>0.05/m)
  #p.adjust q-value
  padj = p.adjust(pvals,method="fdr")
  FP2 <- sum(padj[-(1:positives)]<=0.05)
  c(FP1,FN1,FP2)
})
mean(result[3,]/(m-positives))

#Question 10 FALSE NEGATIVES
result <- replicate(B,{
  mat <- matrix(rnorm(n*m),m,n)
  mat[1:positives,1:(n/2)] <- mat[1:positives,1:(n/2)]+delta
  pvals = rowttests(mat,g)$p.val
  ##Bonferroni
  FP1 <- sum(pvals[-(1:positives)]<=0.05/m)  
  FN1 <- sum(pvals[1:positives]>0.05/m)
  #p.adjust q-value
  padj = p.adjust(pvals,method="fdr")
  FP2 <- sum(padj[-(1:positives)]<=0.05)
  FN2 <- sum(padj[1:positives]>0.05)
  c(FP1,FN1,FP2,FN2)
})
mean(result[4,]/positives)

#Question 11 FALSE POSITIVES
result <- replicate(B,{
  mat <- matrix(rnorm(n*m),m,n)
  mat[1:positives,1:(n/2)] <- mat[1:positives,1:(n/2)]+delta
  pvals = rowttests(mat,g)$p.val
  ##Bonferroni
  FP1 <- sum(pvals[-(1:positives)]<=0.05/m)  
  FN1 <- sum(pvals[1:positives]>0.05/m)
  #p.adjust q-value
  padj = p.adjust(pvals,method="fdr")
  FP2 <- sum(padj[-(1:positives)]<=0.05)
  FN2 <- sum(padj[1:positives]>0.05)
  #qvalue q-value
  padj2 = qvalue(pvals)$qvalue
  FP3 <- sum(padj2[-(1:positives)]<=0.05)
  c(FP1,FN1,FP2,FN2,FP3)
})
mean(result[5,]/(m-positives))

#Question 12 FALSE NEGATIVES
result <- replicate(B,{
  mat <- matrix(rnorm(n*m),m,n)
  mat[1:positives,1:(n/2)] <- mat[1:positives,1:(n/2)]+delta
  pvals = rowttests(mat,g)$p.val
  ##Bonferroni
  FP1 <- sum(pvals[-(1:positives)]<=0.05/m)  
  FN1 <- sum(pvals[1:positives]>0.05/m)
  #p.adjust q-value
  qvals1 = p.adjust(pvals,method="fdr")
  FP2 <- sum(qvals1[-(1:positives)]<=0.05)
  FN2 <- sum(qvals1[1:positives]>0.05)
  #qvalue q-value
  padj = qvalue(pvals)$qvalue
  FP3 = sum(padj[-(1:positives)]<=0.05)
  FN3 = sum(padj[1:positives]>0.05)
  c(FP1,FN1,FP2,FN2,FP3,FN3)
})
mean(result[6,]/(positives))
