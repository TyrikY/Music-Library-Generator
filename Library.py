import MLG_44.txt

file_list = drive.ListFile({'q': "title='MLG_44.txt'"}).GetList()
if len(file_list) == 0:
    print("File 'MLG_44.txt' not found.")
else:
    file = file_list[0]
    file.GetContentFile('MLG_44.txt')

music_library = []
with open('MLG_44.txt', 'r') as file:
    for line in file:
        track_data = line.strip().split(', ')
        track = {
            "Title": track_data[0],
            "Artist": track_data[1],
            "Album": track_data[2],
            "Genre": track_data[3],
            "Duration": track_data[4]
        }
        music_library.append(track)

print("Music Library:")
for track in music_library:
    print(f"Title: {track['Title']}, Artist: {track['Artist']}, Album: {track['Album']}, Genre: {track['Genre']}, Duration: {track['Duration']}")

def search_library(library, criteria):
    results = []
    for track in library:
        match = True
        for key, value in criteria.items():
            if track.get(key, '').lower() != value.lower():
                match = False
                break
        if match:
            results.append(track)
    return results

def generate_report(library):
    genres = {}
    artists = {}
    total_duration = 0
    for track in library:
        artist = track['Artist']
        genre = track['Genre']
        duration = track['Duration']
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1
        if artist in artists:
            artists[artist] += 1
        else:
            artists[artist] = 1
        total_duration += int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    print("\nLibrary Report:")
    print(f"Total Tracks: {len(library)}")
    print("Genres:")
    for genre, count in sorted(genres.items(), key=lambda x: x[1], reverse=True):
        print(f"{genre}: {count}")
    print("\nTop Artists:")
    for artist, count in sorted(artists.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{artist}: {count}")
    print(f"\nTotal Duartion: {total_duration // 60} minutes {total_duration % 60} seconds")

search_criteria = {'Genre': 'Hip-Hop/Rap'}
hip_hop_tracks = search_library(music_library, search_criteria)
print("\nHip-Hop/Rap Tracks:")
for track in hip_hop_tracks:
    print(f"Title: {track['Title']}, Artist: {track['Artist']}, Album: {track['Album']}, Genre: {track['Genre']}, Duration: {track['Duration']}")

generate_report(music_library)
