import os


# import glob


# def get_file_path():
#     files_path = os.getcwd() + "/sorted/"
#     file_paths = glob.glob(files_path + "*.txt")
#     return file_paths
#
# if __name__ == "__main__":
#     print(get_file_path())


# def combine_files():
#     ""Собрать три в один"""

files_path = os.getcwd() + "/directory/"
file1_path = os.path.join(files_path, "1.txt")
file2_path = os.path.join(files_path, "2.txt")
file3_path = os.path.join(files_path, "3.txt")

file1_name = os.path.basename(file1_path)
file2_name = os.path.basename(file2_path)
file3_name = os.path.basename(file3_path)

with open(file1_path, encoding='utf-8') as f1:
    lines_1 = f1.readlines()
with open(file2_path, encoding='utf-8') as f2:
    lines_2 = f2.readlines()
with open(file3_path, encoding='utf-8') as f3:
    lines_3 = f3.readlines()

file_lilnes_count_dict = {
    "Кол-во строк в file1": len(lines_1),
    "Кол-во строк в file2": len(lines_2),
    "Кол-во строк в file3": len(lines_3),
}
print(file_lilnes_count_dict)

file_write_order_lst = [
    len(lines_1),
    len(lines_2),
    len(lines_3),
]
file_write_order_lst.sort()
print(file_write_order_lst)

with open("result_file.txt", 'w', encoding="utf-8") as f:
    f.write(f"{file2_name}\n")
    f.write(f"{len(lines_2)}\n")
    f.write(" ".join(lines_2))
    f.write(f"\n{file1_name}\n")
    f.write(f"{len(lines_1)}\n")
    f.write(" ".join(lines_1))
    f.write(f"\n{file3_name}\n")
    f.write(f"{len(lines_3)}\n")
    f.write(" ".join(lines_3))
    # return combine_files
    #     print(result_file.txt)
        # return combine_files


# combine_files()




# Образец
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1