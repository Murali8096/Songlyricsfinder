import lyricsgenius
api_key = "tG7q62RrdpheZsC3nfGqGOdJKGPzb3Z7iLDl8hdPe7GMxNK1FXW_qM60fEUvwCMP"
genius =  lyricsgenius.Genius(api_key)
name = input("Enter Artist Name : ")
artist = genius.search_artist(name)
song = input("Type your song for Lyrics : ")
song = artist.song(song)
print(song.lyrics)
