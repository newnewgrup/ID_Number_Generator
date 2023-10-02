#手动输入17位算身份证校验位

def num17_digit():
    import random
    region_code = []
    for i in range(6):
        num = random.randint(0, 9)
        region_code.append(num)
    # print(region_code)
    birth_date = [1, 9, ]
    for j in range(2):
        brith = random.randint(0, 9)
        birth_date.append(brith)
    for k in range(1):
        brith = random.randint(0, 1)
        if brith == 0:
            birth_date.append(brith)
            for m in range(1):
                brith = random.randint(0, 9)
        else:
            birth_date.append(brith)
            for m in range(1):
                brith = random.randint(0, 2)
        birth_date.append(brith)
    for n in range(1):
        brith = random.randint(0, 2)
        birth_date.append(brith)
    for x in range(1):
        brith = random.randint(0, 9)
        birth_date.append(brith)
    # print(birth_date)
    sequence_number = []
    for k in range(3):
        seq_num = random.randint(0, 9)
        sequence_number.append(seq_num)
    # print(sequence_number)
    num_17digit = region_code + birth_date + sequence_number
    return(num_17digit)

id_number = num17_digit()
def calculate_check_digit(id_number):
    # 权重因子
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验位对应值
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    
    if len(id_number) != 17:
        return "输入的身份证号码长度错误，应输入17位数字。"
    
    check_sum = sum(int(a) * b for a, b in zip(id_number, weights))
    return check_codes[check_sum % 11]
id_number = input("请输入17位身份证号码：")
check_digit = calculate_check_digit(id_number)
print("校验位为：", check_digit)
lenth = len(id_number)
id_num_str1 = ''
for i in range(lenth):
    x = str(id_number[i])
    id_num_str1 += x
print("完整的身份证号码为：", id_num_str1 + check_digit)