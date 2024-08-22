import cv2
import numpy as np

sample_img = cv2.imread("sample4.jpg")

ideal_img = cv2.imread("ideal.jpg")

blank_sample = np.zeros(sample_img.shape , dtype="uint8")     # to make the blank as the size of the img

gray_sample = cv2.cvtColor(sample_img , cv2.COLOR_BGR2GRAY)
gray_ideal = cv2.cvtColor(ideal_img , cv2.COLOR_BGR2GRAY)


bitXor = cv2.bitwise_xor(gray_ideal , gray_sample)


# for Ideal One

_ , thresh = cv2.threshold(gray_ideal , 136 , 255 , cv2.THRESH_BINARY)

contours , hierachies = cv2.findContours(thresh , cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)    # Retr_list to make the countours in list and you use the method to detction

# --------------------------------------------
# for Difference One

_ , thresh_2 = cv2.threshold(bitXor , 136 , 255 , cv2.THRESH_BINARY)

contours_2 , _ = cv2.findContours(thresh_2 , cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)    # Retr_list to make the countours in list and you use the method to detction

broken_count = 0
worn_count = 0
for contour in contours_2:
    area = cv2.contourArea(contour)         # to define the area of the contour
    if area > 20 and area < 450:
        worn_count += 1
    elif area > 20 and area < 550:
        broken_count += 1

print(f"Worn count is :{worn_count}")
print(f"Broken count is :{broken_count}")
cv2.drawContours(blank_sample ,contours_2 , -1 , (0 , 0 , 255) , 2)      # to draw the contours , -1 to draw all of them and color and 2 for the thickness

cv2.imshow("Contours drawn in Difference " , blank_sample)

# --------------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX
if broken_count == 0 and worn_count ==0:
    sample_img = cv2.putText(sample_img , "Normal Gear" ,(10 , 550) , font , 0.5 , (255 , 255 , 255) , 1 , cv2.LINE_AA)
    
else:
    text =  "This Gear Has "+ str(worn_count) + " Worn Teeth and " + str(broken_count) + " Broken Teeth"
    sample_img = cv2.putText(sample_img ,text ,(10 , 550) , font , 0.5 , (255 , 255 , 255) , 1 , cv2.LINE_AA)
    
cv2.imshow("The Sample Image" , sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
