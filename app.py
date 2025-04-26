from flask import Flask, request, render_template

app = Flask(__name__)

SHIFT = 3  # Simple Caesar cipher shift

def encrypt(text):
    return ''.join(chr(ord(c) + SHIFT) for c in text)

def decrypt(text):
    return ''.join(chr(ord(c) - SHIFT) for c in text)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        message = request.form['message']
        action = request.form['action']
        if action == 'encrypt':
            result = encrypt(message)
        elif action == 'decrypt':
            result = decrypt(message)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
