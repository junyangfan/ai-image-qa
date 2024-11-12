# 通用配置

# 截图区域配置 (x, y, width, height)
SCREENSHOT_REGION = (100, 280, 300, 400)
# 描述
IMAGE_QA = "提取出图片中的问题和选项，从A、B、C、D四个选项中选择一个正确的答案，并给出选择的原因。"
# 截图间隔配置 (秒)
CAPTURE_INTERVAL = 5



# 星火大模型API的配置，申请地址：https://xinghuo.xfyun.cn/sparkapi
SPARKAI_APP_ID = 'appId'
SPARKAI_API_SECRET = 'apiSecret'
SPARKAI_API_KEY = 'apiKey'
SPARKAI_URL = 'wss://spark-api.cn-huabei-1.xf-yun.com/v2.1/image'
SPARKAI_DOMAIN = 'image'


# 通义千问大模型API的配置，文档/申请地址：https://help.aliyun.com/zh/model-studio/user-guide/vision
ALIYUN_BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions'
ALIYUN_MODEL = 'qwen-vl-max-latest'
ALIYUN_API_KEY = 'apiKey'

