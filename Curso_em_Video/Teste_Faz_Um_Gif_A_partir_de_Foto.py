#Eu pensei que o programa não estava rodando, mas ele faz o gif e vc roda no Teste_Gif.py aqui na lista
import cv2
import imageio

img = cv2.imread("Amigos.jpg")
f = []

for i in range(100, 0, -1):
    ed = cv2.Canny(img, 100+i, 100+(2*i))
    f.append(ed)

with imageio.get_writer("Amigos.gif", mode="I") as writer:
    for idx, frame in enumerate(f):
        writer.append_data(frame)

print('Fim')