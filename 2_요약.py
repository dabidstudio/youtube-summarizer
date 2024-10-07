


sample_text = """첫 번째 주제는 지금 경제에 우리 주식장에서 가장 불타고 있는 얘기 안 할 수 없어서 한번 해보도록 하겠습니다 바로 고려아연 얘기입니다 쩐의 전쟁이 펼쳐지고 있다 아 이거 제가 아는 분들도 지금 아주 이것 때문에 난리가 났는데 9월 13일 날 내용을 조금 이제 소개시켜 드리면 모르시는 분도 많이 있을 테니까 사모펀드 MBK 파트너스가 고려아연의 지분을 공개 매수를 선언했습니다 고려아연은 기업이에요 기업 비철금속 제련하는 기업 굉장히 큰 기업입니다 생각보다 시가총액이 10조가 넘는 큰 기업이라고 할 수 있고 사모펀드 MBK 파트너스가 공개 매수 선언 내용은 이래요 고려아연 지분을 6.98%에서 14%니까 한 7에서 15% 정도 사이의 지분을 공개 매수하겠다 전일 종가 대비 18% 이상 높은 주당 66만 원을 얘기했고요 기간은 지금입니다 9월 13일부터 10월 4일이니까 지금이에요 열흘도 안 남은 지금이라고 할 수 있는데 이걸 만약에 다 사면 공개 매수대금만 2조 원을 넘어요 물론 6.98% 아래 최소 매수 예정 수량 미만일 경우에는 전량 사지는 않겠지
"""

from openai import OpenAI
OPENAI_API_KEY = ""

def summarize_transcript(transcript:str) -> str:

    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt_template = """
    아래 내용을 한글로 요약해주세요:
    - 핵심 내용을 불렛포인트 형태로 요약해주세요.
    - 이 영상을 볼지 말지 결정하기 위한 요약입니다.
    - 요약은 10줄 정도로 해주세요.
    """
    prompt = f"{prompt_template}\n\n{transcript}"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    summary = completion.choices[0].message.content
    return summary


print(summarize_transcript(sample_text))