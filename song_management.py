
# ==========================================
# SONG MANAGEMENT
# ==========================================

SONG_FILE = "songs.txt"
PLAYLIST_FILE = "playlists.txt"
LISTENING_FILE = "listening.txt"


# Read all song records
def read_songs():
    songs = []

    try:
        with open(SONG_FILE, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 5:
                    songs.append(data)

    except FileNotFoundError:
        pass

    return songs


# Save all song records
def save_songs(songs):
    with open(SONG_FILE, "w") as file:
        for song in songs:
            file.write("|".join(song) + "\n")


# Check whether playlist ID exists
def playlist_exists(playlist_id):
    try:
        with open(PLAYLIST_FILE, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 3 and data[0] == playlist_id:
                    return True

    except FileNotFoundError:
        print("[Error] Playlist file not found.")

    return False


# Validate song information
def validate_song(title, artist, genre):
    if not title or not artist or not genre:
        print("[Error] Song details cannot be empty.")
        return False

    if any("|" in value for value in [title, artist, genre]):
        print("[Error] The character | is not allowed.")
        return False

    return True


# ------------------------------------------
# FUNCTION 1: ADD NEW SONG
# ------------------------------------------

def add_song():

    print("\n===== ADD NEW SONG =====")

    songs = read_songs()

    song_id = input("Song ID: ").strip()

    # Check empty Song ID
    if not song_id or "|" in song_id:
        print("[Error] Invalid Song ID.")
        return

    # Prevent duplicate Song ID
    for song in songs:
        if song[0] == song_id:
            print("[Error] Song ID already exists!")
            return

    title = input("Title: ").strip()
    artist = input("Artist: ").strip()
    genre = input("Genre: ").strip()
    playlist_id = input("Playlist ID: ").strip()

    # Validate song details
    if not validate_song(title, artist, genre):
        return

    if not playlist_id or "|" in playlist_id:
        print("[Error] Invalid Playlist ID.")
        return

    # Check playlist ID
    if not playlist_exists(playlist_id):
        print("[Error] Playlist ID does not exist.")
        return

    # Create new song record
    new_song = [song_id, title, artist, genre, playlist_id]

    songs.append(new_song)

    try:
        # Save song into songs.txt
        save_songs(songs)

        # Create initial listening record
        with open(LISTENING_FILE, "a") as file:
            file.write(f"{song_id}|0|0\n")

        print(f"\nSong {song_id} added successfully!")
        print("Initial play count: 0")
        print("Initial rating: 0")

    except OSError:
        print("[Error] Unable to save song information.")


# ------------------------------------------
# FUNCTION 2: UPDATE SONG DETAILS
# ------------------------------------------

def update_song():

    print("\n===== UPDATE SONG DETAILS =====")

    songs = read_songs()

    song_id = input("Song ID to update: ").strip()

    # Find existing song
    for song in songs:

        if song[0] == song_id:

            print("\nCurrent song details:")
            print("Current title:", song[1])

            new_title = input(
                "New title (Enter to keep): "
            ).strip()

            new_artist = input(
                "New artist (Enter to keep): "
            ).strip()

            new_genre = input(
                "New genre (Enter to keep): "
            ).strip()

            new_playlist = input(
                "New playlist ID (Enter to keep): "
            ).strip()

            # Keep current information if input is empty
            updated_title = new_title if new_title else song[1]
            updated_artist = new_artist if new_artist else song[2]
            updated_genre = new_genre if new_genre else song[3]
            updated_playlist = new_playlist if new_playlist else song[4]

            # Validate updated information
            if not validate_song(
                updated_title,
                updated_artist,
                updated_genre
            ):
                return

            if "|" in updated_playlist:
                print("[Error] Invalid Playlist ID.")
                return

            # Validate playlist ID
            if not playlist_exists(updated_playlist):
                print("[Error] Playlist ID does not exist.")
                return

            # Update song information
            song[1] = updated_title
            song[2] = updated_artist
            song[3] = updated_genre
            song[4] = updated_playlist

            try:
                save_songs(songs)
                print(f"\nSong {song_id} updated successfully!")

            except OSError:
                print("[Error] Unable to update song information.")

            return

    print("[Error] Song ID not found!")


# ------------------------------------------
# FUNCTION 3: DELETE SONG
# ------------------------------------------

def delete_song():

    print("\n===== DELETE SONG =====")

    songs = read_songs()

    song_id = input("Song ID to delete: ").strip()

    # Find song using Song ID
    for song in songs:

        if song[0] == song_id:

            print(f"\nFound: {song[1]} - {song[2]}")

            confirm = input(
                "Confirm deletion (Y/N): "
            ).strip().upper()

            if confirm == "Y":

                try:
                    # Remove song from songs.txt
                    updated_songs = [
                        item for item in songs
                        if item[0] != song_id
                    ]

                    save_songs(updated_songs)

                    # Remove related listening record
                    try:
                        with open(LISTENING_FILE, "r") as file:
                            records = file.readlines()

                        with open(LISTENING_FILE, "w") as file:
                            for record in records:
                                data = record.strip().split("|")

                                if not data or data[0] != song_id:
                                    file.write(record)

                    except FileNotFoundError:
                        print("[Warning] Listening file not found.")

                    print("\nSong deleted successfully.")
                    print("Related listening record removed.")

                except OSError:
                    print("[Error] Unable to delete song.")

            elif confirm == "N":
                print("\nDeletion cancelled.")

            else:
                print("\n[Error] Please enter Y or N.")

            return

    print("[Error] Song ID not found!")


# ------------------------------------------
# SONG MANAGEMENT DISPATCHER
# ------------------------------------------

def song_management(choice):

    if choice == "1":
        add_song()

    elif choice == "2":
        update_song()

    elif choice == "3":
        delete_song()

