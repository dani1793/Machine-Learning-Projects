redditData <- read.csv('reddit.csv')

names(redditData)
table(redditData$income.range)
summary(redditData)
summary(redditData$employment.status)
table(redditData$employment.status)

levels(redditData$age.range)
# If the package is not installed use the following command to install the package
# After the package is installed use execute the following commands accordingly
# install.packages('ggplot2', dependencies = T)
library(ggplot2)
qplot(data = redditData, x = age.range)

qplot(data = redditData, x = cheese)

# Ordered factoring of variables in data
redditData$age.range <- factor(redditData$age.range, levels = c('Under 18', '18-24', '25-34', '35-44','45-54','55-63','64 or Above'),
                               ordered = T)
