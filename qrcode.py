import pyqrcode
import png
from pyqrcode import QRCode
qrcode_string="https://www.instagram.com/shaik_aneef_ani"
url=pyqrcode.create(qrcode_string)
url.png("myqrcode.png",scale=6)
