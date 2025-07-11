 # Importing library
import my

# Data to encode
data = "GeeksforGeeks"

# Creating an instance of QRCode class
qr = my.QRCode(version = 1,
                   box_size = 10,
                   border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')

img.save('MyQRCode2.png')