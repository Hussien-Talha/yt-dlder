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


hi = "                                                                                                                  "
first = "           /  \    /  \ ____ |  |   ____  ____   _____   ____    _/  |_  ____   _/  |_|  |__   ____ "                                      
second = "          \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \   \   __\/  _ \  \   __\  |  \_/ __ \ "                                     
third = "            \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |  | (  <_> )  |  | |   Y  \  ___/ "                                    
fourth = "            \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |__|  \____/   |__| |___|  /\___  > "
fifth = "                                                                                                               "
sixth = "                     __       ___.                .___                  .__                    .___ "                                                                                                                                                                                  
seventh = "     ___.__. ____  __ ___/  |_ __ _\_ |__   ____     __| _/______  _  ______ |  |   _________     __| _/___________ "                          
eighth = "     <   |  |/  _ \|  |  \   __\  |  \ __ \_/ __ \   / __ |/  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \ "                        
ninth = "       \___  (  <_> )  |  /|  | |  |  / \_\ \  ___/  / /_/ (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/ "                   
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