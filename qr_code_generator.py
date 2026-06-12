import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the file name: ').strip()

if not data:
    print('No data provided. Exiting.')
    exit()

if not filename:
    print('No filename provided. Exiting.')
    exit()

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')