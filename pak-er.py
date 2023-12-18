import shutil
import base64
import os

FOLDERTOBEPACKED = "template/"
MANIFESTNAME = "manifest.cfg"

def main():
    with open(FOLDERTOBEPACKED + MANIFESTNAME, "r") as cfgContents:
        cleanedList = [line.strip("\n") for line in cfgContents]
        separatedLines = [line.split("=") for line in cleanedList]

    shutil.make_archive(separatedLines[0][1], "zip", FOLDERTOBEPACKED)
    if os.path.isfile(separatedLines[0][1] + ".pak"): os.remove(separatedLines[0][1] + ".pak")
    with open(separatedLines[0][1] + ".zip", "rb") as fileIn, open(separatedLines[0][1] + ".pak", "wb") as fileOut:
        
        base64.encode(fileIn, fileOut)
    if os.path.isfile(separatedLines[0][1] + ".zip"): os.remove(separatedLines[0][1] + ".zip")

if __name__ == "__main__":
    main()