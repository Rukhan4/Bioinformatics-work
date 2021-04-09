#Numeric
x = c(1,1,2,2)
f = formula(~x)
model.matrix(f)
class(x)

#Factor
x = factor(c(1,1,2,2))
f =formula(~x)
model.matrix(f)
class(x)

#With 3 levels
x = factor(c(1,1,2,2,3,3))
model.matrix(~x)

#Adding variables with same levels
x = factor(c(1,1,1,1,2,2,2,2))
y = factor(c('a','a','b','b','a','a','b','b'))
model.matrix(~x+y)

#Interaction between variables
model.matrix(~x+y+x:y)
#same as model.matrix(~x*y)

#Effect of base level factor - swaps positions in this case
x = factor(c(1,1,2,2))
model.matrix(~x)

x = relevel(x,"2")
model.matrix(~x)

#Functions / transformations inside a matrix
z = 1:4 #numeric
model.matrix(~z)
model.matrix(~0+z) #removes intercept column
model.matrix(~z + I(z^2))
