# Object-Oriented Jukebox

In this project, you'll write a class to represent a Jukebox.

You'll practice using Python class syntax and managing state.

## Intro

A Jukebox is an old music player (see https://en.wikipedia.org/wiki/Jukebox).
In the time before mp3 players or smartphones, bars and restaurants would have a
music player that allowed minimal song selection.

In this project, you'll build the song management logic for a Jukebox with a
text interface (no audio for now). Instead of mp3 files, songs will just be
strings.

## Note

This project is not much code, but the code has to meet the requirements
_exactly_. Pay close attention to the names of the class and methods, and make
sure that the behavior is _exactly_ what is specified here.

## Requirements

In `jukebox.py`, write a `Jukebox` class that meets the following requirements.

A Jukebox needs to keep track of the following data:
- _The Song list_: a list of strings for the song titles
- _The Current song_: the index of the currently playing song
- _The Status_: is the jukebox currently playing or paused

You can name the data variables any names you want. The interface that will be
    tested is the methods.

A Jukebox should have the following methods:
- `play`: start playing the Jukebox
- `pause`: pause the Jukebox
- `next`: go to the next song
- `previous`: go to the previous song
- `current_state`: return a message indicating whether the jukebox is playing or
  paused. If it's playing, it should also return the current song that's playing.
  - If paused: return `"Paused"`
  - If playing: return `"Playing: [Song name]"` with the name of the current song

**Further Specifications**
- The jukebox should receive a list of songs (strings) when initialized
- The jukebox should start out paused
- The jukebox should stay paused until `play` is called.
- When `play` is called, the jukebox should continue playing until `pause` is
    called.
- The current song should start at the first song
- The current song should always be one of the songs in the list of songs.
  - If
    the playlist is at the end when `next()` is called, the current song should 
    go back to the start of the list.
  - If the current song is at the start of the list when `previous()` is called,
      it should go 'backwards' to the end of the list
- You are welcome to write any helper functions that would be helpful to you

## Rubric

We will be using Gradescope's autograding feature for this project. If your code
passes the unit tests, you will get most of the points for this project. We will
also award some credit for the organization and style of the code in your
solution.

## Testing

Run the unit tests with `python -m unittest` or `pytest`.

You can inspect or run `main.py` to see an interactive use of the Jukebox class.

A working sample run of `main.py` has this output:

```
❯ python main.py
Paused
Playing: Kuna Kuna
Playing: Inauma
Paused
Playing: Vaida
Playing: Sasa Hivi
Playing: McMca
Playing: Dai Dai
Playing: Woman
Playing: Mbona
Playing: Toto
Playing: Kanairo dating
Playing: Wanjapi
Playing: Kuna Kuna
Playing: Kuna Kuna
Playing: Wanjapi
Playing: Kanairo dating
Playing: Toto
Playing: Mbona
Playing: Woman
```
