import json

def read_json(filename):
    """Reads .json file and returns contents as dict."""
    with open(filename) as filein:
        dump = json.load(filein)
    return dump

def robust_crop(img, page_size, width=700, height=600):
    x0, y0 = [0.5*xy for xy in page_size]
    x1, x2 = int(x0-.5*width), int(x0+.5*width)
    y1, y2 = int(y0-.5*height), int(y0+0.5*height)
    return img[y1:y2, x1:x2]