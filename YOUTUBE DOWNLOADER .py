import pytube,time
#import os, time, pyfiglet,sys
#os.system ('pip install sys')
#os.system('pip install pytube')
#os.system('pip install pyfiglet')
#os.system ('pip install os')
#os.system ('pip install time')
#time.sleep (2)
'''os.system ('clear')
time.sleep (3)
print ('\033[;092m')
c=('\033[;092m××××××××××××××××××××××××××××××××××××')
for I in c+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.020)
print ()
d =('\033[;092m#####Welcome To AbdullahScript#####')
for I in d +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.10)
print ()
p=('\033[;092m##### Script youtube downloader###')
for I in p+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.10)
print ()
u=('\033[;092m### Designed By Abdullah Salah###')
for I in u+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.10)
print ()
print ('\033[;092m')

i=''\033[;092m Telegram channel : 

  ◇ http://t.me/Techno0099
            

Youttube channel  : 

 ◇ https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg '
for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
h=pyfiglet.figlet_format ('YOUTUBE VID DOWNLOADER')
for I in h+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.0050)
print ()'''
while True :
    print ('\033[;092m')
    url=input ('Enter The Video Link > :  ')
    print ()
    time.sleep (1)
    print ('\033[;093mloading please wait...')
    print ()
    t=pytube.YouTube(url).streams.                                           get_highest_resolution().download('/storage/emulated/0/Video Script Downloading')
    if True :
    
        time.sleep (3)
        print ('\033[;096mDone Downloading')


