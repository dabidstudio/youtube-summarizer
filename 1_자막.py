
from youtube_transcript_api import YouTubeTranscriptApi

def get_korean_transcript(youtube_url):
    # Extract video ID from the URL
    video_id = youtube_url.split("v=")[1]
    
    try:
        # Fetch available transcripts
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)

        # Check if a Korean transcript is available
        korean_transcript = None
        for transcript in transcripts:
            if transcript.language_code == 'ko':
                korean_transcript = transcript.fetch()
                break

        if korean_transcript:
            # Combine all text parts into one
            korean_text = "\n".join([entry['text'] for entry in korean_transcript])
            return korean_text
        else:
            return "Korean subtitles not available for this video."

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
youtube_url = "https://www.youtube.com/watch?v=dfcv07E5eo0"
korean_subtitles = get_korean_transcript(youtube_url)
print(korean_subtitles)
