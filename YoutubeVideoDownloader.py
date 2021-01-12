# Import Required Module
import requests
import json
from pytube import YouTube
from threading import *
from functools import partial
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox

# Threading 1
def Tkinter_Threading():
    t1=Thread(target=Video_Download)
    t1.start()

# Threading 2
def Tkinter_Threading1():
    t1=Thread(target=Video_Download1)
    t1.start()


# Downlaod youtube Video
# Required Video url and file name
def youtube_video_download(videoUrl,filename="Video"): 
    # Creating object of YouTube() 
    getVideo = YouTube(videoUrl) 
    
    # Get all available streams of video and select the first stream
    videoStream = getVideo.streams.first()
   
    # Downloading the video to destination
    videoStream.download(filename=filename)

# Video Download (call when video url is given by user)
def Video_Download():
	# Set statusbar 
    statusvar.set("Video Download Starts")

    # update variable
    sbar.update() 

    # Remove Error text
    error.config(text = "")

    # When one button is clicked another button should be disabled
    btn2["state"] = "disabled"

    # video download starts
    try:
        youtube_video_download(video_url.get())
        statusvar.set("Video Download Finished")
        
        # Messge box
        messagebox.showinfo("SUCCESSFULLY",  
                        "VIDOE SUCCESSFULLY DOWNLOADED") 

    # If video url is incorrect or internet is not connected
    # show error
    except:
        error.config(text = "Video URL is Incorrect")
        statusvar.set("Video Download Failed")

    # When video is downlaoded button is enabled
    btn2["state"] = "normal"

# Video download from API
def Video_Download1():
	# change progress bar value
    progress['value'] = 0
    root.update_idletasks()

	# Set statusbar 
    statusvar.set("Video Download Starts")

    # update variable
    sbar.update() 

    # When one button is clicked another button should be disabled
    btn1["state"] = "disabled"

    # API url
    url = 'http://smartgsc.rannlabprojects.com/api/CMS/SearchAdvertisement'

    # boy to send
    data = {
        "Gender":"All",
        "MacAddress":"b8:27:eb:45:c7:21",
        "Location":"", 
        "Business":"",
        "Age":""
    }

    # Post Method
    x = requests.post(url, data = data)

    # convert into json 
    responses = json.loads(x.json())

    # Initialize progress and count value
    progress_value = int(100/len(responses))
    progress_count = 1

    # Iterate through each responses
    for response in responses:
    	# Downlaod video (video url and file name)
        youtube_video_download(response['VideoUrl'],str(response["ID"]))        

        # change progress bar value
        progress['value'] = progress_value*progress_count
        root.update_idletasks()

        # increment count value
        progress_count+=1

    # When video is downlaoded button is enabled
    btn1["state"] = "normal"

    # update status bar
    statusvar.set("Video Download Finished")

    # Messge box
    messagebox.showinfo("SUCCESSFULLY",  
                        "VIDOE SUCCESSFULLY DOWNLOADED") 

# Create Tinter object
root = Tk()

# set geometry
root.geometry("400x300")

# set Min and Max Size
root.maxsize(400,300)
root.minsize(400,300)

# Set Icon
root.iconbitmap("youtube.ico")

# Set title
root.title("Youtube Video Downloader")

# Label 1
lb1 = Label(root, text= "Enter Video URL:- ", font= "Arial 13 bold")
lb1.pack()

# Entry widget
video_url = Entry(root,width=60)
video_url.pack(pady=10)

# Error label
error = Label(root, text= "", font= "Arial 10", fg="red")
error.pack()

# button 1
btn1 = Button(root,text="Download", font= "Arial 13",command=Tkinter_Threading)
btn1.pack(pady=10)

# label 2
lb1 = Label(root, text= "Download Video From API", font= "Arial 13 bold")
lb1.pack(pady=10)

# button 2
btn2 = Button(root,text="Download", font= "Arial 13",command=Tkinter_Threading1)
btn2.pack(pady=10)

# progress bar
progress = Progressbar(root, orient = HORIZONTAL, 
            length = 300, mode = 'determinate')
progress.pack()

# status bar
statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w",fg="red")
sbar.pack(side=BOTTOM, fill=X)

# execute tkinter
root.mainloop()