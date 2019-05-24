import pyqrcode
import png


def qrcode(dog_id):
    q = pyqrcode.create('http://localhost:8000/dog/%s' % dog_id)
    q.png('media/qr/qr_%s' % dog_id+'.png', scale=10)
    print('Qr Code Generate...')