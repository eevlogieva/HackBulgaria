class Song():
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = 3
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if rating < Song.MIN_RATING or rating > Song.MAX_RATING:
            error_message = "Rating must be from {} to {}"
            raise ValueError(error_message.format(Song.MIN_RATING, Song.MAX_RATING))
        else:
            self.rating = rating

    def hash_song(self):
        hashed_song = {}
        hashed_song["title"] = self.title
        hashed_song["artist"] = self.artist
        hashed_song["album"] = self.album
        hashed_song["length"] = self.length
        hashed_song["rating"] = self.rating
        hashed_song["bitrate"] = self.bitrate
        return hashed_song
