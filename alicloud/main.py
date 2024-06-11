import os
from datetime import datetime

def create_temp_dir() -> dict:
    full_txt = "full-volume.txt"
    scanning_txt = "scanning_non-compliance.txt"

    # 获取当前目录路径
    current_directory = os.getcwd()

    # 定义temp文件夹路径
    temp_directory = os.path.join(current_directory, 'temp')

    # 如果temp文件夹不存在，则创建它
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    # 获取当前日期和时间，并格式化为YYYYMMDD-HHMMSS
    current_datetime = datetime.now().strftime('%Y%m%d-%H%M%S')

    # 定义新的文件夹路径
    root_path = os.path.join(temp_directory, current_datetime)
    full_txt = os.path.join(root_path, full_txt)  # 定义全量数据文件路径
    scanning_txt = os.path.join(root_path, scanning_txt)  # 定义扫描不合规数据文件路径

    # 创建新的日期-时间文件夹
    os.makedirs(root_path)

    # 在新文件夹中创建文件
    with open(full_txt, 'w', encoding='utf-8') as file:
        file.write('全量数据\n')  # 写入空内容或可以在这里写入其他默认内容

    with open(scanning_txt, 'w', encoding='utf-8') as file:
        file.write('扫描不合规数据\n')  # 写入空内容或可以在这里写入其他默认内容

    print(f"当前脚本运行存放目录：{root_path}")

    return {'full_txt': full_txt, 'scanning_txt': scanning_txt}


if __name__ == '__main__':
    files = create_temp_dir()
    print(files["full_txt"])
    # 以追加模式打开文件
    with open(files["full_txt"], 'a', encoding='utf-8') as file:
        file.write('彭于晏\n')
        file.write('吴彦祖\n')

    with open("E:\code\py-demo\\alicloud\\temp\\20240611-223629\\full-volume.txt", 'a', encoding='utf-8') as file:
        file.write('彭于晏11\n')
        file.write('吴彦祖22\n')
