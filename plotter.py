import matplotlib.pyplot as plt
import numpy as np
from songs_dataset import SongsDataset
from pandas.plotting import scatter_matrix
import pandas as pd


def plot_scatters(songs_dataset: SongsDataset):
    data_column_names = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                         'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                         'chorus_hit', 'sections', 'target']
    for column_name1 in data_column_names:
        for column_name2 in data_column_names:
            plot_scatter(songs_dataset, column_name1, column_name2)


def plot_numerical_histograms(songs_dataset: SongsDataset):
    data_column_names = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                         'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                         'chorus_hit', 'sections', 'target']

    for column_name in data_column_names:
        plot_histogram(songs_dataset, column_name)


def plot_categorical_histograms(songs_dataset: SongsDataset):
    artists = set([song.artist for song in songs_dataset.songs[:20]])

    target_amount = []

    for artist in artists:
        count = 0
        for song in songs_dataset.songs:
            if song.artist == artist:
                count += 1
        target_amount.append(count)

    df = pd.DataFrame({'artists': artists, 'target_songs': target_amount})
    ax = df.plot.bar(x='artists', y='target_songs', rot=0)
    plt.show()


def plot_histogram(songs_dataet: SongsDataset, column_name):
    attributes = []
    for song in songs_dataet.songs:
        attributes.append(song.__getattribute__(column_name))
    print(attributes)
    plt.figure(column_name)
    plt.hist(attributes)
    plt.show()


def plot_scatter(songs_dataset: SongsDataset, x_column_name, y_column_name):
    plt.title("Scatter Plot: " + x_column_name + " " + y_column_name)
    x_axis = []
    for song in songs_dataset.songs:
        x_axis.append(song.__getattribute__(x_column_name))
    y_axis = []
    for song in songs_dataset.songs:
        y_axis.append(song.__getattribute__(y_column_name))

    z = np.polyfit(x_axis, y_axis, 1)
    p = np.poly1d(z)

    plt.plot(x_axis, p(x_axis), "r--")

    plt.scatter(x_axis, y_axis)
    plt.xlabel(x_column_name, fontsize=14)
    plt.ylabel(y_column_name, fontsize=14)
    plt.legend()
    plt.show()

def plot_scatter_matrix(songs_dataset: SongsDataset):
    data_column_names = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                         'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                         'chorus_hit', 'sections', 'target']

    songs = songs_dataset.songs

    df = pd.DataFrame({'danceability': [song.danceability for song in songs],
                       'energy': [song.energy for song in songs],
                       'key': [song.key for song in songs],
                       'loudness': [song.loudness for song in songs],
                       'mode': [song.mode for song in songs],
                       'acousticness': [song.acousticness for song in songs],
                       'instrumentalness': [song.instrumentalness for song in songs],
                       'liveness': [song.liveness for song in songs],
                       'valence': [song.valence for song in songs],
                       'tempo': [song.tempo for song in songs],
                       'duration_ms': [song.duration_ms for song in songs],
                       'time_signature': [song.time_signature for song in songs],
                       'chorus_hit': [song.chorus_hit for song in songs],
                       'sections': [song.sections for song in songs],
                       'target': [song.target for song in songs],
                       'speechiness': [song.speechiness for song in songs]}, columns=data_column_names)
    scatter_matrix(df, alpha=0.2)

    plt.show()
