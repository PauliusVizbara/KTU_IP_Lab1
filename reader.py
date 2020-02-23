from song import Song
import csv


def read_songs_data(filename):
    songs = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for song in reader:
            songs.append(
                Song(song['track'], song['artist'], song['uri'], float(song['danceability']), float(song['energy']),
                     int(song['key']),
                     float(song['loudness']), int(song['mode']), float(song['speechiness']),
                     float(song["acousticness"]), float(song['instrumentalness']), float(song['liveness']),
                     float(song['valence']), float(song['tempo']), float(song['duration_ms']), float(song['time_signature']),
                     float(song['chorus_hit']), int(song['sections']), int(song['target'])))
    return songs
