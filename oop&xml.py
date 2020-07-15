'/bin/bash'
#External Packages
import AudioFile,song
root = Tk()
import GUI


# Master music player class. Primary model backend that runs the program.

class MusicPlayer():
	_audioList = []
	_masterPlaylistName = "Main Library"

	def __init__(self):
		self._playlists = []
		self.currentPlaylist = None
		self.currentSong = None
		self.currentUser = None
		# Populate our song list for usage
		self._audioList.append(Song(None, "Darude Sandstorm", rating=2))
		self._audioList.append(Song(None, "Baby Dont Hurt Me", rating=1))
		self._audioList.append(Song(None, "I Want To Break Free", rating=4))	        
		self.newPlaylist(self._masterPlaylistName, self._audioList)
		# Start our GUI
		self.gui = Tk()

# Creates a new playlist and adds it the the master list of playlists
	def newPlaylist(self, name= None, songs= None):

		newPlaylist = Playlist(name)
		if (songs != None):
			for s in songs:
				newPlaylist.addAudio(s)
		self._playlists.append(newPlaylist)
		print("DEBUG: playlist created:" + newPlaylist.name)

    # Creates and adds a new custom song to the master playlist

	def newSong(self, response):
		if(response != None):
			newSong = Song(None, response[0])

			if (response[1] != ''):
				newSong.artist = Artist(response[1])

			if (response[2] != '' and int(response[2]) > 0 and int(response[2]) <= 5):
				newSong.rating = int(response[2])

			self.addAudioToMasterList(newSong)
			self.gui.focusMasterPlaylist()
		else:
			self.gui.displayMessage("Incorrect or Missing Song Information!")

    

# GET function to search for a playlist by name
	def getPlaylist(self, getN):
		for p in self._playlists:
			if (p.name == getN):
				return p

		raise NotFoundException("Playlist not found.")



	def getAudio(self, sName, detail = None):
		for s in self._audioList:
			if (s.name == sName):
				if (detail == None):
					return s
				elif (type(s) is Song and s.artist.name == str(detail)):
					return s
				elif (type(s) is Podcast and s.episode == int(detail)):
					return s

# Finds and deletes the passed in audio file
	def deleteAudio(self, AudioFile):
		for p in self._playlists:
			for s in p.songList:
				if (s == audio):
					p.songList.remove(s)
		self._audioList.remove(audio)
		self.gui.displayMessage("Song Deleted!")


	def addAudioToMasterList(self, AudioFile):
		self._audioList.append(audio)
		self.getPlaylist(self._masterPlaylistName).addAudio(audio)


# Saves a playlist to an XML file
	def savePlaylistXML(self):
		root = ET.Element("root")	    
		for song in self.currentPlaylist.songList:
			song.addXML(root)
		print(ET.tostring(root, encoding='utf8').decode('utf8'))
		tree = ET.ElementTree(root)
		tree.write((self.currentPlaylist.name + ".xml"))
		self.gui.displayMessage("Playlist successfully exported!")

# Loads a playlists XML file into the program
	def loadPlaylistXML(self, name):
		try:
			self.getPlaylist(name)
			self.gui.displayMessage("Playlist already created with that name.")
		except NotFoundException: 	    
			playlistTree = ET.parse(name + ".xml")
			root = playlistTree.getroot()
			newPlaylist = Playlist(name)
			for child in root:
				try: 
					song = self.getAudio(child[0].text, child[2].text)
					newPlaylist.addAudio(song)	            
				except NotFoundException: 
					song = self.newSong([child[0].text, child[2].text, child[1].text])
					self.addAudioToMasterList(song)	            
					newPlaylist.addAudio(self.getAudio(child[0].text, child[2].text))
			self._playlists.append(newPlaylist)
			print("DEBUG: playlist created:" + newPlaylist.name)
			self.gui.updatePlaylistBox()
			self.gui.displayMessage("Playlist " + name + " successfully imported!")


# CLASS PROPERTIES AND PUBLIC VARIABLES

	@property
	def playlists(self):
		return self._playlists
	@playlists.setter
	def playlists(self, playlists):
		self._playlists = playlists

	@property
	def audioList(self):
		return self._playlists
	@audioList.setter
	def audioList(self, audioList):
		self._audioList = audioList

	@property
	def masterPlaylistName(self):
		return self._masterPlaylistName
	@masterPlaylistName.setter
	def masterPlaylistName(self, masterPlaylistName):
		self._masterPlaylistName = masterPlaylistName

class Artist(object):
	def __init__(self, artist_name):
		self.name = artist_name

# Start our program
mp = MusicPlayer()

