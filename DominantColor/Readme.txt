Brief approach on this problem.

* So here we create a function called DominantColors which accepts the image and the clusters as input. 
* Since opencv reads images in BGR format, it is first converted into RGB format using cv2.cvtColor
* The image is then reshaped to a list of pixels for our computation.
* We then use kmeans clustering method for the said image.
* The kmeans.cluster_centers_ gives us our dominant colors in the image.
* Now the output for this comes out as a list of [R,G,B] numbers.
* So we convert this into hex by using the webcolors library.
* The output is converted into tuple , and then using rgb_to_hex function the said tuple is converted into hex value.
* Now as we do not want any neutral colors, I created a list which contains the hex code for white, black and prominent shades of grey.
* Each dominant hex value is then compared to this list and if the hex value does not match to any of the  list values , it is stored in the database.
* Else it is skipped and we move on to the next hex value.

* At  the end of this program we will have a database which contains image name and its dominant colors hex code without the neutral colors.