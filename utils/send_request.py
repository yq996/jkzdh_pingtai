import logging
import json
import allure
import pymysql
import requests
from config.config import *
from utils.Decrypt import decode_base64


@allure.step("2.发送HTTP请求")
def send_http_request(**request_data):
    res = requests.request(**request_data, verify=False)

    # 1. 解密响应文本
    decrypted_text = decode_base64(res.text)

    # 2. 替换原始响应的内容（让 res.json() 解析解密后的文本）
    # 注意：_content 是 bytes 类型，需将解密后的文本转为 bytes
    res._content = decrypted_text.encode('utf-8')

    # 3. 日志输出
    logging.info(f"响应头为：{res.headers}")
    logging.info(f"原始响应文本为: {res.text}")  # 原始加密内容
    logging.info(f"解密后的响应内容为: {decrypted_text}")  # 解密后内容

    # 4. 验证 res.json() 是否可用（此时解析的是解密后的内容）
    try:
        logging.info(f"解密后响应JSON为: {res.json()}")
    except json.JSONDecodeError:
        logging.warning("解密后的内容仍无法解析为JSON")

    return res


# def send_jdbc_request(sql, index=0):
#     conn = pymysql.Connect(
#         host=DB_HOST,
#         port=DB_PORT,
#         database=DB_NAME,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         charset="utf8"
#     )
#     cur = conn.cursor()
#     cur.execute(sql)
#     result = cur.fetchone()
#     cur.close()
#     conn.close()
#     return result[index]
