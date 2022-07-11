from linkedList import LinkedList

"""
Controls on a CD Player include Stop, Play, Skip, Back
"""
class CD:
	def __init__(self) -> None:
		"""Initializes an instance of CD."""
		self.tracks = LinkedList()
	
	def add_song(self, title):
		self.tracks.insert_tail(title)

class CD_Player:
	def __init__(self, cd:CD) -> None:
		"""Creates an instance of CD Player."""
		self.first = cd.tracks.head
		self.last = cd.tracks.tail
		self.curr = cd.tracks.head

	def play(self):
		"""Plays current track."""
		print(f"Play: '{self.curr}'")

	def stop(self):
		"""Stops current track."""
		print(f"Stop: '{self.curr}'")

	def skip(self):
		"""Skips to next track."""

		# If we reach end of tracks
		# then set the current track to the first.
		if self.curr.next is None:
			self.curr = self.first
		else:
			self.curr = self.curr.next

		# Play current track.
		print()
		print("Skip to next track.")
		self.play()
	
	def back(self):
		"""Skips to the previous track."""

		# If we reach start of the tracks
		# then set the current track to the last.
		if self.curr.prev is None:
			self.curr = self.last
		else: 
			self.curr = self.curr.prev

		# Play current track.
		print()
		print("Skip to previous track.")
		self.play()

# Create an instance of CD.
cd = CD()

# Add songs to CD.
cd.add_song("Blinding Lights")
cd.add_song("The Twist")
cd.add_song("Smooth")
cd.add_song("Mack The Knife")
cd.add_song("Uptown Funk")
cd.add_song("How Do I Live")
cd.add_song("Party Rock Anthem")
cd.add_song("I Gotta Feeling")
cd.add_song("Macarena")
cd.add_song("The Shape of You")

# Create an instance of CD Player.
player = CD_Player(cd)

# Play first track.
player.play()

# Skip forward 3 tracks.
player.skip() # Output: Skip to next track.
			  # 		Play: 'The Twist'
player.skip() # Output: Skip to next track.
			  # 		Play: 'Smooth'
player.skip() # Output: Skip to next track.
			  # 		Play: 'Mack The Knife'

# Skip back 4 tracks.
player.back() # Output: Skip to previous track.
			  # 		Play: 'Smooth'
player.back() # Output: Skip to previous track.
			  # 		Play: 'The Twist'
player.back() # Output: Skip to previous track.
			  # 		Play: 'Blinding Lights'
player.back() # Output: Skip to previous track.
			  # 		Play: 'The Shape of You'