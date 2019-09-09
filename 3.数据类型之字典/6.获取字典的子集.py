# -*- coding:utf-8 _*-
"""

"""
if __name__ == '__main__':
    common_key = {"amount", "product_code", "plan_code"}
    resp_data = {
        "amount": 2199.00,
        "product_code": "LJ11010",
        "plan_code": "11010",
        "bank_code": "9001",
        "bank_name": "建设银行",
    }

    map = {key: resp_data[key] for key in resp_data.keys() & common_key}
    print(map)
