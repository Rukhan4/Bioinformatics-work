N = 10000 #no. genes
lambda = 2^seq(1,16,len=N) #assume range is 2 to 1 or 2 to 16, these are true abundances of genes
y = rpois(N,lambda) #null hyp thesis is true for all genes
x = rpois(N,lambda) #independant realizations
ind=which(y>0 & x>0) #make sure no 0 due to ratio and log

library(rafalib)
mypar()
splot(log2(lambda),log2(x/y),subset=ind)

###Real gene expression data

BiocManager::install("parathyroidSE")
library(parathyroidSE)
data("parathyroidGenesSE")
se = parathyroidGenesSE
x = assay(se)[,23]
y = assay(se)[,24]
ind = which(y>0 & x>0)
splot((log2(x)+log2(y))/2,log2(x/y),subset=ind)
