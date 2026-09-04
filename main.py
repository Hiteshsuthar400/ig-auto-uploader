import os
import subprocess
from instagrapi import Client
import google.generativeai as genai
import config  # Imports your separated data file

# Configure AI using the key from config.py
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def download_from_drive(folder_id):
    print("Downloading video from Google Drive...")
    # Drive API logic goes here
    return "temp_downloaded_video.mp4" 

def enhance_video(input_path, output_path):
    print("Enhancing video quality via FFmpeg...")
    command = [
        'ffmpeg', '-y', '-i', input_path,
        '-vf', 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2',
        '-r', '30',
        '-c:v', 'libx264', '-preset', 'slow', '-crf', '18',
        '-c:a', 'aac', '-b:a', '128k',
        output_path
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_path

def generate_caption(topic="a cool lifestyle video"):
    prompt = f"Write a short, engaging Instagram caption for {topic}. Include 5 relevant viral hashtags. Do not include emojis."
    return model.generate_content(prompt).text.strip()

def upload_to_instagram(video_path, caption):
    print("Logging into Instagram...")
    cl = Client()
    # Login using credentials from config.py
    cl.login(config.IG_USERNAME, config.IG_PASSWORD)
    
    print("Uploading to Instagram...")
    media = cl.clip_upload(video_path, caption)
    print(f"Upload successful! Media ID: {media.dict().get('id')}")

def main():
    raw_video = download_from_drive(config.DRIVE_FOLDER_ID)
    processed_video = "ready_for_ig.mp4"
    
    enhance_video(raw_video, processed_video)
    caption = generate_caption("a cinematic nature drone shot")
    upload_to_instagram(processed_video, caption)
    
    if os.path.exists(raw_video): os.remove(raw_video)
    if os.path.exists(processed_video): os.remove(processed_video)

if __name__ == "__main__":
    main()
