
## 1. 요구 사항

코드 실행을 위한 요구사항 (라이브러리) 는 다음과 같음

- `streamlit`
- `youtube_transcript_api`
- `openai`

## 2. 라이브러리 설치

### 2.1. pip 사용하여 라이브러리 설치하기

1. **pip**를 사용하여 필요한 라이브러리를 설치

```bash
pip install streamlit youtube-transcript-api openai
```

맥북의 경우
```bash
pip3 install streamlit youtube-transcript-api openai
```


위 명령어를 실행하면 필요한 모든 라이브러리가 설치됨

### 2.2. 가상환경(venv) 사용하기

간혹 라이브러리 설치가 잘 되지 않거나, 충돌이 발생할 수 있음. 이럴 경우 파이썬의 가상환경(venv)을 사용하여 문제를 해결하기

#### 가상환경 설정 및 실행 방법

1. **venv** 모듈을 사용하여 가상환경을 생성

```bash
python -m venv venv
```

맥북의 경우
```bash
python3 -m venv venv
```

2. 가상환경 활성화.

   - **Windows**:

   ```bash
   venv\Scripts\activate
   ```

   - **macOS/Linux**:

   ```bash
   source venv/bin/activate
   ```

   터미널에서 (venv)라고 표시가 되면 가상환경 활성화가 완료됨

3. 가상환경이 활성화되었으면, 다시 라이브러리를 설치.

   ```bash
   pip install streamlit youtube-transcript-api openai
   ```
   맥북
   ```bash
   pip3 install streamlit youtube-transcript-api openai
   ```



4. 필요 작업이 끝난 후 가상환경을 비활성화하려면 다음 명령어를 입력합니다.

```bash
deactivate
```

## 3. 코드 실행 방법

라이브러리 설치 후, 아래와 같이 코드를 실행할 수 있음:

```bash
streamlit 최종.py
```
