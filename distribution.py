import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go
result = []
for i in range(0,1000):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    result.append(d1+d2)

fig = ff.create_distplot([result],["Result"])

#1. Normal distribution is symmetric around the peak value. Bell shape

mean = statistics.mean(result)
median = statistics.median(result)
mode = statistics.mode(result)
standarddeviation = statistics.stdev(result)
print(mean)
print(median)
print(mode)
print(standarddeviation)
#2. Mean = Median = Mode in a normal distribution and corresponds to the peak value

#3.68% of all data lie within one standard deviation of the mean
#95% of all the data lie within two standard deviation of the mean
#99% of all the data lie within three standard deviation of the mean

firststdstart,firststdend = mean-standarddeviation,mean+standarddeviation
secondstdstart,secondstdend = mean-(2*standarddeviation),mean+(2*standarddeviation)
thirdstdstart,thirdstdend = mean-(3*standarddeviation),mean+(3*standarddeviation)

data1 = [i for i in result if i > firststdstart and i < firststdend]
data2 = [i for i in result if i > secondstdstart and i < secondstdend]
data3 = [i for i in result if i > thirdstdstart and i < thirdstdend]
print(len(data1)*100/len(result))
print(len(data2)*100/len(result))
print(len(data3)*100/len(result))

fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.18],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.18],mode = "lines",name = "standarddeviation1"))
fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.18],mode = "lines",name = "standarddeviation1"))
fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.18],mode = "lines",name = "standarddeviation2"))
fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.18],mode = "lines",name = "standarddeviation2"))
fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.18],mode = "lines",name = "standarddeviation3"))
fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.18],mode = "lines",name = "standarddeviation3"))
fig.show()