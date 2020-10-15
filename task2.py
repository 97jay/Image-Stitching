"""
Image Stitching Problem
(Due date: Oct. 23, 3 P.M., 2019)
The goal of this task is to stitch two images of overlap into one image.
To this end, you need to find feature points of interest in one image, and then find
the corresponding ones in another image. After this, you can simply stitch the two images
by aligning the matched feature points.
For simplicity, the input two images are only clipped along the horizontal direction, which
means you only need to find the corresponding features in the same rows to achieve image stiching.

Do NOT modify the code provided to you.
You are allowed use APIs provided by numpy and opencv, except “cv2.findHomography()” and
APIs that have “stitch”, “Stitch”, “match” or “Match” in their names, e.g., “cv2.BFMatcher()” and
“cv2.Stitcher.create()”.
"""
import cv2
import numpy as np
import random

def solution(left_img, right_img):
    """
    :param left_img:
    :param right_img:
    :return: you need to return the result image which is stitched by left_img and right_img
    """
    limg=cv2.cvtColor(left_img,cv2.COLOR_BGR2GRAY)
    rimg=cv2.cvtColor(right_img,cv2.COLOR_BGR2GRAY)
    sift=cv2.xfeatures2d.SIFT_create()
    kp1,des1=sift.detectAndCompute(limg,None)
    kp2,des2=sift.detectAndCompute(rimg,None)
    mat=cv2.BFMatcher()
    matches=mat.knnMatch(des2,des1,k=2)
    good_match=[]
    for l1,r1 in matches:
        if l1.distance<0.6*r1.distance:
            good_match.append(l1)
    src_pts=np.array([tuple([int(pos) for pos in kp2[z.queryIdx].pt]) for z in good_match])
    dst_pts=np.array([tuple([int(pos) for pos in kp1[z.trainIdx].pt]) for z in good_match])
    h,stat=cv2.findHomography(src_pts,dst_pts,cv2.RANSAC,5.0)
    final_img=cv2.warpPerspective(right_img,h,(left_img.shape[1] + right_img.shape[1],left_img.shape[0]))
    final_img[0:left_img.shape[0],0:left_img.shape[1]]=left_img

    return final_img
    #raise NotImplementedError
    

if __name__ == "__main__":
    left_img = cv2.imread('left.jpg')
    right_img = cv2.imread('right.jpg')
    result_image = solution(left_img, right_img)
    cv2.imwrite('results/task2_result.jpg',result_image)


