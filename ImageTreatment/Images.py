from PIL import Image

class ImageInfo:
    def GetImageRes(imagepath):
        image=Image.open(imagepath)
        resolution = image.size
        return resolution
