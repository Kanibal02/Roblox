# Made by kanibal & chatGPT
# Made by kanibal & chatGPT
# Made by kanibal & chatGPT

import requests
import time
import os

def fetch_image_url(place_id):
    # Define the URL with the dynamic placeId
    url = f'https://thumbnails.roblox.com/v1/places/gameicons?placeIds={place_id}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the "imageUrl"
        if "data" in data and len(data["data"]) > 0 and "imageUrl" in data["data"][0]:
            return data["data"][0]["imageUrl"]
        else:
            print("imageUrl not found in the response")
            return None
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def download_image(image_url, save_path):
    # Send a GET request to the image URL
    response = requests.get(image_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the image to the specified path
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved to {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def get_unique_filename(base_name, extension):
    counter = 1
    unique_name = f"{base_name}{extension}"
    while os.path.exists(unique_name):
        unique_name = f"{base_name}_{counter}{extension}"
        counter += 1
    return unique_name

def main():
    # Get the placeId from the user
    place_id = input("Enter the placeId: ")
    
    # Fetch the image URL
    image_url = fetch_image_url(place_id)
    
    if image_url:
        # Define the base path and extension for the image
        base_name = os.path.join(os.path.dirname(__file__), 'gameicon')
        extension = '.png'
        
        # Get a unique filename
        save_path = get_unique_filename(base_name, extension)
        
        # Download and save the image
        download_image(image_url, save_path)

    # Infinite loop to keep the command prompt open
    print("Script completed. You can close this window safely.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
    
# Made by kanibal & chatGPT
# Made by kanibal & chatGPT
# Made by kanibal & chatGPT