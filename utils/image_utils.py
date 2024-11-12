# image_utils.py
import pyautogui
import base64
from io import BytesIO
import config  # 导入配置文件

# 截图并转换为base64格式
def capture_and_convert_to_base64(region):
    try:
        # 截取屏幕指定区域
        screenshot = pyautogui.screenshot(region=region)

        # 将截图保存为内存中的字节流
        img_byte_arr = BytesIO()
        screenshot.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)

        # 将字节流转换为base64编码
        img_base64 = base64.b64encode(img_byte_arr.read()).decode('utf-8')

        # 确保 Base64 编码有效
        if not img_base64 or len(img_base64) < 10:
            print("无效的 Base64 数据，截图可能失败")
            return None

        return img_base64

    except Exception as e:
        print(f"截图或转换失败: {e}")
        return None

# 保存截图到本地文件
def capture_and_save_image(region, file_name="screenshot.png"):
    try:
        # 截取屏幕指定区域
        screenshot = pyautogui.screenshot(region=region)

        # 将截图保存为本地文件
        screenshot.save(file_name)
        print(f"本地图片已保存为 '{file_name}'")

    except Exception as e:
        print(f"截图保存失败: {e}")
