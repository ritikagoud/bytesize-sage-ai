# PulsePoint AI – ByteSize Sage Hackathon

PulsePoint AI is a multimodal video intelligence tool that converts long-form
educational videos into short, high-impact clips for the attention economy.

## Problem
High-value insights in lectures, podcasts, and workshops are often buried
inside long videos, making them inaccessible for short-form audiences.

## Solution
This system automatically:
- Extracts audio from long-form videos
- Analyzes audio energy to detect high-emphasis moments
- Identifies meaningful timestamps
- Clips the video around those moments
- Generates multiple short, shareable reels

## Tech Stack
- Python
- MoviePy
- Librosa
- NumPy

## How to Run
1. Place the input video as `input_video.mp4`
2. Run:
   python main.py
3. Output clips are generated in the `outputs/` folder

## Demo
Screen recording link: https://drive.google.com/file/d/1d6vgMWx1N0cpacy5jumiQ9iV5erL-tya/view?usp=sharing

## Output Samples
- outputs/clip_1.mp4
- outputs/clip_2.mp4
- outputs/clip_3.mp4
- outputs/clip_4.mp4
