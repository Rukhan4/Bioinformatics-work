library(tissuesGeneExpression)
data(tissuesGeneExpression)

#1 distance between each column 
d = dist(t(e))

#Hierarchical clustering using the distances with hclust()
hc = hclust(d)
class(hc)
plot(hc,cex=0.5,label=tissue)

#Add color
library(rafalib)
mypar(1,1)
myplclust(hc,cex=0.5,label=tissue,lab.col=as.fumeric(tissue)) #Crashes my session?

#Define discrete cluster on dendrogram by putting a cut off line
abline(h=120)
clust = cutree(hc,h=120)

#Discover new biology if we didnt know what tissues present
table(true=tissue,cluster = clust)
#colon is perfectly clustered
#kidney is badly clustered because its spread across the dendrogram