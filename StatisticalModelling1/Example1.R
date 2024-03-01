# Importing data
x <- Global_Temperature_NASA_Data$Year - 1980
y <- Global_Temperature_NASA_Data$Temperature

# Plotting the scatterplot
plot(x, y, main = "Global average surface temperature compared to 1951-80 baseline", xlab = "years elapsed", ylab ="degrees C")

# Model
model = lm(y ~ x)
summary(model)

# Fit regression to model
abline(model)