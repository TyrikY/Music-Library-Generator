# Music-Library-Generator
The goal of this project is to develop a program that allows users to effeciently mangage a digital music library stored in a text file. The program provides features for adding, removing, and updating music tracks, as well as searching and generating reports on the library.

# Structure
The music library data will be stored in a text file, with each track represented by a line containing the track information (title, artist, album, genre, duration) separted by a comma. In the program, I used a list of dictionaries to represent the music tracks, where each dictionary contains the track data.

# Program Functionality
  1. Add Track: Allow user to add a new track to the library by providing necessary information
  2. Remove Track: Allow users to remove an existing track from the library by specifying the track title or others relevant information.
  3. Update Track: Allow users to update the information of an exsiting track in the library.
  4. Search Library: Allow users to search the library based on various criteria. The program should display the matching tracks.
  5. Generate Reports: The program should be able to generate reports on the library, such as:
    - Total number of tracks
    - Number of tracks pr genre
    - Top artists
    - Total duration of the library
  6. Load/Save Library: The program should be able to load the music library data from the text file when it starts and save any changes made to the library back to the file when the program exits.


