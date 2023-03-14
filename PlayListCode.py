#creating a class named RecentlyPlayedStore this class further has three main methods which operates 

#the playlist generation

class RecentlyPlayedStore:

    def __init__(self, capacity):

        self.capacity = capacity

        self.store = {}

    def add_song(self, user, song):

        if user not in self.store:

            self.store[user] = []

        self.store[user].insert(0, song)

        if len(self.store[user]) > self.capacity:

            self.store[user].pop()

    def get_recently_played_songs(self, user):

        if user not in self.store:

            return []

        return self.store[user]

#creating a new RecentlyPlayedStore with capacity of 3 songs

store = RecentlyPlayedStore(3)

#TestCase-1

#adding 4 songs for user1

store.add_song("user1", "song1")

store.add_song("user1", "song2")

store.add_song("user1", "song3")

store.add_song("user1", "song4")

#calling the get_recently_played_Songs method to print the playList for user1

recent_songs_user1 = store.get_recently_played_songs("user1")

#Most recently played song will be at the starting of list

print("Playlist of User1:", recent_songs_user1)

#TestCase-2

#adding 4 songs for user2

store.add_song("user2", "song1")

store.add_song("user2", "song1")

store.add_song("user2", "song4")

store.add_song("user2", "song1")

#calling the get_recently_played_Songs method to print the playList for user2

recent_songs_user2 = store.get_recently_played_songs("user2")

#Most recently played song will be at the starting of list

print("Playlist of User2:", recent_songs_user2)
