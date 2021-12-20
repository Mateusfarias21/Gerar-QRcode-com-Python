import pyqrcode
import png

qrcode = pyqrcode.create("http://centralcliente.proocupacional.com.br/FichaClinica")

qrcode.png ("FichaClinica.png", scale=6)
