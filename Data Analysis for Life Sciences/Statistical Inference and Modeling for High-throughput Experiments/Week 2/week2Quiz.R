#Question 2
16/(16+83)
9/(9+92)

#Question 3 
m = 6319
alpha = 0.05
k = alpha/m

#Question 4 
set.seed(11)
pvals= runif(m,0,1)
sum(pvals<k)

#Question 5
set.seed(12)
B = 10000
result = replicate(B,{
  pvals= runif(m,0,1)
  sum(pvals<k)
})
mean(result>0)

#Set up 6-10 
if (!file.exists("bottomly_eset.RData")) download.file("http://bowtie-bio.sourceforge.net/recount/ExpressionSets/bottomly_eset.RData",
                                                       "bottomly_eset.RData")
                                                                                                            
load("bottomly_eset.RData")
library(Biobase)
library(genefilter)
library(qvalue)

dat = exprs(bottomly.eset)
strain = pData(bottomly.eset)$strain
results = rowttests(dat,strain)
pvals = results$p.value
pvals = na.omit(pvals)

#Question 6
sum(pvals<0.05)

#Question 7 
pcut = (alpha/nrow(dat))

#Question 8 
z = sum(pvals<pcut)

#Question 9 
fdr = p.adjust(pvals,method="fdr",n=length(pvals))
sum(fdr<0.05)            

#Question 10
sum(qvalue(pvals)$qvalues<0.05)
