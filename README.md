# Pinterest Video Downloader CLI

A command-line interface (CLI) application to download Pinterest videos in high quality (1080P). This tool supports both single video downloads and bulk downloading from multiple URLs.

## Features

- 🎥 Download Pinterest videos in high quality (1080P)
- 📦 Two download modes:
  - Single Link Download: Download video from a single Pinterest URL
  - Bulk Download: Download multiple videos from URLs listed in file.txt
- 📂 Automatic folder creation with date-based naming (DDMMYYYY_PinterestDownloader)
- 🔄 Progress tracking for bulk downloads
- ⚡ Fast and efficient downloads using chunked transfer
- 🛡️ Error handling and download status reporting

## Installation

1. Make sure you have Python 3.6 or higher installed on your system
2. Clone or download this repository
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Run the application using Python:
```bash
python app.py
```

### Menu Options

The application presents three options:
```
=== Pinterest Downloader ===
0. Support Developer 💖
1. Single Link Downloader
2. Bulk Downloader (from file.txt)
```

### Single Link Download
1. Choose option `1` from the menu
2. Enter the Pinterest video URL when prompted
3. The video will be downloaded to a date-based folder (e.g., "03052025_PinterestDownloader")

### Bulk Download
1. Create a `file.txt` in the same directory as `app.py`
2. Add Pinterest video URLs to `file.txt`, one URL per line
3. Choose option `2` from the menu
4. The application will process all URLs and download videos to the date-based folder

## Output

- Downloaded files are saved in a folder named with the current date (DDMMYYYY_PinterestDownloader)
- Videos are saved with timestamps in the format: `pinterest_YYYYMMDD_HHMMSS.mp4`

## Support the Developer

If you find this tool helpful, consider supporting the developer:

[![Saweria](https://img.shields.io/badge/Saweria-Support%20Developer-orange)](https://saweria.co/ahmadiizhar)

🎁 Support Link: [https://saweria.co/ahmadiizhar](https://saweria.co/ahmadiizhar)

## Notes

- Ensure you have a stable internet connection for reliable downloads
- Make sure you have sufficient disk space for storing downloaded videos
- For bulk downloads, verify that your `file.txt` contains valid Pinterest video URLs
