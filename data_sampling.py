import statistics
import csv
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()
print(statistics.mean(data))
def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def showFigure(mean_list):
    df = mean_list
    fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = randomSetOfMean(10)
        mean_list.append(set_of_means)

    showFigure(mean_list)
    print(statistics.mean(mean_list))

setup()