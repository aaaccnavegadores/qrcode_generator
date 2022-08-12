'''pip install qrcode[pil]'''
import qrcode
 
data = input("Insira o Link: ")
name = input("Digite o nome para ser salvo (com .jpg): ")

'''dimensoes da imagem'''
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image()
img.save(name)