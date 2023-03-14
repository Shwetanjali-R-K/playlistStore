Detailed explanation of the code:
The RecentlyPlayedStore class is the main class. It has two methods: add_song and get_recently_played_songs.

The __init__ method initializes the store with a capacity and creates an empty dictionary to store the user as the key and a list of recently played songs as the value.

The add_song method adds a song to the list of recently played songs for a given user. If the user is not in the store, a new list is created for that user. The song is added to the front of the list using the insert(0, song) method. If the length of the list exceeds the capacity, the least recently played song is removed from the end of the list using the pop() method. Here front means the index[0] of list so at this position of list we place the most recently played song. Pop method removes the song from last position of list.

The get_recently_played_songs method returns the list of recently played songs for a given user. If the user is not in the store, an empty list is returned. 

Please refer the test cases to validate code,
Output of the test cases are as follows,
Output of TestCase-1:
Playlist of User1: ['song4', 'song3', 'song2']

Output of TestCase-2:
Playlist of User2: ['song1', 'song4', 'song1']
