
from aip import AipFace

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

APP_ID = '19492926'
API_KEY = 'a8rMl8rs5udD8j96d8Hb9yIE'
SECRET_KEY = 'nAEZD2dRwEyKLLS9OLTX7GdZq0OvHPwp'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
image = get_file_content('/home/l/ex.jpg')

options = {}
#options["max_face_num"] = 1
#options["face_fields"] = "age"
result = client.detect(image, options)
print(result)
#print(image)
