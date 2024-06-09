class Song:
    pass

    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



thriller = Song("Thriller", "Michael Jackson", "Pop")
print(thriller.name, thriller.artist, thriller.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

thats_life = Song("That's Life", "Frank Sinatra", "Classic Pop")
print(thats_life.name, thats_life.artist, thats_life.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

mobb = Song("Shook Ones, Pt. II", "Mobb Deep", "Rap")
print(mobb.name, mobb.artist, mobb.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

f_sinatra = Song("Sway", "Frank Sinatra", "Classic Pop")
print(f_sinatra.name, f_sinatra.artist, f_sinatra.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

shusho = Song("Mtetezi", "Christina Shusho", "Gospel")
print(shusho.name, shusho.artist, shusho.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

kool = Song("Fresh", "Kool & The Gang", "Soul")
print(kool.name, kool.artist, kool.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

perry = Song("Killing Me Softly With Her Song", "Perry Como", "Vocal Pop")
print(perry.name, perry.artist, perry.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

cohen = Song("Dance Me to the End of Love", "Leonard Cohen", "Folk")
print(cohen.name, cohen.artist, cohen.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

castro = Song("I'll Play the Blues for You", "Daniel Castro", "Jazz")
print(castro.name, castro.artist, castro.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)

sade = Song("Smooth Operator", "Sade", "Jazz")
print(sade.name, sade.artist, sade.genre)
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)








        


