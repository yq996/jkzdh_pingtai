import json
import openpyxl
from config.config import *
from utils.Encryption import encry


# from utils.Encryption import md5_hash


def read_excel(file_path=EXCEL_FILE, sheet_name=SHEET_NAME):
    # 打开 excel 文件
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook[sheet_name]

    data = []
    keys = [cell.value for cell in worksheet[2]]  # 获取表头行

    for row in worksheet.iter_rows(min_row=3, values_only=True):
        # 跳过空行
        if not any(row):
            continue

        dict_data = dict(zip(keys, row))

        # 只处理is_true为True的行
        if dict_data.get("is_true"):
            # 处理密码所在的字段
            json_str = dict_data.get("json")
            print("1",json_str)
            # 检查json字段是否存在且非空
            if json_str and isinstance(json_str, str):
                try:
                    # 解析JSON字符串
                    json_data = json.loads(json_str)
                    print(2,json_data)
                    if "login_info" in json_data:
                        login_info_data = json_data["login_info"]
                        print(3,login_info_data)
                        # 如果JSON中包含password字段，进行加密
                        if "password" in login_info_data and "username" in login_info_data:
                            original_name = str(login_info_data["username"])
                            original_pwd = str(login_info_data["password"])
                            encrypted_data = encry(original_name,original_pwd)
                            print(4,encrypted_data)
                            json_data["login_info"] = encrypted_data
                            print(5,json_data)
                            # 更新原始数据中的json字段
                            dict_data["json"] = json.dumps(json_data)
                            print(6,dict_data)


                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {json_str} - {e}")
                    # 可以选择跳过这个测试用例或保留原始数据
            else:
                print(f"警告: 测试用例 '{dict_data.get('title', '未知')}' 的json字段为空或非字符串")

            data.append(dict_data)
            print('7',data)
    workbook.close()
    return data


