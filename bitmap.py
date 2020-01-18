class bmp():
    def header():
        header = b''
        # file header (everything is little endian)
        header += b'\x42\x4D'         # file type 'BM'
        header += b'\x36\x03\x08\x00' # file size (822 bytes, 0x336)
        header += b'\x00\x00'         # reserved
        header += b'\x00\x00'         # reserved
        header += b'\x36\x00\x00\x00' # offset to image data (0x36)
        # windows BITMAPINFOHEADER (see https:en.wikipedia.org/wiki/BMP_file_format#DIB_header_%28bitmap_information_header%29)
        header += b'\x28\x00\x00\x00' # this header size (40 bytes)
        header += b'\x10\x00\x00\x00' # bitmap width (16) signed int 
        header += b'\x10\x00\x00\x00' # bitmap height (16) signed int
        header += b'\x01\x00'         # color planes (apparently 1)
        header += b'\x18\x00'         # bits per pixel (24-bit color, i.e. 3 bytes for RGB)
        header += b'\x00\x00\x00\x00' # compression (uncompressed)
        header += b'\x00\x00\x00\x00' # raw image size (no need to specify if uncompressed)
        header += b'\x30\x00\x00\x00' # horizontal resolution (in pixels/meter) (helpful for printers)
        header += b'\x30\x00\x00\x00' # vertical   --||--
        header += b'\x00\x00\x00\x00' # colors in color palette (none for 24-bit color)
        header += b'\x00\x00\x00\x00' # important colors (nope)
        # pixel array
        # 16x16 image (little endian, so BGR BGR etc...)
        return header
    
    def mario():
        data = b'\xff\xff\xff\x04\x6b\x6a\xff\xff\xff\xff\xff\xff\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
>>>>>>> 49b4b6c340d300f605935ba450c5e436b104a6fe
\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x04\x6b\x6a\x04\x6b\x6a\
\xff\xff\xff\x25\x9d\xe3\xff\xff\xff\x04\x6b\x6a\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x04\x6b\x6a\x04\x6b\x6a\
\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\xff\xff\xff\x25\x34\xb1\x25\x34\xb1\x04\x6b\x6a\x25\x34\xb1\x25\x34\xb1\x25\x9d\xe3\x25\x34\xb1\x25\x34\xb1\x25\x9d\xe3\x25\x34\xb1\x04\x6b\x6a\x04\x6b\x6a\
\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\
\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\
\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x34\xb1\x04\x6b\x6a\xff\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\x25\x9d\xe3\x04\x6b\x6a\x04\x6b\x6a\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\x25\x9d\xe3\x04\x6b\x6a\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\x25\x9d\xe3\x25\x9d\xe3\x04\x6b\x6a\x25\x9d\xe3\xff\xff\xff\x04\x6b\x6a\x04\x6b\x6a\x04\x6b\x6a\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x9d\xe3\x25\x9d\xe3\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\x25\x34\xb1\xff\xff\xff\xff\xff\xff\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x25\x9d\xe3\x25\x9d\xe3\x25\x9d\xe3'
        return data
    
def genImage(name, header, data):
    image = header + data
    
    with open(name, "wb") as file:
        file.write(image)
