import unittest
from gradescope_utils.autograder_utils.decorators import weight
from jukebox import Jukebox

songs = ["Kuna Kuna", "Herawa Ni", "Inauma", "Vaida", "Sasa Hivi", "McMca", "Dai Dai", "Woman", "Mbona", "Toto", "Kanairo dating", "Wanjapi"] 

class TestJukebox(unittest.TestCase):
    @weight(1)
    def test_init_paused(self):
        player = Jukebox(songs)
        assert player.current_state() == "Paused"

    @weight(2)
    def test_play(self):
        player = Jukebox(songs)
        player.play()
        assert player.current_state() == "Playing: Kuna Kuna"

    @weight(1)
    def test_pause(self):
        player = Jukebox(songs)
        player.play()
        player.pause()
        assert player.current_state() == "Paused"

    @weight(1)
    def test_next(self):
        player = Jukebox(songs)
        player.play()
        player.next()
        assert player.current_state() == "Playing: Herawa Ni"

    @weight(2)
    def test_previous_wrap(self):
        player = Jukebox(songs)
        player.play()
        player.previous()
        assert player.current_state() == "Playing: Wanjapi"

    @weight(2)
    def test_next_next_prev(self):
        player = Jukebox(songs)
        player.play()
        player.next()
        player.next()
        player.previous()
        assert player.current_state() == "Playing: Herawa Ni"

    @weight(3)
    def test_next_wrap(self):
        player = Jukebox(songs)
        player.play()
        for i in range(len(songs)):
            player.next()
        player.next()
        assert player.current_state() == "Playing: Herawa Ni"

if __name__ == "__main__":
    unittest.main()
