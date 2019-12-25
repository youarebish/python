from aip import AipFace
import base64
import os


class FaceDetection:

    def __init__(self, app_id, api_key, secret_key, image):
        self.__client = AipFace(app_id, api_key, secret_key)
        self.__image = image

    def __get_image(self):
        """拼接图片路径，并对图片进行base64编码"""
        base_image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img")
        image = os.path.join(base_image_path, self.__image)
        try:
            with open(image, 'rb') as f:
                image_base64 = base64.b64encode(f.read())
                return image_base64.decode('utf-8')
        except FileNotFoundError:
            return

    def __result(self):
        """获取图片审核的结果"""
        image = self.__get_image()
        options = {
            "max_face_num": 3,
            "face_field": "age,beauty,expression,face_shape,gender"
        }
        # print('image', image)
        if image:
            self.result = self.__client.detect(image, "BASE64", options)
            if self.result.get('error_msg', '') == 'image check fail':
                self.result = {'id': 'asdf',
                               'result': {
                                   'face_list': [{'age': 0,
                                                  'beauty': 0,
                                                  'face_shape': {'type': 'heart'},
                                                  'gender': {'type': 'female'}}]}}
        else:
            pass
        # setattr(self, 'result', self.result)

    def get_age(self):
        """获取年龄，返回值整型"""
        if not hasattr(self, 'result'):
            pass
        self.__result()
        if self.result:

            if self.result.get('id', '') == 'asdf':
                return '脸未找到'
            if not self.result.get('error_code'):
                return self.result.get("result").get("face_list")[0].get("age")
            return self.result
        return "图片未找到"

    def get_gender(self):
        """获取性别信息
        女孩：返回False，男孩返回：True"""
        if not hasattr(self, 'result'):
            self.__result()
        if self.result.get('id', '') == 'asdf':
            return '脸未找到'
        if self.result:
            if not self.result.get('error_code'):
                return True if self.result.get("result").get("face_list")[0].get("gender").get(
                    'type') == "male" else False
            return self.result
        return "图片未找到"

    def get_score(self):
        """获取颜值得分，返回值浮点型"""
        if not hasattr(self, 'result'):
            self.__result()
            if self.result.get('id', '') == 'asdf':
                return 0
        if self.result:
            if not self.result.get('error_code'):
                return self.result.get("result").get("face_list")[0].get("beauty")
            return self.result
        return "图片未找到"

    def get_face_shape(self):
        """获取脸型，返回值字符串"""
        if not hasattr(self, 'result'):
            self.__result()
            if self.result.get('id', '') == 'asdf':
                return '脸未找到'
        if self.result:
            if not self.result.get('error_code'):
                return self.result.get("result").get("face_list")[0].get("face_shape").get("type")
            return self.result
        return "图片未找到"
