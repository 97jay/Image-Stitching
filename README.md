# Image-Stitching

The goal of this task is to stitch two images together to construct a panorama image. First, you need 
to find keypoints (points of interest) in the given images using corner detector, e.g., Harris detector. 
Then, you use SIFT or other feature descriptors to extract features for these keypoints. Next, you 
should match the keypoints between two images by comparing their feature distance. After having the 
matched point pairs, you are able to compute the homography matrix using RANSAC algorithm. Finally, you 
can use the homography matrix to stitch the two given images.
