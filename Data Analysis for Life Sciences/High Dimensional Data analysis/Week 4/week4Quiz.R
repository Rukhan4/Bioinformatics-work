library(bladderbatch)
data(bladderdata)
# Get the expression data
edata = exprs(bladderEset)
# Get the pheno data
pheno = pData(bladderEset)
ind = which(pheno$batch %in% 1:3)

# subset expression data
expr = edata[ ,ind]

# subset pheno data and redefine factor levels
pdata = data.frame(batch = factor(pheno$batch[ind]),
                   cancer = factor(pheno$cancer[ind]))
table(pdata)

#Question 2
index = which(pdata$cancer == "Normal")
expr_norm = edata[ ,index]
batch_norm = factor(pdata$batch[index])
library(genefilter)
library(qvalue)

pval = rowttests(expr_norm, batch_norm)$p.value

qval = qvalue(pval)$qvalue
mean(qval < 0.05)

#Question 3
pval = rowttests(expr,factor(pdata$cancer))$p.value
qval = qvalue(pval)$qvalue
mean(qval < 0.05)

#Question 4
X = model.matrix(~pdata$cancer + pdata$batch)

#Question 5
#A
pvals = sapply(1:nrow(expr),function(i){
  y = expr[i,]
  fit = lm(y~X-1)
  summary(fit)$coef[2,4]
})
qvals = qvalue(pvals)
mean(qvals$qvalues<0.05)
#B
pvals_1v2 = sapply(1:nrow(expr),function(i){
  y = expr[i,]
  fit = lm(y~X-1) 
  summary(fit)$coef[3,4]
})

qvals_1v2 = qvalue(pvals_1v2)$qvalue
mean(qvals_1v2 < 0.05)
#C
pvals_1v3 = sapply(1:nrow(expr),function(i){
  y = expr[i,]
  fit = lm(y~X-1) 
  summary(fit)$coef[4,4]
})

qvals_1v3 = qvalue(pvals_1v3)$qvalue
mean(qvals_1v3 < 0.05)

#Question 6 
y = expr - rowMeans(expr)
s = svd(y)
varexplained = s$d^2/ sum(s$d^2)
plot(varexplained)
sum(varexplained>0.05)

#Question 7 
pcs = s$v[,1:2]

library(rafalib)
mypar(1,2)
plot(pcs[,1], pcs[,2], col=pdata$cancer)
legend("topleft", legend=levels(pdata$cancer), pch=1, col=1:2)
plot(pcs[,1], pcs[,2], col=pdata$batch)
legend("topleft", legend=levels(pdata$batch), pch=1, col=1:3)

#Question 8 
cors = cor(as.numeric(pdata$cancer),s$v[,1])
abs(cors)

#Question 9
library(sva)
cancer = pdata$cancer
mod = model.matrix(~cancer)
svafit = sva(expr,mod)
svafit$n.sv #No. significant variables

#Question 10
mod0 = model.matrix(~1,data=pdata)
fpvals = f.pvalue(expr, mod, mod0) #Calculates pvalues for each gene(row)
#given a design matrix mod with the variable of interest and a null matrix mod0 that 
#contains all variables except the variable of interest

#Alter the alternative and null model matrices to adjust for surrogate variable
modSv = cbind(mod,svafit$sv)
mod0Sv = cbind(mod0,svafit$sv)
fpval2 = f.pvalue(expr,modSv,mod0Sv)
qfpval2 = qvalue(fpval2)
mean(qfpval2$qvalues<0.05)
