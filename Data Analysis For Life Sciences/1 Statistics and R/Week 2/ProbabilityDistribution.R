install.packages("gapminder")
#contains life expectancy, GDP per capita and population by country every 5 years from 1952 to 2007
library(gapminder)
data(gapminder)

#Life expectancy for only year 1952
dat1952 <- gapminder[gapminder$year=="1952",]
x <- dat1952$lifeExp
hist(x)
mean(x<=40)

#Creating an ecdf function
prop = function(q){
  mean(x<=q)
}
prop(40)
qs = seq(from=min(x),to=max(x), length = 20)
props= sapply(qs,prop)
plot(qs,props,main="life expectancy(q) for range of years")
plot(ecdf(x))
#one liner: props = sapply(qs,function(q)mean(x<=q))
#plot(props)
#plot(ecdf(x))