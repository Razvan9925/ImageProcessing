from PIL import Image
im = Image.open(r"E:\tsts\parrots.bmp")
print(im.format, im.size, im.mode)
width, height = im.size

def readRGB():
    file = open("E:/tsts/output.txt", "w")
    for x in range(width):
        for y in range(height):
            pxl_coord = (x, y)
            r, g, b = im.getpixel(pxl_coord)
            file.write(str(r) + "\n")
            file.write(str(g) + "\n")
            file.write(str(b) + "\n")

    file.close()
    im.close()
    print("LOG: create rgb")

def rgb_to_xyz(input, output, width, height):
    xyz = open(output, "w")

    with open(input, "r") as rgb:
        for i in range(width):
            for j in range(height):
                r = int(rgb.readline())
                g = int(rgb.readline())
                b = int(rgb.readline())

                x = 0.431 * r + 0.342 * g + 0.178 * b
                y = 0.222 * r + 0.707 * g + 0.071 * b
                z = 0.020 * r + 0.130 * g + 0.939 * b

                xyz.write("%d\n%d\n%d\n" % (x, y, z))

    xyz.close()
    print("LOG: rgb to xyz")

#def xyz_to_rgb(input, output, width, height):

    
def main():
    readRGB()
    first_RGB = "E:/tsts/output.txt"
    xyz_file = "E:/tsts/xyz_out.txt"
    rgb_to_xyz(first_RGB, xyz_file, width, height)


if __name__ == "__main__":
    main()