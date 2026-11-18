import sys

def song_management():
    #song managment code 

def playlist_data():
    #playlist data code 
   
def listening_activity():
    #listening activity code
    
def display_and_export():
    #display,export,documentation code

def menu():
    print("\n*** MUSIC PLAYLIST MANAGER ***")
    print("1. Add new song")
    print("2. Update song details")
    print("3. Delete a song")
    print("4. Log listening activity")
    print("5. Display playlist")
    print("6. Generate listening summary")
    print("7. Export summary to file")
    print("8. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice in ['1','2','3']:
            song_management()
        elif choice == '4':
            listening_activity()
        elif choice in ['5','6','7']:
            display_and_export()
        elif choice == '8':
            print("\nThank you for using Music Playlist Manager!\nGoodbye!!")
            sys.exit(0)
        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 8.")
            
if __name__ == "__main__":
    main()
   

