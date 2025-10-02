# 🎵 My Audio Hosting

A simple web-based audio player to preview and test your audio collection.

## 🎬 Preview

![Audio Player Interface - Search Feature](https://github.com/user-attachments/assets/42c7ea1c-1c64-4644-b29b-72dab3dff9f3)

*Search and filter your audio collection with an intuitive interface*

![Audio Player Interface - Category Filter](https://github.com/user-attachments/assets/84641e65-5d1f-4cf0-8c8f-4108a11da3a4)

*Filter by category to quickly find specific types of music*

## 📋 Overview

This repository contains a collection of audio files (MP3 format) with a simple web interface to preview and test them. The interface provides:

- 🎧 Audio playback with controls
- 🔍 Search functionality
- 🏷️ Category filtering
- 📊 Progress bars and time display
- 📱 Responsive design for mobile and desktop

## 🚀 Quick Start

### Method 1: Using Python (Recommended)

The easiest way to preview and test the website is to use the included Python server:

```bash
python3 preview-server.py
```

This will:
1. Automatically generate the list of audio files
2. Start a local web server on port 8000
3. Open your browser to http://localhost:8000

**That's it!** You can now browse and play all your audio files.

### Method 2: Manual Setup

If you prefer to set things up manually:

1. **Generate the audio file list:**
   ```bash
   python3 generate-audio-list.py
   ```

2. **Start a local web server:**
   
   Using Python 3:
   ```bash
   python3 -m http.server 8000
   ```
   
   Or using Python 2:
   ```bash
   python -m SimpleHTTPServer 8000
   ```

3. **Open your browser:**
   
   Navigate to: http://localhost:8000

### Method 3: Using Node.js

If you have Node.js installed, you can use `http-server`:

1. Install http-server (if not already installed):
   ```bash
   npm install -g http-server
   ```

2. Generate the audio list and start the server:
   ```bash
   python3 generate-audio-list.py
   http-server -p 8000
   ```

3. Open your browser to: http://localhost:8000

## 🎨 Features

### Search
- Type in the search box to filter audio files by name
- Search is case-insensitive and matches any part of the filename

### Categories
- Click on category buttons to filter by music type
- Categories are automatically detected from file naming patterns
- Click "All" to show all files

### Playback Controls
- **Play/Pause**: Click the play button or anywhere on an audio item
- **Progress Bar**: Click anywhere on the progress bar to seek
- **Now Playing**: See what's currently playing in the highlighted section at the top

### Audio Item Features
- Each audio file is displayed as a card
- Click the play button (▶) to start playback
- Progress bar shows playback progress
- Time display shows current playback time
- Currently playing item is highlighted

## 📁 File Structure

```
my-audio-hosting/
├── index.html              # Main web interface
├── preview-server.py       # Quick start server (recommended)
├── generate-audio-list.py  # Script to generate audio file list
├── audio-files.json        # Generated list of audio files (auto-created)
├── README.md               # This file
└── *.mp3                   # Your audio files
```

## 🛠️ Requirements

- **Python 3.x** (for running the server and generating file lists)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- No additional dependencies required!

## 📱 Browser Compatibility

The audio player works on:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🔧 Troubleshooting

### Audio files not showing up?

1. Make sure you've run the `generate-audio-list.py` script
2. Check that `audio-files.json` was created in the same directory
3. Refresh your browser (Ctrl+R or Cmd+R)

### Server not starting?

1. Check if port 8000 is already in use:
   ```bash
   # On macOS/Linux:
   lsof -i :8000
   
   # On Windows:
   netstat -ano | findstr :8000
   ```

2. Try using a different port:
   ```bash
   python3 -m http.server 8080
   ```
   Then open http://localhost:8080

### Audio not playing?

1. Check your browser's console (F12) for errors
2. Make sure the audio files are in the same directory as index.html
3. Some browsers may block autoplay - click the play button manually
4. Check your browser's audio permissions

## 🌐 Deploying Online

To host this online (e.g., on GitHub Pages, Netlify, or Vercel):

1. Generate the audio file list:
   ```bash
   python3 generate-audio-list.py
   ```

2. Commit and push both `index.html` and `audio-files.json`

3. Enable GitHub Pages or deploy to your hosting service

4. The audio files will be served directly from your repository

## 📝 Adding New Audio Files

1. Add your new `.mp3` files to the repository
2. Run the generate script again:
   ```bash
   python3 generate-audio-list.py
   ```
3. Refresh your browser

## 🎯 Tips

- **Use descriptive filenames** - They'll be displayed as-is in the player
- **Organize by prefix** - Files starting with the same prefix will be grouped as a category
- **Keep files small** - For better web performance, consider compressing large files
- **Use consistent naming** - This helps with searching and filtering

## 📄 License

This project is provided as-is for personal use. Audio files may have their own licenses.

## 🤝 Contributing

Feel free to enhance the audio player interface or add new features!

---

**Enjoy your audio collection! 🎶**
