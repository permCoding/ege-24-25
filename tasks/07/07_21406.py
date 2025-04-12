from math import ceil
im1 = 3840 * 2160 * 17
im2 = 1280 * 720 * 5
print(ceil(120*(im1-im2)/8)/1024)