dat <- read.csv("femaleMiceWeights.csv")
View(dat)
library(dplyr)
#Only mice on chow diet
controls <- filter(dat,Diet == "chow")
View(controls)
othercontrols <- select(controls,Bodyweight)
unlist(othercontrols)


## Sleek one liner 


onelinecontrols <- filter(dat,Diet=="chow")%>%select(Bodyweight)%>%unlist
View(onelinecontrols)
mean(onelinecontrols)