import cv2
from glob import glob
mask_lst = glob('../Inpainting/lama/input_data/*_mask.png')

for i in mask_lst:
  img1 = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
  k = cv2.getStructuringElement(cv2.MORPH_RECT, (13,13))
  dst = cv2.dilate(img1, k)

  cv2.imwrite(i[:-4]+"_Dilation_13.png", dst)