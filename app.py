import os
import random
import string
import requests
from datetime import datetime
import base64

# Constants
API_URL = "https://pintod.com/wp-json/aio-dl/video-data/"
OUTPUT_FOLDER = datetime.now().strftime("%d%m%Y") + "_PinterestDownloader"

def generate_token():
    """Generate a random 64-character lowercase string"""
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(64))

def generate_hash(url):
    """Generate a base64 encoded hash with random padding"""
    base = base64.b64encode(url.encode()).decode()
    random_pad = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return base + random_pad

def ensure_output_folder():
    """Create output folder if it doesn't exist"""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

def download_media(url, filename):
    """Download media file from URL"""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Successfully downloaded: {filename}")
        return True
    print(f"Failed to download media from URL")
    return False

def process_pinterest_url(url):
    """Process a single Pinterest URL"""
    try:
        print(f"\nProcessing URL: {url}")
        
        # Generate random token and hash
        token = generate_token()
        hash_value = generate_hash(url)

        # Prepare form data
        form_data = {
            'url': url,
            'token': token,
            'hash': hash_value
        }

        # Make API request
        print("Fetching media information...")
        response = requests.post(API_URL, data=form_data)
        
        if response.status_code == 200:
            data = response.json()
            
            # Get high resolution media (1080P)
            if 'medias' in data and len(data['medias']) > 1:
                media_url = data['medias'][1]['url']
                filename = f"pinterest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
                
                # Ensure output folder exists
                ensure_output_folder()
                
                # Download the media
                return download_media(media_url, filename)
                
        print("Failed to process URL: Invalid response from API")
        return False
        
    except Exception as e:
        print(f"Error processing URL: {str(e)}")
        return False

def process_bulk_download():
    """Process all URLs from file.txt"""
    try:
        if not os.path.exists('file.txt'):
            print("Error: file.txt not found!")
            return False
            
        with open('file.txt', 'r') as f:
            urls = f.read().splitlines()
        
        if not urls:
            print("Error: file.txt is empty!")
            return False
            
        print(f"\nFound {len(urls)} URLs in file.txt")
        success_count = 0
        
        for i, url in enumerate(urls, 1):
            if url.strip():
                print(f"\nProcessing URL {i}/{len(urls)}")
                if process_pinterest_url(url.strip()):
                    success_count += 1
                    
        print(f"\nDownload completed! Successfully downloaded {success_count}/{len(urls)} files")
        print(f"Files saved in: {OUTPUT_FOLDER}")
        return True
        
    except Exception as e:
        print(f"Error in bulk download: {str(e)}")
        return False

def main():
    print("\n=== Pinterest Downloader ===")
    print("0. Support Developer 💖")
    print("1. Single Link Downloader")
    print("2. Bulk Downloader (from file.txt)")
    
    while True:
        choice = input("\nPilih menu (0/1/2): ")
        
        if choice == "0":
            print("\nTerima kasih atas dukungannya!")
            print("Saweria: https://saweria.co/ahmadiizhar")
            os.system("start https://saweria.co/ahmadiizhar")
            break
            
        elif choice == "1":
            url = input("\nMasukkan URL Pinterest: ")
            if process_pinterest_url(url):
                print(f"\nDownload completed! File saved in: {OUTPUT_FOLDER}")
            break
            
        elif choice == "2":
            process_bulk_download()
            break
            
        else:
            print("Pilihan tidak valid! Silakan pilih 1 atau 2.")

if __name__ == '__main__':
    main()
