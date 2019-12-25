import time

from face_detection import FaceDetection
import os

# 1.获取百度AI授权认证
APPID = "18057918"
APIKEY = "1MK9ChxIVgIGPoagCQ20wPYU"
SECRET_KEY = "RLfRkGrFT0hUwfofTXIYQboSnqwOiBWT"

# 2.相对路径
path = r"../img"
images = os.listdir(path)
print(images)

image = images[1]
image_path = path + "/" + image

print(image)

# 3.创建对象
face = FaceDetection(APPID, APIKEY, SECRET_KEY, image_path)
# 4.调用方法，获取结果
age = face.get_age()
beauty = face.get_score()
gender = face.get_gender()
face_shape = face.get_face_shape()

print(beauty)
print(gender)
print(age)
print(face_shape)
