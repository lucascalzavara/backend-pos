from pip._vendor import requests

url = "http://192.168.15.13"

def capturarImagem():
    api_url = url + "/capturar-foto"
    response = requests.get(api_url)

    print(response.status_code)

    return response

def obterImagem():
    api_url = url + "/foto-salva"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        with open("fotos-capturadas/image.jpg", 'wb') as f:
            f.write(response.content)

    return response