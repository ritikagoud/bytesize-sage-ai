import librosa
import numpy as np
from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path,audio_path="temp_audio.wav"):
    video=VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path,verbose=False,logger=None)
    return audio_path

def get_audio_energy(audio_path,hop_length=512):
    y,sr=librosa.load(audio_path,sr=None)
    rms=librosa.feature.rms(y=y,hop_length=hop_length)[0]
    times=librosa.frames_to_time(range(len(rms)),sr=sr,hop_length=hop_length)
    return rms,times

def find_top_peaks(rms, times, top_n=3):
    avg_energy = np.mean(rms)
    peak_indices = np.where(rms > avg_energy)[0]

    if len(peak_indices) == 0:
        return [times[len(times)//2]]

    selected = peak_indices[::max(1, len(peak_indices)//top_n)]
    peak_times = [times[i] for i in selected[:top_n]]
    return peak_times


def clip_video(video_path, peak_times,clip_duration=30):
    video=VideoFileClip(video_path)
    os.makedirs("outputs",exist_ok=True)

    for i,t in enumerate(peak_times):
        start=max(t - clip_duration / 2, 0)
        end=min(start + clip_duration, video.duration)
        clip=video.subclip(start, end)
        clip.write_videofile(
            f"outputs/clip_{i+1}.mp4",
            codec="libx264",
            audio_codec="aac",
            verbose=False,
            logger=None
        )

def main():
    video_path="input_video.mp4"  
    audio_path=extract_audio(video_path)
    rms,times=get_audio_energy(audio_path)
    peak_times=find_top_peaks(rms,times,top_n=3)
    clip_video(video_path,peak_times)

if __name__=="__main__":
    main()
