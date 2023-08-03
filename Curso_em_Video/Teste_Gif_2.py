#Não rodou...sabe Deus o porque
import cv2
import imageio

img = cv2.imread("Luciene.jpg")
f = []

for i in range(50, 0, -1):
    ed = cv2.Canny(img, 100+i, 100+(2*i))
    f.append(ed)

with imageio.get_writer("Luciene.gif", mode="I") as writer:
    for idx, frame in enumerate(f):
        writer.append_data(frame)

print('Fim')