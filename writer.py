import csv

from songs_dataset import SongsDataset


def write_songs_categorical_statistics(songs_dataset: SongsDataset, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Atributo_pavadinimas', 'Kiekis', 'Trukstamos_reiksmes', 'Kardinalumas', 'Moda', 'Modos_daznumas',
                      'Modos_procentine_reiksme',
                      'Moda2', 'Modos2_daznumas', 'Modos2_procentine_reiksme']
        data_column_names = ['track', 'artist', 'uri']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for column_name in data_column_names:
            writer.writerow({'Atributo_pavadinimas': column_name, 'Kiekis': songs_dataset.attribute_count(column_name),
                             'Trukstamos_reiksmes': songs_dataset.attribute_missing_percentage(column_name),
                             'Kardinalumas': songs_dataset.attribute_cardinality(column_name),
                             'Moda': songs_dataset.attribute_mode(column_name),
                             'Modos_daznumas': songs_dataset.attribute_mode_count(column_name),
                             'Modos_procentine_reiksme': songs_dataset.attribute_mode_percentage(column_name),
                             'Moda2': songs_dataset.attribute_mode_2(column_name),
                             'Modos2_daznumas': songs_dataset.attribute_mode_count_2(column_name),
                             'Modos2_procentine_reiksme': songs_dataset.attribute_mode_percentage_2(column_name)})


def write_songs_numerical_statistics(songs_dataset: SongsDataset, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Atributo_pavadinimas', 'Kiekis', 'Trukstamos_reiksmes', 'Kardinalumas', 'Minimali_reiksme',
                      'Maksimali_reiksme', 'Pirmas_kvantilis', 'Trecias_kvantilis', 'Vidurkis', 'Mediana',
                      'Standartinis_nuokrypis']
        data_column_names = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                             'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                             'chorus_hit', 'sections', 'target']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for column_name in data_column_names:
            writer.writerow({'Atributo_pavadinimas': column_name, 'Kiekis': songs_dataset.attribute_count(column_name),
                             'Trukstamos_reiksmes': songs_dataset.attribute_missing_percentage(column_name),
                             'Kardinalumas': songs_dataset.attribute_cardinality(column_name),
                             'Minimali_reiksme': songs_dataset.attribute_minimum_value(column_name),
                             'Maksimali_reiksme': songs_dataset.attribute_maximum_value(column_name),
                             'Pirmas_kvantilis': songs_dataset.attribute_first_quantile(column_name),
                             'Trecias_kvantilis': songs_dataset.attribute_third_quantile(column_name),
                             'Vidurkis': songs_dataset.attribute_average(column_name),
                             'Mediana': songs_dataset.attribute_median(column_name),
                             'Standartinis_nuokrypis': songs_dataset.attribute_standard_deviation(column_name)})
