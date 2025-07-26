import pytesseract
from PIL import Image
import cv2


# 设置tesseract路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Y7000\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def preprocess_image(image_path):
    """预处理图片"""
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError

    # 将图片转化为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用高斯模糊去噪
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 二值化处理（使用Otsu方法自动确定阈值）
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    return binary


def recognize_captcha(image_path):
    """使用Tesseract OCR 识别验证码"""
    # 预处理图像
    processed_image = preprocess_image(image_path)

    # 将OpenCV的Numpy数组转化为PIL图像
    pil_image = Image.fromarray(processed_image)

    # 使用Tesseract 进行OCR 识别
    text = pytesseract.image_to_string(pil_image, config='--psm 6')

    # 返回识别结果
    return text.strip()


# 验证码图像路径
captcha_image = 'img_data.jpg'

# 识别验证码
result = recognize_captcha(captcha_image)
print(f'识别的验证码是：{result}')
