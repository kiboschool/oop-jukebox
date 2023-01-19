class Jukebox:
    def __init__(self, songs):
        self.songs = songs
        self.current_song = 0
        self.status = 'paused'

    def play(self):
        self.status = 'playing'

    def pause(self):
        self.status = 'paused'

    def next(self):
        self.current_song += 1
        if self.current_song >= len(self.songs):
            self.current_song = 0

    def previous(self):
        self.current_song -= 1
        if self.current_song < 0:
            self.current_song = len(self.songs) - 1

    def current_state(self):
        if self.status == 'paused':
            return "Paused"
        if self.status == 'playing':
            return "Playing: " + self.songs[self.current_song]
