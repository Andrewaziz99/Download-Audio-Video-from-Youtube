import os
from pytube import YouTube
print('\nYoutube Audio/Video Downloader. script by ©Andrew Aziz\n')
print('--------------------------------------------------------\n')

link = input('Paste link here: ')
yt = YouTube(link)

print('\nchoose format:\n1:Audio [m4a]\n2:Video [mp4]')
choice = input('\nselected format: ')

if choice == '1':

    outloc = input('\nEnter the download path: ')

    video = yt.streams.filter(only_audio=True).first()

    try:
        out_file = video.download(outloc)

        base, ext = os.path.splitext(out_file)

        rename = input("\nDo you want to rename the file? (Y/N)")
        if rename.upper() == 'Y' :
            base1 = input('\nName: ')
            new_file = base1 + '.m4a'
            os.rename(out_file, new_file)
        else :
              new_file = base + '.m4a'
              os.rename(out_file, new_file)


        print("\nAudio Downloaded Successfully\n")

    except Exception as e:
        print("\nAudio Downloaded Unsuccessfully\n")
        print(e)

else:
    try:
        Video = YouTube(link)

        outloc = input('\nEnter the download path: ')

        # filters = Video.streams.filter(progressive=True, file_extension='mp4').get_by_itag(22)

        # download the highest quality video
        # filters.get_highest_resolution().download(outloc)

        # stream = Video.streams.first()
        # stream.download()

        # out_file = Video.streams.get_highest_resolution()
        # print(f'Found stream:\nNAME: {out_file.title}\nRES: {out_file.resolution}\nFPS: {out_file.fps}\nTYPE: {out_file.subtype}')
        # print('Starting to download, please wait...')
        # r = out_file.download()
        # print('File saved: ', r)

        out_file = Video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(outloc)

        base, ext = os.path.splitext(out_file)
        rename = input("\nDo you want to rename the file? (Y/N)")
        if rename.upper() == 'Y' :
            base1 = input('\nName: ')
            new_file = base1 + '.mp4'
            os.rename(out_file, new_file)
        else :
              new_file = base + '.mp4'
              os.rename(out_file, new_file)  

        print("\nVideo Downloaded Successfully\n")

    except Exception as e:
        print('\nVideo Downloaded Unsuccessfully')
        print(e)

