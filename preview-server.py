#!/usr/bin/env python3
"""
Simple HTTP server to preview and test the audio hosting website locally.
Automatically generates the audio file list and starts a web server.
"""

import os
import http.server
import socketserver
import webbrowser
import json
from pathlib import Path

PORT = 8000

def generate_audio_list():
    """Generate a list of all MP3 files in the current directory."""
    current_dir = Path(__file__).parent
    
    # Get all MP3 files in the current directory
    audio_files = []
    for file in current_dir.glob('*.mp3'):
        audio_files.append(file.name)
    
    # Sort the files alphabetically
    audio_files.sort()
    
    # Write to JSON file
    output_file = current_dir / 'audio-files.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audio_files, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated audio-files.json with {len(audio_files)} audio files")
    return len(audio_files)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to add proper CORS headers for audio files."""
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Add cache control for better performance
        self.send_header('Cache-Control', 'public, max-age=3600')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Override to provide cleaner log messages."""
        if args[1] == '200':
            return  # Don't log successful requests to reduce clutter
        super().log_message(format, *args)

def start_server():
    """Start the HTTP server."""
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("\n" + "="*60)
    print("🎵 My Audio Hosting - Preview & Test Server")
    print("="*60)
    
    # Generate the audio file list
    count = generate_audio_list()
    
    # Start the server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n🌐 Server running at: {url}")
        print(f"📁 Serving {count} audio files")
        print(f"\n✨ Opening browser...")
        print(f"\n💡 Press Ctrl+C to stop the server\n")
        print("="*60 + "\n")
        
        # Open the browser automatically
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Could not open browser automatically: {e}")
            print(f"Please open {url} manually in your browser.")
        
        # Serve forever
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped.")
            print("="*60)

if __name__ == '__main__':
    start_server()
