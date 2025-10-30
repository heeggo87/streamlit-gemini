# 💬 Gemini 챗봇 앱

Google의 Gemini LLM을 활용하여 사용자의 질문에 실시간으로 응답하는 Streamlit 기반 챗봇입니다. 웹 브라우저에서 바로 실행 가능하며, 간단한 설정만으로 누구나 사용할 수 있습니다.

---

## 🧰 기술 스택

- **Streamlit** – 빠르고 직관적인 웹 앱 프레임워크
- **Google Generative AI SDK** – Gemini 모델을 호출하는 Python 클라이언트
- **Python 3.9+**

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| 💬 실시간 질문 응답 | 사용자가 입력한 질문에 대해 Gemini 모델이 자연어로 답변 |
| 🧠 대화 기록 유지 | `st.session_state`를 활용해 이전 대화 내용을 화면에 유지 |
| 🗨️ 채팅 UI 구성 | Streamlit의 `chat_input`, `chat_message` 컴포넌트를 활용한 직관적인 인터페이스 |
| 🔒 API 키 보안 관리 | `secrets.toml`을 통해 Gemini API 키를 안전하게 관리 |
| ⚡ 빠른 응답 | Gemini 2.5 Flash 모델을 사용하여 빠르고 정확한 응답 제공 |

---

## 📦 설치 및 실행 방법

1. **레포 클론**
   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. **필수 패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **API 키 설정**
   `.streamlit/secrets.toml` 파일을 생성하고 다음 내용을 추가합니다:

   ```toml
   GEMINI_API_KEY = "your-gemini-api-key"
   ```

4. **앱 실행**
   ```bash
   streamlit run app.py
   ```

---

## 🚀 배포 방법

### 🔧 방법 1: Streamlit Community Cloud

1. [Streamlit Cloud](https://streamlit.io/cloud)에 로그인
2. GitHub 레포를 연결하고 `app.py`를 선택
3. `.streamlit/secrets.toml`에 API 키를 설정
4. 배포 후 URL을 통해 누구나 접근 가능

### 🐳 방법 2: Docker로 배포

1. `Dockerfile` 생성:

   ```Dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY . /app
   RUN pip install -r requirements.txt
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. 이미지 빌드 및 실행:

   ```bash
   docker build -t gemini-chatbot .
   docker run -p 8501:8501 gemini-chatbot
   ```

---

## 📁 파일 구조

```
gemini-chatbot/
├── app.py               # Streamlit 앱 메인 코드
├── requirements.txt     # 필요한 패키지 목록
└── .streamlit/
    └── secrets.toml     # Gemini API 키 저장
```

---

## 📄 라이선스

MIT 라이선스. 자유롭게 사용하고 수정하세요.

---

