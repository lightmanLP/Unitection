from os import listdir as LD
from PIL import Image, ImageOps

for i in LD():
 if not(i.endswith('.png')):
  continue
 image = Image.open(i)
 if image.mode == 'RGBA':
  r,g,b,a = image.split()
  Image.merge('RGBA',list(ImageOps.invert(Image.merge('RGB', (r,g,b))).split())+[a]).save(i)
 else:
  ImageOps.invert(image).save(i)
 print(i)