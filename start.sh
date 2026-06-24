#!/bin/bash
# Quick Start Script for My Audio Hosting
# This script provides an easy way to preview and test the website

echo "=========================================="
echo "🎵 My Audio Hosting - Quick Start"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3 to continue."
    exit 1
fi

echo "✅ Python 3 is installed"
echo ""

# Ask user which method they prefer
echo "How would you like to start the server?"
echo "1) Quick start (recommended) - Automatic setup and browser launch"
echo "2) Manual setup - Generate files and start server manually"
echo ""
read -p "Enter your choice (1 or 2): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting preview server..."
        echo ""
        python3 preview-server.py
        ;;
    2)
        echo ""
        echo "📋 Step 1: Generating audio file list..."
        python3 generate-audio-list.py
        echo ""
        echo "🌐 Step 2: Starting web server..."
        echo "Server will be available at: http://localhost:8000"
        echo "Press Ctrl+C to stop the server"
        echo ""
        python3 -m http.server 8000
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again and choose 1 or 2."
        exit 1
        ;;
esac
