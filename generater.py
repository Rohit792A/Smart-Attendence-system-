from MyQR import myqr
import os

#create a text file and fill the information line by line
#create and read the text file
f=open("data.txt",'r')
lines = f.read().split("\n")
print (lines)


# using for loop for generating multiple qr codes
for i in range(0,len(lines)):
    data=lines[i]
    name=data
    print(name)#data is used to encode lines

#following are requirements for using base64

    version, level, qr_name = myqr.run(
    str(name),
    version = 1,
    level = 'H',

    #background for QR-code
    #you can use any picture in the background including gif
    picture = 'a.jpg',  #select picture you want to use
    colorized = True,    #select if you want colour or not
    contrast = 1.0,
    brightness = 1.0,
    save_name = str(lines[i]+'.bmp'),  #concatenate name and the file type of qr , this is file name
    save_dir = os.getcwd()           #save this file  in the directory we are using
    )
