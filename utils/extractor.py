import logging
import allure
import jsonpath
# from utils.send_request import send_jdbc_request


def json_extractor(case, all, res):
    if case["jsonExData"]:
        with (allure.step("4.JSON提取")):
            res_json = res.json()
            result = jsonpath.jsonpath(res_json, case["check"])[0]
            if result == 200:
                for key, value in eval(case["jsonExData"]).items():
                    value = jsonpath.jsonpath(res_json, value)
                    all[key] = value[0] if len(value) == 1 else value

                status=all.get("status",[])
                hostbody=all.get("hostbody",[])

                if len(hostbody) ==len(status):
                    hostbidy_list=[
                        hostbody for hostbody,status in zip(hostbody,status)
                        if status=="1"
                    ]
                    if hostbidy_list:
                        all["hostbid"]=hostbidy_list
                        logging.info(f"过滤后的hosybody剩余{len(hostbidy_list)}个")
                else:
                    logging.info(f"两个长度不一致！！！")

                logging.info(f"4.JSON提取, 根据{case['jsonExData']}提取数据, 此时全局变量为: {all}")
            else:
                logging.info(f"状态码是{result},响应数据为空！！")

    if case["headeExData"]:
        with allure.step("4.响应头提取"):
            for key, value in eval(case["headeExData"]).items():
                value = res.headers.get(value)
                all[key] = value
            logging.info(f"4.headers提取, 根据{case['headeExData']}提取数据, 此时全局变量为: {all}")


# def jdbc_extractor(case, all):
#     if case["sqlExData"]:
#         with allure.step("4.JDBC提取"):
#             for key, value in eval(case["sqlExData"]).items():
#                 value = send_jdbc_request(value)
#                 all[key] = value
#             logging.info(f"4.JDBC提取, 根据{case['sqlExData']}提取数据, 此时全局变量为: {all}")
