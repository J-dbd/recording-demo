from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import whisper
# 임시
app = FastAPI()

# CORS 허용 (로컬 테스트용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포 시 도메인 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Whisper 모델 로드 (최초 실행 시 시간이 다소 소요됨)
model = whisper.load_model("base")


@app.post("/upload-audio")
async def upload_audio(audio: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
            contents = await audio.read()
            tmp.write(contents)
            tmp_path = tmp.name

        result = model.transcribe(tmp_path, language="ko")
        return {"transcript": result["text"]}
    except Exception as e:
        return {"error": str(e)}
