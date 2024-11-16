import requests
from time import sleep
from utils.image_utils import capture_and_convert_to_base64  # 导入通用方法
import config  # 导入配置文件

# 将 Base64 编码的图片数据传递给 OpenAI API
def send_to_openai(image_base64, text):
    url = config.OPENAI_BASE_URL  # OpenAI API 接口地址

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.OPENAI_API_KEY}",  # 使用你的 OpenAI API 密钥
    }

    # 构造请求的 payload
    data = {
        "model": config.OPENAI_MODEL,  # 使用的模型类型，可以根据需要调整
        "messages": [
            {"role": "user", "content": [
                {"type": "text", "text": text},  # 用户发送的文本提示
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
            ]}
        ]
    }

    # 发送 POST 请求
    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            print(result['choices'][0]['message']['content'].replace("**", ""))  # 输出返回的内容
        else:
            print(f"请求失败: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"发送请求时发生错误: {e}")

# 定义全局变量 last_img_base64
last_img_base64 = None

# 定时截图并与上次截图比较，传递图像的 Base64 编码
def capture_periodically(region, interval=config.CAPTURE_INTERVAL):
    global last_img_base64
    while True:
        # 获取当前截图并转换为 Base64
        img_base64 = capture_and_convert_to_base64(region)

        if img_base64 and img_base64 != last_img_base64:
            print("图片已更改，发送到 OpenAI API...")
            # 更新最后一次截图
            last_img_base64 = img_base64
            print(f"发送的图像数据（部分）：{img_base64[:30]}...")  # 打印 base64 字符串的前 30 个字符进行验证

            # 启动请求并将 Base64 图像数据传递给 OpenAI API
            send_to_openai(img_base64, config.IMAGE_QA)  # 传递图像的 Base64 编码和文本
        else:
            print("图片未变化，跳过请求")

        # 等待指定的时间间隔再进行下一次截图
        sleep(interval)

# 主执行部分
if __name__ == '__main__':
    # 直接开始定时截图并将 Base64 图像数据发送到 OpenAI API
    capture_periodically(config.SCREENSHOT_REGION, interval=config.CAPTURE_INTERVAL)
