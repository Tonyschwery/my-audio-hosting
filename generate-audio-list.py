#!/usr/bin/env python3
"""
Generate a JSON file containing a list of all MP3 files in the current directory.
This file is used by index.html to display the audio files.
"""

import os
import json

def generate_audio_list():
    """Generate a list of all MP3 files in the current directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all MP3 files in the current directory
    audio_files = []
    for file in os.listdir(current_dir):
        if file.endswith('.mp3'):
            audio_files.append(file)
    
    # Sort the files alphabetically
    audio_files.sort()
    
    # Write to JSON file
    output_file = os.path.join(current_dir, 'audio-files.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audio_files, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated audio-files.json with {len(audio_files)} audio files")
    print(f"📝 Output file: {output_file}")
    
    return len(audio_files)

if __name__ == '__main__':
    count = generate_audio_list()
    print(f"\nYou can now open index.html in your browser to preview the audio files!")
