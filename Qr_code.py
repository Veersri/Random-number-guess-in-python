# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 22:33:52 2025

@author: veerk
"""

import qrcode
from PIL import Image

# Create a QRCode object with custom settings
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (up to ~30%)
    box_size=20,  # Size of each box in the QR code grid
    border=4  # Width of the border (minimum is 4 for QR standards)
)

# This adds the actual URL or text that will be stored in the QR code
qr.add_data("add your url here ==")
qr.make(fit=True)  # Automatically adjusts the QR code size to fit the data

# Create the QR code image with custom fill and background colors
# fill_color sets the color of the QR code blocks
# back_color sets the background color behind the QR code
img = qr.make_image(fill_color="green", back_color="white")

# Save the QR code as an SVG file for high-quality scalable format
img.save("insta_id.svg")   

# Display the QR code image in the default image viewer
img.show()
