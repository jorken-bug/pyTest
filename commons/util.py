import os

import openpyxl
import yaml


# 写入
def write_yaml(data):
    with open(os.getcwd() + '/extract_token.yaml', encoding="utf-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)

# 读取
def read_yaml(key):
    with open(os.getcwd() + '/extract_token.yaml', encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value[key]

# 清空
def clear_yaml():
    with open(os.getcwd() + '/extract_token.yaml', encoding="utf-8", mode="w") as f:
        f.truncate()

# 读取yaml文件
def read_yaml_testcase(yamlpath):
    yaml_full_path = os.path.join(os.getcwd(), yamlpath)
    with open(yaml_full_path, encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


# 读取Excel文件
def read_excel(excelpath):
    excel = openpyxl.load_workbook(excelpath)
    sheet = excel.active

    test_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        case_info = {
            'title': row[0],
            'type': row[1],
            'url': row[2],
            'method': row[3],
            'validate': row[4]
            }
        test_data.append(case_info)

    return test_data
