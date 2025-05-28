# 通用配置

# 屏幕截图区域配置 (x, y, width, height)
SCREENSHOT_REGION = (100, 20, 300, 400)
# 描述
IMAGE_QA = "提取出图片中的问题和选项，从A、B、C、D四个选项中选择一个正确的答案，并给出选择的原因。"
# 截图间隔配置 (秒)
CAPTURE_INTERVAL = 5

# ChatGPT 模型 API 配置
OPENAI_API_KEY = 'apiKey'
OPENAI_BASE_URL = 'https://api.openai.com/v1/chat/completion'
OPENAI_MODEL = 'gpt-4o'

# 星火大模型API的配置，申请地址：https://xinghuo.xfyun.cn/sparkapi
# 修改 SPARKAI_APP_ID、SPARKAI_API_SECRET、SPARKAI_API_KEY 参数，SPARKAI_BASE_URL、SPARKAI_DOMAIN 参数无需修改
SPARKAI_APP_ID = 'appId'
SPARKAI_API_SECRET = 'apiSecret'
SPARKAI_API_KEY = 'apiKey'
SPARKAI_BASE_URL = 'wss://spark-api.cn-huabei-1.xf-yun.com/v2.1/image'
SPARKAI_DOMAIN = 'image'


# 通义千问大模型API的配置，文档/申请地址：https://help.aliyun.com/zh/model-studio/user-guide/vision
# 修改 ALIYUN_API_KEY 参数，ALIYUN_BASE_URL、ALIYUN_MODEL 参数无需修改
ALIYUN_API_KEY = 'apiKey'
ALIYUN_BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions'
ALIYUN_MODEL = 'qwen-vl-max-latest' # 可选模型地址(用VL模型)：https://help.aliyun.com/zh/model-studio/models#94b18818a6ywy
