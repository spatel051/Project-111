import random
import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("The mean of the whole dataset is " + str(population_mean))

def random_set_of_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def plot_graph(mean_list):
    new_sample_mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)

    first_std_deviation_start, first_std_deviation_end = new_sample_mean - std_deviation, new_sample_mean + std_deviation
    second_std_deviation_start, second_std_deviation_end = new_sample_mean - (2 * std_deviation), new_sample_mean + (2 * std_deviation)
    third_std_deviation_start, third_std_deviation_end = new_sample_mean - (3 * std_deviation), new_sample_mean + (3 * std_deviation)

    fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [new_sample_mean, new_sample_mean], y = [0, 0.8], mode = "lines", name = "MEAN"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.8], mode = "lines", name = "FIRST STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.8], mode = "lines", name = "FIRST STANDARD DEVIATION END"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.8], mode = "lines", name = "SECOND STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.8], mode = "lines", name = "SECOND STANDARD DEVIATION END"))
    fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0, 0.8], mode = "lines", name = "THIRD STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.8], mode = "lines", name = "THIRD STANDARD DEVIATION END"))
    fig.show()

def set_up():
    mean_list = []

    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    plot_graph(mean_list)
    
    new_sample_mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    z_score = (new_sample_mean - population_mean) / std_deviation
    print("z score = " + str(z_score))

set_up()