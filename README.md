# IG Auto Uploader 🚀

A complete, automated pipeline that fetches video content from Google Drive, enhances the video quality specifically for mobile aspect ratios, generates viral, AI-powered captions, and autonomously uploads the final product to Instagram.

## ✨ Features
* **Google Drive Integration:** Automatically fetches raw video files from a designated Google Drive folder.
* **FFmpeg Video Enhancement:** Resizes, pads, and optimizes video bitrate and framerate (1080x1920, 30fps) for native Instagram Reels quality.
* **AI Caption Generation:** Uses Google Gemini Pro to write engaging captions and relevant viral hashtags based on the video's topic.
* **Automated Publishing:** Authenticates and uploads the finished video directly to a specified Instagram account using `instagrapi`.
* **Secure Credential Management:** Utilizes a `.env` file structure to keep your API keys and passwords secure and out of version control.

## 🛠️ Technologies Used
* **Python 3.x**
* **Instagrapi:** Unofficial Instagram API wrapper for media uploads.
* **Google Generative AI:** For automated caption generation.
* **Google Drive API:** For cloud file retrieval.
* **FFmpeg:** For backend video processing.

## 📋 Prerequisites
Before running this project, ensure you have the following installed and configured:
1. **Python 3.7+**
2. **FFmpeg:** Installed and added to your system's PATH.
3. **Google Cloud Console Account:** You need an active project with the Google Drive API enabled, and a downloaded `credentials.json` file placed in the root directory.
4. **Google Gemini API Key:** Generated from Google AI Studio.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/ig-auto-uploader.git](https://github.com/YourUsername/ig-auto-uploader.git)
   cd ig-auto-uploader
