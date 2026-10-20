def read_can_csv(file_path):
    # 准备一个空列表，用来装所有的行
    log_data = []

    with open(file_path, "r", encoding="utf-8") as f:
        next(f)  # 跳过第一行表头 (timestamp,can_id,data)

        for line in f:
            # 1. 去掉换行符，并按逗号切分这一行
            parts = line.strip().split(",")

            # 确保切分出来正好是3个部分
            if len(parts) == 3:
                # 2. 把这三个部分装进一个字典里
                row_dict = {
                    "time": float(parts[0]),  # 时间转成小数
                    "id": parts[1],  # ID保持字符串
                    "data": parts[2]  # 数据保持字符串
                }
                # 3. 把字典塞进大列表里 (注意：一定是 append 追加)
                log_data.append(row_dict)

    return log_data


# 调用函数，拿到数据
my_logs = read_can_csv("mock_can.csv")

# 用循环打印出来看看
print(f"一共读取了 {len(my_logs)} 行数据：")

for row in my_logs:
    if row["id"] == "0x100":
        print(f"时间: {row['time']} | ID: {row['id']} (目标ID) | 数据: {row['data']}")
    else:
        print(f"时间: {row['time']} | ID: {row['id']} | 数据: {row['data']}")

