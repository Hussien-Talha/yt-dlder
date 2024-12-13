import os
from yt_dlp import YoutubeDL

# Define the User-Agent header for yt-dlp
YDL_OPTIONS = {
    'outtmpl': '%(title)s.%(ext)s',  # Output file naming format
    'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
    'quiet': False,  # Show output in the console
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert to MP4
    }],
    'noplaylist': True,  # Download only the video, not the playlist
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    },
}

def debug_video_streams(info_dict):
    """Print available video formats for debugging."""
    for format in info_dict['formats']:
        print(f"Format: {format['format_id']} - Resolution: {format.get('resolution', 'unknown')} - Ext: {format['ext']}")

def download_video(url):
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # Extract video info without downloading
            debug_video_streams(info_dict)  # Debug available streams
            ydl.download([url])  # Download the video
            print(f"Downloaded: {info_dict['title']}.mp4")
    except Exception as e:
        print(f"An error occurred: {e}")

def verify_youtube_url(url):
    try:
        with YoutubeDL() as ydl:
            ydl.extract_info(url, download=False)
        return True
    except:
        return False

hi = "                                                                                                                  "
first = "           /  \    /  \ ____ |  |   ____  ____   _____   ____    _/  |_  ____   _/  |_|  |__   ____ "                                      
second = "          \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \   \   __\/  _ \  \   __\  |  \_/ __ \ "                                     
third = "            \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |  | (  <_> )  |  | |   Y  \  ___/ "                                    
fourth = "            \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |__|  \____/   |__| |___|  /\___  > "
fifth = "                                                                                                               "
sixth = "                     __       ___.                .___                  .__                    .___ "                                                                                                                                                                                
seventh = "     ___.__. ____  __ ___/  |_ __ _\_ |__   ____     __| _/______  _  ______ |  |   _________     __| _/___________ "                        
eighth = "     <   |  |/  _ \|  |  \   __\  |  \ __ \_/ __ \   / __ |/  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \ "                      
ninth = "       \___  (  <_> )  |  /|  | |  |  / \\\\\\ \  ___/  / /_/ (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/ "                  
tenth = "       / ____|\____/|____/ |__| |____/|___  /\___  > \____ |\____/ \/\_/|___|  /____/\____(____  )\____ |\___  >__| "                  
one = "         \/                                 \/     \/       \/                 \/                \/      \/    \/ "                                                                                                                                                                                                                                                                                       

print(repr(hi))
print(repr(hi)) 
print(repr(first))
print(repr(second))
print(repr(third)) 
print(repr(fourth))
print(repr(fifth))
print(repr(sixth))
print(repr(seventh))
print(repr(eighth))
print(repr(ninth))
print(repr(tenth))
print(repr(one))
print(repr(hi))
print(repr(hi))

url = input('Enter a YouTube video URL: ')
while not verify_youtube_url(url):
    print('The YouTube URL is invalid.')
    user_input = input('Enter "cancel" to end the script or press enter to continue: ')
    if user_input.lower() == 'cancel':
        break
download_video(url)