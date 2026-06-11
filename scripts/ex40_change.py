class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

print(__name__)
# when I execute the python script
# __name__ will be __main__

# When I import the __name__ will be 
# name of the module / script
if __name__ == "__main__":
    # all the declaration should be 
    # below the above If statement
    happy_bday = Song(["Happy Birthday to you",
                   "I don't want to get sued ",
                   "So I'll stop right there"])

    bulls_on_parade = Song(["They rally around tha family,"
                        "With pockets full of shells"])
    print(__name__)
    
    happy_bday.sing_me_a_song()

    bulls_on_parade.sing_me_a_song()
        