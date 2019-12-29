from functions import breakline, clrscr, take_input, banner_print
from PIL import Image
import os


def resize_img(fPath=None):
    if not fPath:
        fPath = input("Enter the file's path: ")
    base_height = 400
    img = Image.open(fPath)
    h_percent = (base_height / float(img.size[1]))
    w_size = int((float(img.size[0]) * float(h_percent)))
    img = img.resize((w_size, base_height), Image.ANTIALIAS)
    print()
    try:
        os.makedirs(os.path.join(os.path.split(fPath)[0], 'Edited'))
    except FileExistsError:
        print('The Edited folder already exists.')
    path = os.path.join(os.path.split(fPath)[0], 'Edited', os.path.split(fPath)[1])
    img.save(path)
    print(f'Saved as {path}')


def resize_batch():
    path = input('Enter the folder\'s path: ')
    files = os.listdir(path)
    for file in files:
        image_file = False
        try:
            Image.open(os.path.join(path, file))
            image_file = True
        except:
            pass
        if image_file:
            resize_img(os.path.join(path, file))


def main():
    clrscr()
    banner_print("Image Manipulation", font="standard")
    banner_print('-EmperorAj', font='bubble')

    options = ['Edit a single image', 'Edit a batch', 'Exit']
    take_input(options, resize_img, resize_batch, exit)


if __name__ == '__main__':
    main()
