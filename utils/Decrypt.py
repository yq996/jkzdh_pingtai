import base64
import re


def decode_base64(encoded_str: str) -> str:
    """
    检测并解码Base64字符串，支持标准和URL安全格式

    参数:
        encoded_str (str): 待检测和解码的字符串

    返回:
        str: 若为Base64编码则返回解码后的原始字符串，否则返回原字符串

    异常:
        ValueError: 当输入的Base64字符串格式无效时抛出
    """
    # 移除可能存在的换行符和空格
    encoded_str = encoded_str.strip()

    # 判断是否为Base64编码的正则表达式
    # 标准Base64字符集: A-Z, a-z, 0-9, +, /, =
    # URL安全Base64字符集: A-Z, a-z, 0-9, -, _, =
    base64_pattern = r'^[A-Za-z0-9+/=_-]+$'

    # 检查长度是否符合Base64要求（必须是4的倍数，允许填充）
    if len(encoded_str) % 4 not in (0, 2, 3):
        return encoded_str

    # 检查是否只包含Base64字符
    if not re.match(base64_pattern, encoded_str):
        return encoded_str

    try:
        # 尝试标准Base64解码
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode('utf-8')
    except (base64.binascii.Error, UnicodeDecodeError):
        try:
            # 尝试URL安全的Base64解码
            # 替换'-'为'+'，'_'为'/'，并添加必要的填充字符'='
            padding_needed = len(encoded_str) % 4
            if padding_needed:
                encoded_str += '=' * (4 - padding_needed)

            encoded_str = encoded_str.replace('-', '+').replace('_', '/')
            decoded_bytes = base64.b64decode(encoded_str)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            # 不是有效的Base64，返回原始字符串
            return encoded_str


# 示例用法
if __name__ == "__main__":
    # 标准Base64
    encoded = "SGVsbG8gd29ybGQ="
    print(decode_base64(encoded))  # 输出: Hello world

    # URL安全的Base64（无填充）
    encoded_url_safe = "SGVsbG8gd29ybGQ"
    print(decode_base64(encoded_url_safe))  # 输出: Hello world

    # 非Base64字符串
    normal_str = "Hello world"
    print(decode_base64(normal_str))  # 输出: Hello world

    # 包含非法字符的字符串
    invalid_str = "Hello@world!"
    print(decode_base64(invalid_str))  # 输出: Hello@world!

    # 解密获取登录信息响应数据
    res_str="eyJjb2RlIjoyMDAsIm1zZyI6InN1Y2Nlc3MiLCJkYXRhIjp7InBhZ2UiOnsibGFuZ3VhZ2UiOiIiLCJ0aXRsZSI6Iuinhumfs+mikee7vOWQiOeuoeeQhuW5s+WPsCIsImxvZ29fcGF0aCI6Imh0dHBzOlwvXC8xOTIuMTY4LjEwMi43MTo1NDQzXC9pbWFnZXNcL2xvZ29cL2xvZ2luX2ZpbGVfbG9nb18wLnBuZyIsImJhY2tncm91bmRfcGF0aCI6Imh0dHBzOlwvXC8xOTIuMTY4LjEwMi43MTo1NDQzXC9pbWFnZXNcL2JhY2tncm91cFwvYmdfMDQucG5nIiwiaXNfY2FwdGNoYSI6MCwiY2FwdGNoYV9wYXRoIjoiXC9yZXN0XC9pbmRleFwvY2FwdGNoYVwvZ2V0PzE9MSIsImRuYW1lIjoi6K2m57+85YaF6YOo5rWL6K+V6KeG6Z+z6aKR57u85ZCI566h55CG5bmz5Y+wIiwic2l0ZSI6Iuinhumfs+mikee7vOWQiOeuoeeQhuW5s+WPsCJ9LCJ3YXJubmluZyI6eyJpc19leHBpcmVkX3Nvb24iOjAsImV4cGlyZWRfZGF0ZSI6IjIwMjUtMTAtMjEifSwiZm9vdGVyIjp7InN1cHBvcnQiOiLmt7HlnLPorabnv7wiLCJ0ZWxlcGhvbmUiOiI0MDAtNjk3NTU1MiIsInZlcnNpb24iOiJaSEdMLUJaLTcuMS4wLjE4R1pDTEQwMSIsImlzX2NvcHlyaWdodCI6MCwiY29weXJpZ2h0IjoiIiwiZG5hbWUiOiLorabnv7zlhoXpg6jmtYvor5UiLCJuYW1lIjoi6K2m57+8In0sImlzX3NldF9zaGEyNTYiOjAsImxhbmd1YWdlIjoiemgiLCJhcHAiOmZhbHNlLCJhcHBfZG93bl91cmwiOiIiLCJhcHBfY29uZmlnIjp7ImlwIjoiMTkyLjE2OC4xMDIuNzEiLCJwb3J0IjoiNTQ0MyJ9LCJhcHBfY29kZV9zd2l0Y2giOiIwIiwiY2VydF9kb3duX3VybCI6Imh0dHBzOlwvXC8xOTIuMTY4LjEwMi43MTo1NDQzXC9pbWFnZXNcL3BsYXllclwvY2VydC56aXAiLCJwb3BfdXBzX2NvbmZpcm0iOjB9fQ=="
    print(decode_base64(res_str))