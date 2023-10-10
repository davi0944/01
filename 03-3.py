import re

def validate_id_card(id_card):
    pattern = r"(^\d{15}$)|(^\d{17}([0-9]|X)$)"
    if re.match(pattern, id_card):
        return True
    else:
        return False

id_card = input("请输入身份证号码：")
if validate_id_card(id_card):
    print("身份证号码合法")
else:
    print("身份证号码不合法")
