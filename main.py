from songs_dataset import SongsDataset
from reader import read_songs_data
from writer import write_songs_categorical_statistics, write_songs_numerical_statistics
from plotter import *

songs = read_songs_data("data/dataset-of-10s.csv")

songs_dataset = SongsDataset(songs)

write_songs_categorical_statistics(songs_dataset, "categorical_statistics.csv")
write_songs_numerical_statistics(songs_dataset, "numerical_statistics.csv")
#plot_numerical_histograms(songs_dataset)
plot_scatters(songs_dataset)
#plot_scatter_matrix(songs_dataset)
#plot_categorical_histograms(songs_dataset)