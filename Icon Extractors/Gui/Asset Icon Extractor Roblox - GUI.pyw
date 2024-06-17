# Made by kanibal & chatGPT
# Made by kanibal & chatGPT
# Made by kanibal & chatGPT

import tkinter as tk
from tkinter import messagebox
import requests
import os

def fetch_image_url(place_id):
    url = f'https://thumbnails.roblox.com/v1/assets?assetIds={place_id}&returnPolicy=PlaceHolder&size=420x420&format=Png&isCircular=false'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0 and "imageUrl" in data["data"][0]:
            return data["data"][0]["imageUrl"]
        else:
            messagebox.showerror("Error", "imageUrl not found in the response")
            return None
    else:
        messagebox.showerror("Error", f"Failed to fetch data. Status code: {response.status_code}")
        return None

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        messagebox.showinfo("Success", f"Image saved to {save_path}")
    else:
        messagebox.showerror("Error", f"Failed to download image. Status code: {response.status_code}")

def get_unique_filename(base_name, extension):
    counter = 1
    unique_name = f"{base_name}{extension}"
    while os.path.exists(unique_name):
        unique_name = f"{base_name}_{counter}{extension}"
        counter += 1
    return unique_name

def on_submit():
    place_id = entry.get()
    if not place_id:
        messagebox.showerror("Error", "Please enter a AssetId")
        return
    image_url = fetch_image_url(place_id)
    if image_url:
        base_name = os.path.join(os.path.dirname(__file__), 'asseticon')
        extension = '.png'
        save_path = get_unique_filename(base_name, extension)
        download_image(image_url, save_path)

app = tk.Tk()
app.title("Roblox Icon Downloader")
app.geometry("150x120")
app.resizable(False, False)  # Disable window resizing

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter AssetId:")
label.pack(pady=5)

entry = tk.Entry(frame)
entry.pack(pady=5)

button = tk.Button(frame, text="Download", command=on_submit)
button.pack(pady=10)

app.mainloop()

# Made by kanibal & chatGPT
# Made by kanibal & chatGPT
# Made by kanibal & chatGPT