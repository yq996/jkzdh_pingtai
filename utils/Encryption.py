import hashlib
import urllib.parse
import base64
import json

def encry(username, password):
    """
    加密函数：将用户名和密码按流程加密处理
    流程：MD5 → 拼接JSON → URL编码 → Base64编码

    Args:
        username (str): 用户名
        password (str): 明文密码

    Returns:
        str: 最终加密后的Base64字符串
    """
    # MD5编码密码
    md5_password = hashlib.md5(password.encode()).hexdigest()
    #    print(md5_password)
    # 组合成JSON
    credentials = {"username": username, "password": md5_password}
    json_data = json.dumps(credentials)

    # URL编码
    url_encoded = urllib.parse.quote(json_data)

    # Base64编码
    base64_encoded = base64.b64encode(url_encoded.encode('utf-8')).decode()

    return base64_encoded

