import os

FILENAME = "MLG_44.txt"

def load_library():
    """Load the music library from the file."""
    library = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split("], ")
                if len(parts) == 5:
                    title, artist, album, genre, duration = [part.split(": [") for part in parts]
                    track = {
                        "Title": title[0],
                        "Artist": artist[0],
                        "Album": album[0],
                        "Genre": genre[0],
                        "Duration": duration[0],
                    }
                    library.append(track)
    return library

def save_library(library):
    """Save the music library to the file."""
    with open(FILENAME, "w") as file:
        for track in library:
            file.write(f"Title: [{track['Title']}], Artist: [{track['Artist']}], Album: [{track['Album']}], Genre: [{track['Genre']}], Duration: [{track['Duration']}]\n")

def add_track(library):
    """Add a new track to the library."""
    title = input("Enter the track title: ")
    artist = input("Enter the artist name: ")
    album = input("Enter the album name: ")
    genre = input("Enter the genre: ")
    duration = input("Enter the duration (e.g., 3:42): ")
    track = {
        "Title": title,
        "Artist": artist,
        "Album": album,
        "Genre": genre,
        "Duration": duration,
    }
    library.append(track)
    print("Track added successfully.")

def remove_track(library):
    """Remove a track from the library."""
    title = input("Enter the track title to remove: ")
    for track in library:
        if track["Title"].lower() == title.lower():
            library.remove(track)
            print("Track removed successfully.")
            return
    print("Track not found.")

def update_track(library):
    """Update the information of a track in the library."""
    title = input("Enter the track title to update: ")
    for track in library:
        if track["Title"].lower() == title.lower():
            new_title = input("Enter the new title (or leave blank to keep current): ")
            if new_title:
                track["Title"] = new_title
            new_artist = input("Enter the new artist (or leave blank to keep current): ")
            if new_artist:
                track["Artist"] = new_artist
            new_album = input("Enter the new album (or leave blank to keep current): ")
            if new_album:
                track["Album"] = new_album
            new_genre = input("Enter the new genre (or leave blank to keep current): ")
            if new_genre:
                track["Genre"] = new_genre
            new_duration = input("Enter the new duration (or leave blank to keep current): ")
            if new_duration:
                track["Duration"] = new_duration
            print("Track updated successfully.")
            return
    print("Track not found.")

def search_library(library):
    """Search the library based on various criteria."""
    search_type = input("Enter the search criteria (Title, Artist, Album, Genre, Duration): ").lower()
    search_value = input(f"Enter the {search_type} to search for: ").lower()
    matching_tracks = [track for track in library if search_value.lower() in str(track[search_type.capitalize()]).lower()]
    if matching_tracks:
        print(f"Tracks matching '{search_value}' for '{search_type}':")
        for track in matching_tracks:
            print(f"Title: [{track['Title']}], Artist: [{track['Artist']}], Album: [{track['Album']}], Genre: [{track['Genre']}], Duration: [{track['Duration']}]")
    else:
        print("No matching tracks found.")

def generate_reports(library):
    """Generate reports on the library."""
    print("Library Report:")
    print(f"Total number of tracks: {len(library)}")

    genres = set(track["Genre"] for track in library)
    print("Number of tracks per genre:")
    for genre in genres:
        count = sum(1 for track in library if track["Genre"] == genre)
        print(f"{genre}: {count}")

    artists = set(track["Artist"] for track in library)
    print("Top artists:")
    for artist in sorted(artists, key=lambda a: sum(1 for track in library if track["Artist"] == a), reverse=True):
        count = sum(1 for track in library if track["Artist"] == artist)
        print(f"{artist}: {count}")

    total_duration = sum(sum(int(d.split(":")[0]) * 60 + int(d.split(":")[1]) for d in [track["Duration"]]) for track in library)
    hours = total_duration // 3600
    minutes = (total_duration % 3600) // 60
    seconds = total_duration % 60
    print(f"Total duration of the library: {hours} hours, {minutes} minutes, {seconds} seconds")

def main():
    library = load_library()
    while True:
        print("\nMusic Library Generator")
        print("1. Add Track")
        print("2. Remove Track")
        print("3. Update Track")
        print("4. Search Library")
        print("5. Generate Reports")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_track(library)
        elif choice == "2":
            remove_track(library)
        elif choice == "3":
            update_track(library)
        elif choice == "4":
            search_library(library)
        elif choice == "5":
            generate_reports(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()