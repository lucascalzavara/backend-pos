from flask import Flask
import processamento as process
import cv2
import webapi

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/capturarImagen')
def capturarImagen():
    webapi.capturarImagem()
    # delay
    imagem = webapi.obterImagem().content
    
    im_cicles, qtd = process.contar(imagem)
    return {
        'im_cicles': im_cicles,
        'qtd_ovos': qtd
    }