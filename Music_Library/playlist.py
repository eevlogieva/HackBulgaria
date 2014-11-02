from song import Song
import time
import json


class Playlist:
    LOW_BITRATE = 64

    @staticmethod
    def load(file_name):
        file = open(file_name, "r")
        new_playlist = json.loads(file.read())
        my_playlist = Playlist(new_playlist["name"])
        for index, song in enumerate(new_playlist["songs"]):
            my_playlist.add_song(Song(
                song["title"],
                song["artist"],
                song["album"],
                song["length"],
                song["bitrate"]))
            my_playlist.songs[index].rate(song["rating"])
        file.close()
        return my_playlist

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        songs_to_remove = []
        for song in self.songs:
            if song.title == song_name:
                songs_to_remove.append(song)
        for item in songs_to_remove:
            self.songs.remove(item)

    def length(self):
        length = 0
        for song in self.songs:
            length += song.length
        return length

    def remove_disrated(self, rate):
        songs_to_be_removed = []
        for song in self.songs:
            if song.rating < rate:
                songs_to_be_removed.append(song)
        for song in songs_to_be_removed:
            self.songs.remove(song)

    def remove_bad_quality(self):
        songs_to_be_removed = []
        for song in self.songs:
            if song.bitrate < self.LOW_BITRATE:
                songs_to_be_removed.append(song)
        for song in songs_to_be_removed:
            self.songs.remove(song)

    def show_artists(self):
        artists = []
        for song in self.songs:
            artists.append(song.artist)
        return set(artists)

    def __str__(self):
        string = ""
        for song in self.songs:
            format_time = time.strftime("%M:%S", time.gmtime(song.length))
            string += "{} {} - {}".format(song.artist, song.title, format_time)
            string += "\n"
        return string

    def hash_songs(self):
        hashed_songs = []
        for song in self.songs:
            hashed_songs.append(song.hash_song())
        return hashed_songs

    def hash_playlist(self):
        hash_playlist = {}
        hash_playlist["name"] = self.name
        hash_playlist["songs"] = self.hash_songs()
        return hash_playlist

    def save(self, file_name):
        file = open(file_name, "w")
        file.write(json.dumps(self.hash_playlist()))
        file.close()


def main():
    my_playlist = Playlist("AC/DC Playlist")
    my_playlist.add_song(Song("HEll", "AC/DC", "One", 300, 256))
    my_playlist.songs[0].rate(3)
    my_playlist.add_song(Song("Heaven", "AC/DC", "One", 280, 128))
    my_playlist.songs[1].rate(2)
    my_playlist.save("test.json")
    my_playlist2 = Playlist.load("test.json")

if __name__ == '__main__':
    main()
