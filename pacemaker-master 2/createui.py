import os  # 允许你与操作系统交互，包括文件和目录的操作

if __name__ == '__main__':  # 检查当前脚本是否被直接运行（而不是被导入为模块）
    for file in os.listdir('.'):  # 获取当前目录下的所有文件和子目录的列表
        if file.endswith('.ui'):  # 遍历这个列表，对于每个文件名，它检查是否以'.ui'结尾，表示这是一个Qt Designer的用户界面文件（.ui文件）
            ui_modification_time = os.path.getmtime(file)  # 获取ui结尾的文件的修改时间
            try:  # 与文件相关的python文件修改时间
                py_modification_time = os.path.getmtime('ui_' + file.replace('.ui', '.py'))
            except:  # 没有找到文件就0
                py_modification_time = 0
            if ui_modification_time <= py_modification_time:
                continue  # 表示文件没有被修改，跳过
            print(
                f'pyside6-uic {file} -o {"ui_" + file.replace(".ui", ".py")}')  # 使用f字符串将要执行的命令打印出来，调用pyside6-uic将python转换成ui
            os.system(
                f'pyside6-uic {file} -o {"ui_" + file.replace(".ui", ".py")}')  # 使用os函数来执行上述打印命令，将ui转换成python文件，调用pyside6-uic,将结果保存到一个与ui文件名相关的python文件中
