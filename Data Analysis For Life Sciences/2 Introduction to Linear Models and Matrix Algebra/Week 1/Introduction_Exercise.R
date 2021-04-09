#Question 1 

library(UsingR)
data("father.son",package="UsingR")
x <- father.son
avgson <- mean(x$sheight)
avgson

#Question 2 

x = father.son$fheight
y = father.son$sheight                   
mean(y[round(x)==71])

#library(dplyr) filter(father.son,round(fheight)==71) %>% summarize(mean(sheight))

