from gtts import gTTS
import tempfile

# Hàm chuyển văn bản thành giọng nói và lưu vào file MP3
def generate_speech(text):
    # Tạo file tạm thời và trả về đường dẫn file tạm thời
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        tts = gTTS(text, lang='vi')  # Sử dụng ngôn ngữ tiếng Việt
        tts.save(temp_file.name)
        return temp_file.name
