def num17_digit():
    import random
    region_code = []
    for num_1_6 in range(6):
        num = random.randint(0, 9)
        region_code.append(num)
    # print(region_code)
    birth_date = [1, 9, ]
    for num_9_10 in range(2):
        brith = random.randint(0, 9)
        birth_date.append(brith)
    for num_11 in range(1):
        brith = random.randint(0, 1)
        if brith == 0:
            birth_date.append(brith)
            for num_12 in range(1):
                brith = random.randint(0, 9)
        else:
            birth_date.append(brith)
            for num_12 in range(1):
                brith = random.randint(0, 2)
        birth_date.append(brith)
    for num_13 in range(1):
        brith = random.randint(0, 2)
        birth_date.append(brith)
    for num_14 in range(1):
        brith = random.randint(0, 9)
        birth_date.append(brith)
    # print(birth_date)
    sequence_number = []
    for num_15_17 in range(3):
        seq_num = random.randint(0, 9)
        sequence_number.append(seq_num)
    # print(sequence_number)
    num_17digit = region_code + birth_date + sequence_number
    return(num_17digit)

def calculate_check_digit(id_number):
    # 权重因子
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验位对应值
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    check_sum = sum(int(a) * b for a, b in zip(id_number, weights))
    return check_codes[check_sum % 11]


for x in range(5):
    id_number = num17_digit()
    check_digit = calculate_check_digit(id_number)
    #将17位数转换为字符串
    lenth = len(id_number)
    id_num_str1 = ''
    for i in range(lenth):
        j = str(id_number[i])
        id_num_str1 += j
    id_card_num = id_num_str1 + check_digit
    print(id_card_num)