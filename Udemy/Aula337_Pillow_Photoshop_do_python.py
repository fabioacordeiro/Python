# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂

from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / ' new.JPG'

pil_image = Image.open(ORIGINAL)
print(pil_image.size)
width, height = pil_image.size
exif = pil_image.info['exif']

# Podemos ver que na nova definição de tamanho temos uma regra de 3
# width     new_width
# height    ??
# Podemos utilizar a regra de 3 para obter a nova largura ou altura
new_width = 640
new_height = round(height * new_width / width)
# O resize abaixo vai dimensionar com os novos valores
new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # A opção abaixo exif ele mantem as informações da imagem como qual câmera foi tirada, tamanho, e outros parâmetros, achei desnecessário manter além de aumentar o tamanho da imagem.
    # exif=exif,
)
