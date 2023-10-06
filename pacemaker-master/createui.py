import os

if __name__ == '__main__':
    for file in os.listdir('.'):
        if file.endswith('.ui'):
            ui_modification_time = os.path.getmtime(file)
            try:
                py_modification_time = os.path.getmtime('ui_' + file.replace('.ui', '.py'))
            except:
                py_modification_time = 0
            if ui_modification_time <= py_modification_time:
                continue
            print(f'pyside6-uic {file} -o {"ui_" + file.replace(".ui", ".py")}')
            os.system(f'pyside6-uic {file} -o {"ui_" + file.replace(".ui", ".py")}')