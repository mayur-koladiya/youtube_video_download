#get video quality  information

from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=tXOIvjbNhts')
video.streams.all()
stream = video.streams.all()
for i in stream:
  print(i)
