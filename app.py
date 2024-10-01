from flask import Flask, render_template, request, jsonify
from pyzbar.pyzbar import decode
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_qr_code():
    # Recebe o arquivo de imagem enviado no request
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    # Abre a imagem usando PIL
    image = Image.open(io.BytesIO(file.read()))
    
    # Decodifica o QR Code
    decoded_objects = decode(image)
    
    if not decoded_objects:
        return jsonify({'error': 'No QR Code found'}), 400
    
    # Extrai o texto do QR Code
    qr_data = decoded_objects[0].data.decode('utf-8')
    
    return jsonify({'qr_data': qr_data}), 200

if __name__ == '__main__':
    app.run(debug=True)
