import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import re


# Set OpenAI API key
OPENAI_API_KEY = ""


## 특정 video에 대해서 자막을 구하는 함수
## 자막의 형태는 리스트 형태로 구해짐
def get_video_transcript(video_id: str, languages: list = ["ko", "en"]) -> list:

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, languages=languages
        )
        return transcript_list
    except Exception:
        return []

## 자막을 받아서 요약을 해주는 함수
def summarize_transcript(transcript: list) -> str:

    client = OpenAI(api_key=OPENAI_API_KEY)
    combined_text = " ".join([entry["text"] for entry in transcript])

    prompt_template = """
    아래 내용을 한글로 요약해주세요:
    - 핵심 내용을 불렛포인트 형태로 요약해주세요.
    - 이 영상을 볼지 말지 결정하기 위한 요약입니다.
    - 요약은 10줄 정도로 해주세요.
    """
    prompt = f"{prompt_template}\n\n{combined_text}"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    summary = completion.choices[0].message.content
    return summary

## 유튜브 영상 ID를 추출하는 함수
def extract_video_id(url: str) -> str:
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return video_id_match.group(1) if video_id_match else ""






def main():

    st.title("유튜브 요약 프로그램")

    # Input for YouTube video URL
    video_url = st.text_input(
        "YouTube 영상 URL을 입력하세요",
    )

    if video_url:
        video_id = extract_video_id(video_url)
        transcript = get_video_transcript(video_id)

        if transcript:
            with st.expander("### 전체 스크립트", expanded=False):
                full_transcript = " ".join([t['text'] for t in transcript])
                st.text_area("", value=full_transcript, height=300)
            with st.expander("### 요약", expanded=False):
                summary = summarize_transcript(transcript)
                st.write(summary)
            st.video(video_url)


if __name__ == "__main__":
    main()
