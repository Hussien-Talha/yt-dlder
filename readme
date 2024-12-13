# YouTube Video Downloader with `yt-dlp`

This project is a Python-based YouTube video downloader that utilizes the `yt-dlp` library for efficient and robust video downloading. The script allows users to download videos in the highest resolution and includes functionality for validating URLs and printing debugging information about available video streams.

---

## Features

- **High-Quality Video Downloads**: Automatically selects and downloads the highest resolution available for a given video.
- **Debugging Video Streams**: Prints the details of available video streams for debugging purposes.
- **URL Verification**: Checks if the provided YouTube URL is valid before attempting to download.
- **Flexible File Naming**: Handles cases where files with the same name already exist by appending incremental numbers to the file name.

---

## Requirements

- Python 3.6 or higher
- `yt-dlp` library
- `ssl` module (standard in Python)
- Internet connection

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Hussien-Talha/yt-dlder.git
   cd yt-dlder
   ```

2. **Install Dependencies:**
   Install `yt-dlp` via pip:
   ```bash
   pip install yt-dlp
   ```

3. **Setup Environment:**
   Ensure Python has the necessary permissions and SSL context is properly configured:
   ```python
   import ssl
   ssl._create_default_https_context = ssl._create_unverified_context
   ```

---

## Usage

1. Run the script:
   ```bash
   python youtube_downloader.py
   ```

2. Enter a YouTube video URL when prompted:
   ```
   Enter a YouTube video URL: https://www.youtube.com/watch?v=example
   ```

3. The script will:
   - Validate the URL.
   - Display available video streams for debugging.
   - Download the video in the highest resolution available.

4. Check the output in the script's directory. The downloaded file will have an `.mp4` extension.

---

## Debugging

The script includes a `debug_video_streams` function to display all available streams. This helps in understanding the formats and resolutions provided by YouTube for a given video.

---

## Customization

Modify the following as needed:

- **Download Quality**:
  Update the configuration in `yt-dlp` options for different download preferences (e.g., audio-only or specific resolutions).
- **User-Agent Header**:
  Adjust headers in the `yt-dlp` options if facing compatibility issues.

---

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests with improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.