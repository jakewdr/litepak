import base64
import zipfile
from io import BytesIO, StringIO
from timeit import default_timer as timer
from PIL import Image

PAKNAME = "Template.pak"

def decodeText():
    start = timer()
    with open(PAKNAME, "rb") as pakFile:
        decodedPakContents = BytesIO(base64.b64decode(pakFile.read()))
    pakFileUnpacked = zipfile.ZipFile(decodedPakContents, "r")
    unpackedManifest = str(pakFileUnpacked.read("manifest.cfg").decode('UTF-8')).replace('\r', '')
    end = timer()
    print(str(end - start))

def decodeImage():
    with open(PAKNAME, "rb") as pakFile:
        decodedPakContents = BytesIO(base64.b64decode(pakFile.read()))
    pakFileUnpacked = zipfile.ZipFile(decodedPakContents, "r")
    image = pakFileUnpacked.read("images/neco.png")
    with open('neco.png', "wb") as file: 
        file.write(image)

if __name__ == "__main__":
    #decodeText()
    decodeImage()