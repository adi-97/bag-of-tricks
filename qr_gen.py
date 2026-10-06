import qrcode
from qrcode.constants import ERROR_CORRECT_M


def generate_qr(url, output="qrcode.png", box_size=10, border=4, fill="black", back="yellow"):
    url = url.strip()
    if "://" not in url:
        url = "https://" + url

    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_M, box_size=box_size, border=border)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color=fill, back_color=back).save(output)
    return output

#generate_qr(<add your url here>)