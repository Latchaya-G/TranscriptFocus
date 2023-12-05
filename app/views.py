# transcript_viewer/views.py
from django.shortcuts import render, redirect
from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(youtube_link):
    # Extract video ID from YouTube link
    match = re.search(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', youtube_link)
    if match:
        return match.group(1)
    return None

def home(request):
    #print(request.POST['yt_link'])
   # video_id = extract_video_id(request.POST['yt_link'])
    video_id = extract_video_id('https://youtu.be/oBt53YbR9Kk?si=fZaJwXiZzc1Jkb-o')
    if video_id:
        # Fetch transcript data
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Format transcript data as a list of dictionaries
        transcript_data = [
            {'start': entry['start'], 'end': entry['start'] + entry['duration'], 'text': entry['text']}
            for entry in transcript
        ]

        return render(request, 'app/index.html', {'transcript_data': transcript_data, 'video_id': video_id})
    else:
        return render(request, 'app/index.html', {'error_message': 'Invalid YouTube link'})

def get_link(request):
    if request.method == "POST":
        link = request.POST['yt_link']
        return redirect('home')
    return render(request, 'app/get_link.html')
