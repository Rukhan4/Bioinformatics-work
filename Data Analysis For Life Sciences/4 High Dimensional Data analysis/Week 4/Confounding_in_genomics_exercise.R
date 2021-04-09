library(Biobase)
library(devtools)
install_github("genomicsclass/GSE5859")
library(GSE5859)
data(GSE5859)
#extract gene expression data
geneExpression = exprs(e)
#extract sample info
sampleInfo = pData(e)
#These are bioconductor functions

#Exercise 1 #For how many years more than one ethnicity rep
#Extract year from each date:
year = format(sampleInfo$date,"%y")
tab = table(year,sampleInfo$ethnicity)
x = rowSums(tab!=0)
sum(x>=2)

#Exercise 2 #Proportion of month.year more than one ethnicity rep
#Extract month:
month.year = format(sampleInfo$date,"%m%y")
tab = table(month.year,sampleInfo$ethnicity)
x = rowSums(tab!=0)
mean(x>=2)

#Exercise 3 CEU samples processed in 2002 to 2003
library(genefilter)
library(qvalue)
year = factor(format(sampleInfo$date,"%y"))
index = which(year%in%c("02","03")&sampleInfo$ethnicity=="CEU")
year = droplevels(year[index])
pval = rowttests(geneExpression[,index],year)$p.value
qval = qvalue(pval)
sum(qval$qvalues<0.05) #FDR cutoff
qval$pi0

#Exercise 4 CEU samples processed in 2003 to 2004
year = factor(format(sampleInfo$date,"%y"))
index = which(year%in%c("03","04")&sampleInfo$ethnicity=="CEU")
year = droplevels(year[index])
pval = rowttests(geneExpression[,index],year)$p.value
qval = qvalue(pval)
sum(qval$qvalues<0.05)

#Exercise 5 CEU vs ASN
index = which(sampleInfo$ethnicity%in%c("CEU","ASN"))
g = droplevels(sampleInfo$ethnicity[index])
pval = rowttests(geneExpression[,index],g)$p.value
qval = qvalue(pval)
sum(qval$qvalues<0.05)

#Exercise 6 only for samples processed in 2005(two groups represented here)
year = factor(format(sampleInfo$date,"%y"))
index = which(sampleInfo$ethnicity%in%c("CEU","ASN")&year=="05")
g = droplevels(sampleInfo$ethnicity[index])
pval = rowttests(geneExpression[,index],g)$p.value
qval = qvalue(pval)
sum(qval$qvalues<0.05)

#Exercise 7 3 random CEU samples from 2002 vs ASN from 2005
year = factor(format(sampleInfo$date,"%y"))
indexASN = which(sampleInfo$ethnicity=="ASN" & year == "05")
set.seed(3)
indexCEU = sample(which(sampleInfo$ethnicity=="CEU" & year == "02"),3)
index = c(indexASN,indexCEU)
g = droplevels(sampleInfo$ethnicity[index])
pval = rowttests(geneExpression[,index],g)$p.value
qval = qvalue(pval)
sum(qval$qvalues<0.05)
