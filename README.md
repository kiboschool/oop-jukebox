# Object-Oriented Jukebox

In this project, you'll write a class to represent a Jukebox.

You'll practice using Python class syntax and managing state.

## Requirements

> This project is not much code, but the code has to meet the requirements
> _exactly_. Pay close attention to the names of the class and methods, and make
> sure that the methods behavior is exactly as specified here.

A Jukebox needs to keep track of the following data:
- _The Song list_: an array of strings for the song titles
- _Current song_: the index of the currently playing song
- _Status_: is the jukebox currently playing or paused

A Jukebox should have the following methods:
- `play`: start playing the Jukebox
- `pause`: pause the Jukebox
- `next`: go to the next song
- `previous`: go to the previous song
- `current_state`: print a message indicating whether the jukebox is playing or paused. If it's playing, it should also return the current song that's playing.
  - If paused: return `"Paused"`
  - If playing: return `"Playing: [Song name]"` with the name of the current song

Notes:
- The jukebox should be initialized with an array of songs (strings)
- The jukebox should start out paused
- The current song should start at the first song
- The current song should always be one of the songs in the list of songs.
  - If
    the playlist is at the end when `next()` is called, the current song should 
    go back to the start of the list.
  - If the current song is at the start of the list when `previous()` is called,
      it should go 'backwards' to the end of the list
- You can name the data variables any names you want. The interface that will be
    tested is the methods.
- You are welcome to write any helper functions that would be helpful to you

## Testing

You can inspect or run `main.py` to see an interactive use of the Jukebox class.

Run the unit tests with `python -m unittest` or `pytest`.

## Rubric

We will be using Gradescope's autograding feature for this project. If your code
passes the unit tests, you will get most of the points for this project.

