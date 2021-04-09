library(GSE5859Subset)
data(GSE5859Subset)

#Question 1
sum(sampleInfo$date == "2005-06-27")

#Question 2
geneAnnotation = na.omit(geneAnnotation)
sum(geneAnnotation$CHR=="chrY")

#Question 3
i = which(geneAnnotation$SYMBOL=="ARPC1A")
j = which(sampleInfo$date=="2005-06-10")
geneExpression[i,j]

#Question 4
x = apply(geneExpression,2,median)
y = median(x)

#Question 5
func = function(e,group){
  group = as.factor(group)
  pval = (t.test( e[group==1], e[group==0]))$p.value
  return(pval)
}

g = factor(sampleInfo$group)
ex5 = apply(geneExpression,1,func,g)
min(ex5)
