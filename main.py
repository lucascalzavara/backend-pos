import processamento as process
import cv2
import webapi
import time
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/capturarFoto')
def capturarFoto():
    webapi.capturarImagem()
    time.sleep(30) # em segundos, para esperar a captura da imagem
    webapi.obterImagem()
    return "OK"

@app.route('/getFoto')
def getFoto():

    image = cv2.imread("fotos-capturadas/image.jpg")
    byte_im = process.toByteArray(image)
    return byte_im;


@app.route('/getFotoProcessada')
def getFotoProcessada():
    image = cv2.imread("fotos-capturadas/image.jpg")
    im_cicles, qtd = process.contar(image)
    byte_im = process.toByteArray(im_cicles)
    return byte_im;


@app.route('/getQtdOvos')
def getQtdOvos():
    image = cv2.imread("fotos-capturadas/image.jpg")
    im_cicles, qtd = process.contar(image)
    return str(qtd);