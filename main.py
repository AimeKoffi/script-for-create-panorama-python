from imutils import paths
import imutils
import cv2

def CreatePanoramaPictures(imagesPath):
  imagePaths = sorted(list(paths.list_images(imagesPath)))
  images = []
  # images to stitch list
  for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)
  # stitching
  print("[INFO] stitching images...")
  stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
  (status, stitched) = stitcher.stitch(images) 
  if status == 0:
    return stitched
  # otherwise the stitching failed, likely due to not enough keypoints)
  # being detected
  else:
    return None

# Create a panorama
panorama = CreatePanoramaPictures('imgstostitch')
flag = cv2.imwrite('imgstostitch/panorama.jpg', panorama)
if flag:  
  print("[INFO] stitching images OK.")
else:
  print("[INFO] image stitching failed")      