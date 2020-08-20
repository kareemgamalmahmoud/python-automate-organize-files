import os, shutil

current_dir = os.path.dirname(os.path.realpath(__file__)) 

print('welcome to my script :)')

# organize images into Images folder
for filename in os.listdir(current_dir):
    if filename.endswith((".png" , ".jpg" , "jpeg" , "gif")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.copy(filename , "Images")
        os.remove(filename)
        print('images Done')

# organize code file into codes folder
    if filename.endswith((".py" , ".css" , ".html" , ".js" , "cpp")):
        if not os.path.exists("codes"):
            os.mkdir("codes")
        shutil.copy(filename , "codes")
        os.remove(filename)
        print('code files Done')      

# organize video file into video folder
    if filename.endswith((".mp4" , "wemb")):
        if not os.path.exists("videos"):
            os.mkdir("videos")
        shutil.copy(filename , "videos")
        os.remove(filename)
        print('videos Done')     

# organize docs file into documents folder
    if filename.endswith((".pdf" , ".doc" , ".txt")):
        if not os.path.exists("docs"):
            os.mkdir("docs")
        shutil.copy(filename , "docs")
        os.remove(filename)
        print('docs files Done')   

# organize apps file into apps folder
    if filename.endswith((".exe")): #(.dmg) for mac
        if not os.path.exists("apps"):
            os.mkdir("apps")
        shutil.copy(filename , "apps")
        os.remove(filename)
        print('app files Done')   

# organize archive file into archives folder
    if filename.endswith((".zip" , ".rar")): #(.dmg) for mac
        if not os.path.exists("archives"):
            os.mkdir("archives")
        shutil.copy(filename , "archives")
        os.remove(filename)
        print('archive files Done')                                   

print('Done organizing this folder')