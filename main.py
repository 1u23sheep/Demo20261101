from pathlib import Path

#获取当前脚本的文件夹
PROJECT_DIR = Path(__file__).resolve().parent

#拼接原始数据文件的完整路径
DATA_FILE = PROJECT_DIR / "data" / "raw" / "ALBH.tenv3"

#检查文件
print("数据文件路径：",DATA_FILE)
print("文件是否存在：",DATA_FILE.exists())

#读取文件
with DATA_FILE.open("r",encoding="utf-8")as file:
    header = file.readline()
    first_record = file.readline()
print(header)

#分割表头
fields = first_record.split()

print("拆分后：",fields)
print("数量：",len(fields))

station = fields[0]
date_text = fields[1]

print(station)
print(date_text)