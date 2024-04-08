import os
import shutil

def clear_folder(folder_path):
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        print(f"文件夹 '{folder_path}' 不存在。")
        return

    # 遍历文件夹中的所有子文件夹
    for root, dirs, files in os.walk(folder_path):
        # 删除所有子文件夹中的文件
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"已删除文件: {file_path}")

        # 删除当前子文件夹
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            shutil.rmtree(dir_path)
            print(f"已删除文件夹: {dir_path}")


if __name__ == "__main__":
    # 调用函数来清空指定文件夹下的所有子文件夹
    folder_to_clear = "/path/to/your/folder"
    clear_folder(folder_to_clear)
