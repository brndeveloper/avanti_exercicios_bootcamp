import cv2
import numpy as np

# carregar a imagem
caminho_imagem = 'foto_cone.png'
imagem = cv2.imread(caminho_imagem)

# dimensões da imagem
altura, largura, canais = imagem.shape

# tipo de dado da imagem
tipo_dado = imagem.dtype

# converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# valores de tons de cinza
tom_cinza_maximo = np.max(imagem_cinza)
tom_cinza_minimo = np.min(imagem_cinza)
tom_cinza_medio = np.mean(imagem_cinza)

# exibir informações
print(f"Altura: {altura}")
print(f"Largura: {largura}")
print(f"Canais de cor: {canais}")
print(f"Tipo de dado: {tipo_dado}")
print(f"Tom de cinza máximo: {tom_cinza_maximo}")
print(f"Tom de cinza médio: {tom_cinza_medio}")
print(f"Tom de cinza mínimo: {tom_cinza_minimo}")
