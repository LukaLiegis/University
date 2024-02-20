# Question 1
x <- Insurance_Claims_Payments_Data$Claim
y <- Insurance_Claims_Payments_Data$Payment
# a
sum(x)
sum(y)
sum(x^2)
sum(y^2)
sum(x*y)
# b
mean(x)
mean(y)

# Question 2
# a
plot(x, y, main="Plot of Y versus X")
# b
model = lm(y ~ x)
# c
abline(model)
# d
predict(model, newdata = data.frame(x = 3))