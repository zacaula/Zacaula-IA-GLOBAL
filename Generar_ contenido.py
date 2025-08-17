from PIL import Image
import numpy as np
def generar_imagen():
  imagen = np.random.rand(256, 256, 3)
  imagen = imagen * 255
  imagen = imagen.astype(np.uint8)
  img = Image.fromarray(imagen)
  img.save('imagen_generada.png')
generar_imagen()
