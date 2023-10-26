import os
import pytube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    filename = video.title + '.mp4'
    i = 1
    while os.path.exists(filename):
        filename = video.title + ' (' + str(i) + ')' + '.mp4'
        i += 1
    video.download(filename=filename)

def verify_youtube_url(url):
    try:
        youtube = pytube.YouTube(url)
        return True
    except:
        return False

url = input('Enter a YouTube video URL: ')
while not verify_youtube_url(url):
    print('The YouTube URL is invalid.')
    url = input('Enter a YouTube video URL: ')

download_video(url)
