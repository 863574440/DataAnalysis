from PIL import Image
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from skimage import color


def load_image(path):
    img = Image.open(path)
    data = []
    width, height = img.size
    for i in range(width):
        for j in range(height):
            rgb = img.getpixel((i, j))
            data.append(list(rgb))
    img.close()
    mms = MinMaxScaler()
    data = mms.fit_transform(data)
    return data, width, height


def train_model(train_x, width, height):
    kmeans = KMeans(n_clusters=16)
    kmeans.fit(train_x)
    label = kmeans.predict(train_x)

    label = label.reshape([width, height])
    # pic_mark = Image.new("rgb", (width, height))
    #
    # for x in range(width):
    #     for y in range(height):
    #         # 根据类别设置图像灰度, 类别 0 灰度值为 255， 类别 1 灰度值为 127
    #         pic_mark.putpixel((x, y), int(256 / (label[x][y] + 1)) - 1)
    # pic_mark.save("weixin_mark.jpg", "JPEG")

    label_color = (color.label2rgb(label) * 255).astype(np.uint8)
    label_color = label_color.transpose(1, 0, 2)
    images = Image.fromarray(label_color)
    images.save('weixin_mark_color.jpg')

    # plt.imshow(pic_mark)
    # plt.show()


def main():
    path = "./data/weixin.jpg"
    train_x, width, height = load_image(path)
    train_model(train_x, width, height)


if __name__ == '__main__':
    main()
