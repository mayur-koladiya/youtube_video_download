import pytube
video_url = 'https://www.youtube.com/watch?v=tXOIvjbNhts' # copy and paste url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:/Users/Jay Swaminarayan/.spyder-py3') 

# download with specific format


#from pytube import YouTube
#video = YouTube('https://www.youtube.com/watch?v=PxrnoGyBw4E')

#video.streams.get_by_itag(140).download('C:/Users/Jay Swaminarayan/.spyder-py3') 
#print(video.title)

