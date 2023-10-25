import os
import pytube
import unittest
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()

class TestVideoDownload(unittest.TestCase):
    def test_video_download(self):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        download_video(url)
        self.assertTrue(os.path.exists('Rick Astley - Never Gonna Give You Up (Video).mp4'))

if __name__ == '__main__':
    url = input('Enter a YouTube video URL: ')
    download_video(url)
    TestVideoDownload().test_video_download()
