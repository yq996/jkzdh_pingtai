import ast
import logging
from logging import raiseExceptions

import allure
import jsonpath

from utils.Decrypt import decode_base64


# from utils.send_request import send_jdbc_request


@allure.step("3.HTTP响应断言")
def http_assert(case, res):

    if case["check"]:
        result = jsonpath.jsonpath(res.json(), case["check"])[0]
        # print("111111111111111", jsonpath.jsonpath(res.json(), case["check"])) 结果是数组
        # logging.info(f"3.HTTP响应断言内容: 实际结果({result}) == 预期结果({case['expected']})")
        # expected=case["expected"]
        # if isinstance(expected,str) and expected.startswith('[') and expected.endswith(']'):
        #     try:
        #         expected=ast.literal_eval(expected)
        #     except Exception as e:
        #         raise ValueError(f"期望字符串格式有误：无法转换成列表：{expected},错误信息：{e}")
        expected = case["expected"]
        if isinstance(expected, str) and expected.startswith("[") and expected.endswith("]"):
            try:
                 expected = ast.literal_eval(expected) #安全解析为列表
            except Exception as e:
                raise ValueError(f"期望值字符串格式有误，无法转换成列表：{expected}，错误信息：{e}")
        if isinstance(expected, list):
            assert result in expected
            logging.info(f"实际结果({result}) 在期望值列表 {expected} 中")
        else:
            assert result == expected
            logging.info(f"实际结果({result}) 等于期望值 {expected}")

    else:
        logging.info(f"3.HTTP响应断言内容: 预期结果({case['expected']}) in 实际结果({res.text})")
        assert case["expected"] in res.text

#
# def jdbc_assert(case):
#     if case["sql_check"] and case["sql_expected"]:
#         with allure.step("3.JDBC响应断言"):
#             result = send_jdbc_request(case["sql_check"])
#             logging.info(f"3.JDBC响应断言内容: 实际结果({result}) == 预期结果({case['sql_expected']})")
#             assert result == case["sql_expected"]
