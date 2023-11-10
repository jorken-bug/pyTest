import json

import allure
import pytest
import yaml

from commons.request_all import RequestAll
from commons.util import read_yaml_testcase, write_yaml, read_excel


@allure.feature("TEST")
class Test_Api:

    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("core/token.yaml"))
    def test_get_token(self, caseinfo, request):
        allure.dynamic.title(caseinfo['name'])

        method = caseinfo['request']['method']
        url = f"{request.config.getini('base_url')}{caseinfo['request']['url']}"
        data = caseinfo['request']['params']

        res = RequestAll().all_request(method, url, data=data)

        #获取token
        if 'token' in dict(res.json()).keys():
            write_yaml({"token": res.json()["token"]})

        assert res.status_code == caseinfo['validate']

        with allure.step("验证响应数据"):
            json_data = res.json()

            expected_code = 200
            actual_code = json_data.get("code")

            assert actual_code == expected_code, f"断言失败"

            formatted_json = json.dumps(json_data, ensure_ascii=False, indent=4)  # ensure_ascii定义是否保留原始格式
            formatted_data_json = json.dumps(data, indent=4)

            # 使用allure.dynamic.description_html将响应数据以框内形式展示
            description_html = f"<pre>请求数据：{formatted_data_json}\n\n响应数据：{formatted_json}</pre>"
            allure.dynamic.description_html(description_html)


    @allure.story("数据查询")
    @pytest.mark.parametrize("test_data", read_excel('data/data.xlsx'))
    def test_data_cat(self, test_data, request):
        allure.dynamic.title(test_data['title'])

        method = test_data['type']
        url = f"{request.config.getini('base_url')}{test_data['url']}"

        data = {
            "method": test_data['method']
        }
        #读取yaml文件获取token参数
        with open("extract_token.yaml", "r") as file:
            headers = yaml.safe_load(file)

            # 获取 token 值并添加到请求头中
        token = headers["token"]
        headers = {"gx-token": f"{token}"}

        res = RequestAll().all_request(method, headers=headers, url=url, data=data)

        assert res.status_code == test_data['validate']

        with allure.step("验证响应数据"):
            json_data = res.json()

            formatted_json = json.dumps(json_data, ensure_ascii=False, indent=4)  # ensure_ascii定义是否保留原始格式
            formatted_data_json = json.dumps(data, indent=4)

            # 使用allure.dynamic.description_html将响应数据以框内形式展示
            description_html = f"<pre>请求数据：{formatted_data_json}\n\n响应数据：{formatted_json}</pre>"
            allure.dynamic.description_html(description_html)

            expected_code = 200
            actual_code = json_data.get("code")

            assert actual_code == expected_code, f"断言失败"