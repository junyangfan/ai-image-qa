# save_image.py
import pyautogui
from utils.image_utils import capture_and_save_image
import config  # 导入配置文件

# 截取并保存图片
def save_screenshot():
    capture_and_save_image(config.SCREENSHOT_REGION)

if __name__ == "__main__":
    save_screenshot()
