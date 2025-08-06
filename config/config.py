# 环境基准地址
BASE_URL = "https://192.168.102.71:5443/"
# jyadmin    Jy26957381
# excel格式的测试用例文件配置
EXCEL_FILE = "./data/测试用例完整版.xlsx"
SHEET_NAME = "Sheet1"

# mysql配置
# DB_HOST = ""
# DB_PORT = 3306
# DB_NAME = ""
# DB_USER = ""
# DB_PASSWORD = ""

# mysql资源销毁
SQL1 = 'DELETE FROM users WHERE id = (SELECT id FROM (SELECT MAX(id) AS id FROM users) AS temp); '
# SQL2 = ''
# SQL3 = ''

