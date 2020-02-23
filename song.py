class Song:

    def __init__(self, track, artist, uri, danceability, energy, key, loudness, mode, speechiness, acousticness,
                 instrumentalness, liveness, valence, tempo, duration_ms, time_signature, chorus_hit, sections, target):
        self.track = track
        self.artist = artist
        self.uri = uri
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.time_signature = time_signature
        self.chorus_hit = chorus_hit
        self.sections = sections
        self.target = target
