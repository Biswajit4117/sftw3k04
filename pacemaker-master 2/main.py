from PySide6.QtWidgets import QApplication, QWidget
from modeselection import ModeSelection
from login import Login
# from qt_material import apply_stylesheet
# appy管理应用程序的生命周期，qw创建程序的窗口
import sys

if __name__ == "__main__":  # 表示当只有这个脚本被直接运行的时候，而不是被导入模块时，下面的代码板块才会执行
    app = QApplication(sys.argv)  # 创建一个qt应用程序的对象
    from database import initDb  # 导入init函数，初始化数据库

    initDb()
    window = ModeSelection(None)  # 创建一个modeselection主窗口对象
    login = Login(None)  # 创建一个登录对话框对象
    login.exec()  # 执行登录对话框，等待用户输入登录信息
    window.ui.label.setText(f'Welcome, {login.username}')
    # apply_stylesheet(app, 'dark_amber.xml')
    window.show()


    def relogin():
        window.close()
        login.exec()
        window.ui.label.setText(f'Welcome, {login.username}')
        window.show()


    window.ui.logoutButton.clicked.connect(relogin)
    sys.exit(app.exec())  # 保持应用运行，直到退出
