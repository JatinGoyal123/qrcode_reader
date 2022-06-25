# Generator Code
# pip install pyqrcode
# pip install pypng
import pyqrcode as qr
content="www.techsrijan.com"
qr_code=qr.create(content) 
qr_code.png("mywebsite.png",scale=5)
print('QrCode Generated Successfully')

#Scanner code
# pip install pyzbar
# pip install pillow
from pyzbar.pyzbar import decode
from PIL import Image
img=Image.open('mywebsite.png')
cont=decode(img)
print(cont[0].data.decode())