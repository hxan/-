### 新建AipFace

AipFace是人脸识别的Python SDK客户端，为使用人脸识别的开发人员提供了一系列的交互方法。

参考如下代码新建一个AipFace：

```text
from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
```

在上面代码中，常量`APP_ID`在百度云控制台中创建，常量`API_KEY`与`SECRET_KEY`是在创建完毕应用后，系统分配给用户的，均为字符串，用于标识用户，为访问做签名验证，可在AI服务控制台中的**应用列表**中查看。

**注意**：如您以前是百度云的老用户，其中`API_KEY`对应百度云的“Access Key ID”，`SECRET_KEY`对应百度云的“Access Key Secret”。

### 配置AipFace

如果用户需要配置AipFace的网络请求参数(一般不需要配置)，可以在构造AipFace之后调用接口设置参数，目前只支持以下参数：

| 接口                         | 说明                                           |
| ---------------------------- | ---------------------------------------------- |
| setConnectionTimeoutInMillis | 建立连接的超时时间（单位：毫秒                 |
| setSocketTimeoutInMillis     | 通过打开的连接传输数据的超时时间（单位：毫秒） |

## 接口说明

### 人脸检测

检测请求图片中的人脸，返回人脸位置、72个关键点坐标、及人脸相关属性信息。

检测响应速度，与图片中人脸数量相关，人脸数量较多时响应时间会有些许延长。

典型应用场景：如**人脸属性分析**，**基于人脸关键点的加工分析**，**人脸营销活动**等。

> 五官位置会标记具体坐标；72个关键点坐标也包含具体坐标，但不包含对应位置的详细位置描述。

```text
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用人脸检测 """
client.detect(image);

""" 如果有可选参数 """
options = {}
options["max_face_num"] = 2
options["face_fields"] = "age"

""" 带参数调用人脸检测 """
client.detect(image, options)
```

**人脸检测 请求参数详情**

| 参数名称     | 是否必选 | 类型   | 默认值 | 说明                                                         |
| ------------ | -------- | ------ | ------ | ------------------------------------------------------------ |
| image        | 是       | string |        | 图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式 |
| max_face_num | 否       | string | 1      | 最多处理人脸数目，默认值1                                    |
| face_fields  | 否       | string |        | 包括age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities信息，逗号分隔，默认只返回人脸框、概率和旋转角度 |

**人脸检测 返回数据参数详情**

| 参数                    | 类型     | 必选 | 说明                                                         |
| ----------------------- | -------- | ---- | ------------------------------------------------------------ |
| log_id                  | uint64   | 是   | 日志id                                                       |
| result_num              | uint32   | 是   | 人脸数目                                                     |
| result                  | object[] | 是   | 人脸属性对象的集合                                           |
| +age                    | double   | 否   | 年龄。face_fields包含age时返回                               |
| +beauty                 | double   | 否   | 美丑打分，范围0-100，越大表示越美。face_fields包含beauty时返回 |
| +location               | object   | 是   | 人脸在图片中的位置                                           |
| ++left                  | uint32   | 是   | 人脸区域离左边界的距离                                       |
| ++top                   | uint32   | 是   | 人脸区域离上边界的距离                                       |
| ++width                 | uint32   | 是   | 人脸区域的宽度                                               |
| ++height                | uint32   | 是   | 人脸区域的高度                                               |
| +face_probability       | double   | 是   | 人脸置信度，范围0-1                                          |
| +rotation_angle         | int32    | 是   | 人脸框相对于竖直方向的顺时针旋转角，[-180,180]               |
| +yaw                    | double   | 是   | 三维旋转之左右旋转角[-90(左), 90(右)]                        |
| +pitch                  | double   | 是   | 三维旋转之俯仰角度[-90(上), 90(下)]                          |
| +roll                   | double   | 是   | 平面内旋转角[-180(逆时针), 180(顺时针)]                      |
| +expression             | uint32   | 否   | 表情，0，不笑；1，微笑；2，大笑。face_fields包含expression时返回 |
| +expression_probability | double   | 否   | 表情置信度，范围0~1。face_fields包含expression时返回         |
| +faceshape              | object[] | 否   | 脸型置信度。face_fields包含faceshape时返回                   |
| ++type                  | string   | 是   | 脸型：square/triangle/oval/heart/round                       |
| ++probability           | double   | 是   | 置信度：0~1                                                  |
| +gender                 | string   | 否   | male、female。face_fields包含gender时返回                    |
| +gender_probability     | double   | 否   | 性别置信度，范围0~1。face_fields包含gender时返回             |
| +glasses                | uint32   | 否   | 是否带眼镜，0-无眼镜，1-普通眼镜，2-墨镜。face_fields包含glasses时返回 |
| +glasses_probability    | double   | 否   | 眼镜置信度，范围0~1。face_fields包含glasses时返回            |
| +landmark               | object[] | 否   | 4个关键点位置，左眼中心、右眼中心、鼻尖、嘴中心。face_fields包含landmark时返回 |
| ++x                     | uint32   | 否   | x坐标                                                        |
| ++y                     | uint32   | 否   | y坐标                                                        |
| +landmark72             | object[] | 否   | 72个特征点位置，示例图 。face_fields包含landmark时返回       |
| ++x                     | uint32   | 否   | x坐标                                                        |
| ++y                     | uint32   | 否   | y坐标                                                        |
| +race                   | string   | 否   | yellow、white、black、arabs。face_fields包含race时返回       |
| +race_probability       | double   | 否   | 人种置信度，范围0~1。face_fields包含race时返回               |
| +qualities              | object   | 否   | 人脸质量信息。face_fields包含qualities时返回                 |
| ++occlusion             | object   | 是   | 人脸各部分遮挡的概率,[0, 1],0表示完整，1表示不完整           |
| +++left_eye             | double   | 是   | 左眼                                                         |
| +++right_eye            | double   | 是   | 右眼                                                         |
| +++nose                 | double   | 是   | 鼻子                                                         |
| +++mouth                | double   | 是   | 嘴                                                           |
| +++left_cheek           | double   | 是   | 左脸颊                                                       |
| +++right_cheek          | double   | 是   | 右脸颊                                                       |
| +++chin                 | double   | 是   | 下巴                                                         |
| ++blur                  | double   | 是   | 人脸模糊程度，[0, 1]。0表示清晰，1表示模糊                   |
| ++illumination          | -        | 是   | 取值范围在[0,255],表示脸部区域的光照程度                     |
| ++completeness          | -        | 是   | 人脸完整度，[0, 1]。0表示完整，1表示不完整                   |
| ++type                  | object   | 是   | 真实人脸/卡通人脸置信度                                      |
| +++human                | -        | 是   | 真实人脸置信度，[0, 1]                                       |
| +++cartoon              | -        | 是   | 卡通人脸置信度，[0, 1]                                       |

**人脸检测 返回示例**

```json
{
    "result_num": 1,
    "result": [
        {
            "location": {
                "left": 117,
                "top": 131,
                "width": 172,
                "height": 170
            },
            "face_probability": 1,
            "rotation_angle": 2,
            "yaw": -0.34859421849251,
            "pitch": 2.3033397197723,
            "roll": 1.9135693311691,
            "landmark": [
                {
                    "x": 161.74819946289,
                    "y": 163.30244445801
                },
                ...
            ],
            "landmark72": [
                {
                    "x": 115.86531066895,
                    "y": 170.0546875
                }，
                ...
            ],
            "age": 29.298097610474,
            "beauty": 55.128883361816,
            "expression": 1,
            "expression_probablity": 0.5543018579483,
            "gender": "male",
            "gender_probability": 0.99979132413864,
            "glasses": 0,
            "glasses_probability": 0.99999964237213,
            "race": "yellow",
            "race_probability": 0.99999976158142,
            "qualities": {
                "occlusion": {
                    "left_eye": 0,
                    "right_eye": 0,
                    "nose": 0,
                    "mouth": 0,
                    "left_cheek": 0.0064102564938366,
                    "right_cheek": 0.0057411273010075,
                    "chin": 0
                },
                "blur": 1.1886881756684e-10,
                "illumination": 141,
                "completeness": 1,
                "type": {
                    "human": 0.99935841560364,
                    "cartoon": 0.00064159056637436
                }
            }
        }
    ],
    "log_id": 2493878179101621
}
```