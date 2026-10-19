#!/usr/bin/env python3
"""Report exact raster differences; caller owns any disclosed acceptance tolerance."""
from PIL import Image,ImageChops
import sys,json
A=Image.open(sys.argv[1]).convert('RGB');B=Image.open(sys.argv[2]).convert('RGB')
assert A.size==B.size
D=ImageChops.difference(A,B);hist=D.histogram();max_delta=max(hi for lo,hi in D.getextrema());changed=sum(p!=(0,0,0) for p in D.getdata())
print(json.dumps({'different_pixels':changed,'pixels':A.width*A.height,'max_channel_delta':max_delta,'bounding_box':D.getbbox()}))
