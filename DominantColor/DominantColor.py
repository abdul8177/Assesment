import cv2
from sklearn.cluster import KMeans
from webcolors import rgb_to_hex
import glob
import sqlite3



def dominantColors(pic, k):
    # convert to rgb from bgr
    img = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)

    # reshaping to a list of pixels
    img = img.reshape((img.shape[0] * img.shape[1], 3))

    # using k-means to cluster pixels
    kmeans = KMeans(n_clusters=k)
    kmeans.fit_predict(img)

    # the cluster centers are our dominant colors.
    COLORS = kmeans.cluster_centers_

    # save labels
    LABELS = kmeans.labels_

    # returning after converting to integer from float
    return COLORS.astype(int)


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS dominantColor(Image TEXT, Color BLOB)")

clusters = 3
i =0

# This is a list of all the neutral colors( white , black and prominent shades of grey
neutral = ['#000000', '#080808', '#101010', '#181818', '#202020', '#282828', '#303030', '#383838', '#404040', '#484848',
           '#505050', '#585858', '#606060', '#686868', '#696969', '#707070', '#787878', '#808080', '#888888', '#909090',
           '#989898', '#a0a0a0', '#a8a8a8', '#a9a9a9', '#b0b0b0', '#b8b8b8', '#bebebe', '#c0c0c0', '#c8c8c8', '#d0d0d0',
           '#d3d3d3', '#d8d8dd8', '#dcdcdc', '#e0e0e0', '#e8e8e8', '#f0f0f0', '#f5f5f5', '#f8f8f8', '#ffffff']
conn = sqlite3.connect('ImageColor.db')
c = conn.cursor()

create_table()

for img in glob.glob('pics/*.jpg'):
    pic = cv2.imread(img)
    colors = dominantColors(pic, clusters)

    for i in range(0, len(colors)):
        cov = tuple(colors[i])
        cov = rgb_to_hex(cov)
        if cov in neutral:
            continue
        # t = int(time.time())
        # time = str(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))
        c.execute("INSERT INTO dominantColor(Image, Color) VALUES (?, ?)",
              (img, cov))
        conn.commit()
c.close()
conn.close()
