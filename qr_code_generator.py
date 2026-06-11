import qrcode

def generate_qr_code(data, filename):
    if not data.strip():
        print("Error: Data cannot be empty.")
        return

    if not filename.endswith(".png"):
        filename += ".png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    try:
        img.save(filename)
        print(f"QR code generated and saved as {filename}.")
    except Exception as e:
        print("Error saving file:", e)

if __name__ == "__main__":
    data = input("Enter the text or URL for the QR code: ")
    filename = input("Enter the filename: ")
    generate_qr_code(data, filename)