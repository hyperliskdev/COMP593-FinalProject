from tkinter import *
from tkinter import ttk
import inspect
import os
import apod_desktop
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry


# Determine the path and parent directory of this script
script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
script_dir = os.path.dirname(script_path)


# Initialize the image cache
apod_desktop.init_apod_cache(script_dir)

root = Tk()
root.geometry('600x400')

# Create a basic GUI
root.title("Astronomy Picture of the Day")
root.rowconfigure(0, weight=95)
root.rowconfigure(1, weight=5)
root.columnconfigure(0, weight=50)
root.columnconfigure(1, weight=50)

# Image Frame
image_frame = ttk.LabelFrame(root, text="Image Frame")
image_frame.grid(row=0, column=0, sticky='nsew', columnspan=2, padx=20, pady=20)


# Cache Frame
cache_frame = ttk.LabelFrame(root, text="Cache Frame")
cache_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

cache_frame.columnconfigure(0, weight=50)
cache_frame.columnconfigure(1, weight=50)

cache_frame.rowconfigure(0, weight=100)

cache_select = ttk.Combobox(cache_frame, values=apod_desktop.get_all_apod_titles())
cache_select.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

cache_button = ttk.Button(cache_frame, text="View")
cache_button.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

# Download Frame
download_frame = ttk.LabelFrame(root, text="Download Frame")
download_frame.grid(column=1, row=1, sticky='nsew', padx=20, pady=20)

download_frame.columnconfigure(0, weight=50)
download_frame.columnconfigure(1, weight=50)

download_frame.rowconfigure(0, weight=100)


download_date = Calendar(download_frame, selectmode='day')
download_date.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

def image_date():
    apod_date = download_date.get_date()
    
download_button = ttk.Button(download_frame, text="Download", command=image_date)
download_button.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

### Download Button



root.mainloop()
