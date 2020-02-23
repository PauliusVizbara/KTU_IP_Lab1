import statistics


class SongsDataset:

    def __init__(self, songs):
        self.songs = songs

    # Bendri
    def attribute_count(self, index):
        count = 0
        for song in self.songs:
            if song.__getattribute__(index):
                count += 1
        return count

    def attribute_missing_percentage(self, index):
        return 100 - (self.attribute_count(index) / len(self.songs)) * 100

    def attribute_cardinality(self, index):
        attributes = []
        for song in self.songs:
            attributes.append(song.__getattribute__(index))
        return len(set(attributes))

    # Tolydinio tipo

    def attribute_minimum_value(self, index):
        attributes = []
        for song in self.songs:
            attributes.append(song.__getattribute__(index))
        return min(attributes)

    def attribute_maximum_value(self, index):
        attributes = []
        for song in self.songs:
            attributes.append(song.__getattribute__(index))
        return max(attributes)

    def attribute_first_quantile(self, index):
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))
        attributes.sort()
        return statistics.median(attributes[:len(attributes) // 2])

    def attribute_third_quantile(self, index):
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))
        attributes.sort()
        return statistics.median(attributes[len(attributes) // 2:])

    def attribute_average(self, index):
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))
        return sum(attributes) / len(attributes)

    def attribute_median(self, index):
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))
        return statistics.median(attributes)

    def attribute_standard_deviation(self, index):
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))
        return statistics.stdev(attributes)

    # Kategorinio tipo

    def attribute_mode(self, index):
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))
        return statistics.mode(attributes)

    def attribute_mode_count(self, index):
        mode = self.attribute_mode(index)
        count = 0
        for song in self.songs:
            if song.__getattribute__(index) == mode:
                count += 1
        return count

    def attribute_mode_percentage(self, index):
        return self.attribute_mode_count(index) / self.attribute_count(index) * 100

    def attribute_mode_2(self, index):
        mode = self.attribute_mode(index)
        attributes = []
        for song in self.songs:
            if song.__getattribute__(index):
                attributes.append(song.__getattribute__(index))

        attributes_2 = []

        for entry in attributes:
            if entry != mode:
                attributes_2.append(entry)

        return statistics.mode(attributes_2)

    def attribute_mode_count_2(self, index):
        mode = self.attribute_mode_2(index)
        count = 0
        for song in self.songs:
            if song.__getattribute__(index) == mode:
                count += 1
        return count

    def attribute_mode_percentage_2(self, index):
        return self.attribute_mode_count_2(index) / len(self.songs) * 100