document.querySelector('textarea').addEventListener('input', function() {
    const button = document.querySelector('button');
    if (this.value.trim() !== '') {
        button.disabled = false;  // Kích hoạt nút nếu có văn bản
    } else {
        button.disabled = true;   // Vô hiệu hóa nút nếu không có văn bản
    }
});
