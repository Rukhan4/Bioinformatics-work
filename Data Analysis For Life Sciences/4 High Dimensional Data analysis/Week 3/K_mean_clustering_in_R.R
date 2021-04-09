library(tissuesGeneExpression)
data(tissuesGeneExpression)

km = kmeans(t(e), centers=7)
table(tissue,clusters=km$cluster)

#Visualize
d = dist(t(e))
mds = cmdscale(d)
plot(mds[,1],mds[,2],col=km$cluster)
