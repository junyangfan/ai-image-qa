import requests
from time import sleep
from utils.image_utils import capture_and_convert_to_base64  # 导入通用方法
import config  # 导入配置文件

# 将Base64图片传递给阿里云AI模型
def send_to_aliyun_ai(image_base64, text):
    url = config.ALIYUN_BASE_URL

    headers = {
        "Authorization": f"Bearer {config.ALIYUN_API_KEY}",  # 使用API Key
    }

    # 构造请求的 payload
    data = {
        "model": config.ALIYUN_MODEL,  # 使用阿里云的 AI 模型
        "messages": [
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}},
                {"type": "text", "text": config.IMAGE_QA}
            ]}
        ]
    }

    # 发送POST请求
    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            print(result['choices'][0]['message']['content'])  # 输出返回的内容
        else:
            print(f"请求失败: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"发送请求时发生错误: {e}")

# 定义全局变量 last_img_base64
last_img_base64 = None

# 定时截图并与上次截图比较，传递图像的base64
def capture_periodically(region, interval=config.CAPTURE_INTERVAL):
    global last_img_base64
    while True:
        # 获取当前截图并转换为base64
        img_base64 = capture_and_convert_to_base64(region)

        if img_base64 and img_base64 != last_img_base64:
            print("图片已更改，发送到AI模型...")
            # 更新最后一次截图
            last_img_base64 = img_base64
            print(f"发送的图像数据（部分）：{img_base64[:30]}...")  # 打印base64字符串的前30个字符进行验证

            # 启动请求并将base64图像数据传递给阿里云AI模型
            send_to_aliyun_ai(img_base64, config.IMAGE_QA)  # 传递图像的Base64编码和文本
        else:
            print("图片未变化，跳过请求")

        # 等待指定的时间间隔再进行下一次截图
        sleep(interval)


if __name__ == '__main__':
    # 直接开始定时截图并将base64图像数据发送到AI模型
    capture_periodically(config.SCREENSHOT_REGION, interval=config.CAPTURE_INTERVAL)
