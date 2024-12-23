from flask import Flask, render_template, request, send_file
from convert_text_to_speech import generate_speech
import tempfile

app = Flask(__name__)

# Trang chính với form nhập văn bản
@app.route('/')
def index():
    return render_template('index.html')

# Xử lý chuyển đổi văn bản thành giọng nói
@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    if text.strip():
        # Tạo file MP3 từ văn bản và lưu trữ vào thư mục tạm thời
        file_path = generate_speech(text)
        return send_file(file_path, as_attachment=True, download_name=f"{text[:20]}.mp3")
    return "Vui lòng nhập văn bản không rỗng!"

if __name__ == "__main__":
    app.run(debug=True)
