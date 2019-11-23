library(stringr)
library(dplyr)
dump = read.csv("bandwidth-fluctuation.csv")
dump = dump %>% select(2,7) %>% 
  filter(str_detect(Info, regex("/outputfile(\\d+)")))
dump$res = as.numeric(str_match(dump$Info, "/outputfile(\\d+)")[,2])
head(dump)

library(ggplot2)
# Basic line plot with points
ggplot(data=dump, aes(x=c(1:length(dump$Time)), y=res, group=1)) +
  scale_y_continuous(name="Resolution", breaks=c(360,540,720,1080)) +
  scale_x_continuous(name="Time") + 
  geom_line(color="black", size=0.5, alpha=0.9, linetype=1) +
  geom_point(color="blue", size=1) + 
  ggtitle("Bandwidth fluctuation") + 
  theme(panel.grid.minor = element_blank())

