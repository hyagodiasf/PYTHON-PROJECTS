import qrcode as qr

img_qrcode = qr.make("https://github.com/hyagodiasf")
img_qrcode.save("github_hyagodias.png")