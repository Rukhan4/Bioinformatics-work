library(GSE5859Subset)
data(GSE5859Subset)
mds = cmdscale(dist(t(geneExpression)))
set.seed(10)
result = kmeans(t(geneExpression),center=5)
library(rafalib)
mypar(1,1)
plot(mds,bg=result$cluster,pch=21)
table(sampleInfo$group,result$cluster)
table(sampleInfo$date,result$cluster)
#Reorder
table(sampleInfo$date,result$cluster)[,c(4,1,5,3,2)]
