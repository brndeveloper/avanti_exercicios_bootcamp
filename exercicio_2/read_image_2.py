import cv2
import matplotlib.pyplot as plt

# carregar a imagem
caminho_imagem = 'foto_cone.png'
imagem = cv2.imread(caminho_imagem)

# filtro da média
filtro_media = cv2.blur(imagem, (5, 5))
# filtro da mediana
filtro_mediana = cv2.medianBlur(imagem, 5) 
# filtro gaussiano
filtro_gaussiano = cv2.GaussianBlur(imagem, (5, 5), 0)

# exibir com matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(filtro_media, cv2.COLOR_BGR2RGB))
plt.title('Filtro da Média')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(filtro_mediana, cv2.COLOR_BGR2RGB))
plt.title('Filtro da Mediana')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(filtro_gaussiano, cv2.COLOR_BGR2RGB))
plt.title('Filtro Gaussiano')
plt.axis('off')

plt.tight_layout()
plt.show()
