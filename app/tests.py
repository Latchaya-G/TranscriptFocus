from youtube_transcript_api import YouTubeTranscriptApi
import re
def extract_video_id(youtube_link):
    # Extract video ID from YouTube link
    match = re.search(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', youtube_link)
    if match:
        return match.group(1)
    return None

video_id = extract_video_id('https://youtu.be/oBt53YbR9Kk?si=fZaJwXiZzc1Jkb-o')
transcript = YouTubeTranscriptApi.get_transcript(video_id)
for i in transcript:
	print(i)