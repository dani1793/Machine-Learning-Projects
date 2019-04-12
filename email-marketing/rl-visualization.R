library(RcppCNPy)
library(pracma)
mailingListData <- npyLoad("data-cat-4-ML1.npy")
qValues <- npyLoad("q_values-cat-4-1.npy")
episodeSteps <- npyLoad("episode-steps-4.npy")
length(episodeSteps[1,])
par(mfrow=c(3,2))
# plot(1:15001, episodeSteps[1,5:length(episodeSteps[1,])], type="l")
y <- movavg(episodeSteps[1,20:length(episodeSteps[1,])], 100, "s")
plot(1:19986, y, type = 'l', main='Category 1', xlab = 'iterations', ylab = 'number of days covered', 
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
# length(episodeSteps[2,10:length(episodeSteps[2,])])
plot(1:19986,movavg(episodeSteps[2,20:length(episodeSteps[2,])],100, "s"), type = 'l', main='Category 2', xlab = 'iterations', ylab = 'number of days covered', 
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19986,movavg(episodeSteps[3,20:length(episodeSteps[3,])],100, "s"), type = 'l', main='Category 3', xlab = 'iterations', ylab = 'number of days covered', 
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19986,movavg(episodeSteps[4,20:length(episodeSteps[4,])],100, "s"), type = 'l', main='Category 4', xlab = 'iterations', ylab = 'number of days covered', 
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19986,movavg(episodeSteps[5,20:length(episodeSteps[5,])],100, "s"), type = 'l', main='Category 5', xlab = 'iterations', ylab = 'number of days covered',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19986,movavg(episodeSteps[6,20:length(episodeSteps[6,])],100, "s"), type = 'l', main='Category 6', xlab = 'iterations', ylab = 'number of days covered',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)

par(mfrow=c(3,2))
plot(1:19986,movavg(episodeSteps[7,20:length(episodeSteps[7,])],100, "s"), type = 'l', main='Category 7', xlab = 'iterations', ylab = 'number of days covered',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19986,movavg(episodeSteps[8,20:length(episodeSteps[8,])],100, "s"), type = 'l', main='Category 8', xlab = 'iterations', ylab = 'number of days covered',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19986,movavg(episodeSteps[9,20:length(episodeSteps[9,])],100, "s"), type = 'l', main='Category 9', xlab = 'iterations', ylab = 'number of days covered',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
plot(1:19916,movavg(episodeSteps[10,90:length(episodeSteps[10,])],100, "s"), type = 'l', main='Category 10', xlab = 'iterations', ylab = 'number of days covered',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)

# Category 1
# User 2 has cateory 1 as preference  
dim(mailingListData) # 5 x 365
dim(qValues) # 365 x 5

prefActual = mailingListData[2,]
prefPred = qValues[,2]
summary(prefActual)
summary(prefPred)
#par(mfrow=c(2,1))
pred <- ifelse(prefPred > 13, 1, 0)
actual <- ifelse(prefActual == 2 | prefActual == 3, 1, 0)
plot(1:365, actual, type = 'l', lwd  = 2, ylab = 'agent action / user feedback', xlab = 'days in year',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
#lines(actual, col="red")
lines(pred, col="blue", lty = 2, cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
legend("bottomleft", legend=c("Actual user response", "Learned agent response"),
       col=c("black", "blue"), lty=1:2, cex=1.25,
       box.lty=0)
length(actual)
hist(prefPred, data=prefPred )
pred

length(which(ifelse(prefActual == 2 | prefActual == 3, TRUE, FALSE)))
length(which(prefPred > 25, TRUE, FALSE))

cor(pred, actual)

nonPrefActual = mailingListData[1,]
nonPrefPred = qValues[,1]

summary(nonPrefActual)
summary(nonPrefPred)
nonPPred <- ifelse(nonPrefPred > 25, 1, 0)
nonPActual <- ifelse(nonPrefActual == 2 | nonPrefActual == 3, 1, 0)
plot(1:365, nonPActual, col="black", type = 'l', lwd  = 2, ylab = 'agent action / user feedback', xlab = 'days in year',
     cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
lines(nonPPred, col="blue", lty = 2, cex.lab=1.25, cex.axis=1.25, cex.main=1.25, cex.sub=1.25)
legend("bottomleft", legend=c("Actual user response", "Learned agent response"),
       col=c("black", "blue"), lty=1:2, cex=1.25,
       box.lty=0)
length(nonPrefActual)
hist(nonPrefPred, data=nonPrefPred )

length(which(ifelse(nonPrefActual == 2 | nonPrefActual == 3, TRUE, FALSE)))
length(which(nonPrefPred > 25, TRUE, FALSE))

cor(nonPPred, nonPrefActual)
length(ifelse(nonPrefPred > 25, 'TRUE', 'FALSE'))
length(ifelse(nonPrefActual == 2 | prefActual == 3, 'TRUE', 'FALSE'))

nonPPred
nonPActual

table(pred, actual) # Non pref
table(nonPPred, nonPActual) # pref



