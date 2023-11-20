from PySide6.QtSql import QSqlDatabase, QSqlError, QSqlQuery

# 这个模块提供了在Qt应用程序中使用SQL数据库的支持，管理数据库连接，处理数据库错误，执行SQL查询
user_sql = "create table users (username varchar(20) primary key, password varchar(20))"
insert_user_sql = "insert into users (username, password) values (?, ?)"
device_sql = "create table devices (device_id varchar(20) primary key, device_name varchar(20))"
insert_device_sql = "insert into devices (device_id, device_name) values (?, ?)"
get_device_sql = "select device_name from devices"


# 定义数据库操作函数
def insertUser(username: str, password: str) -> QSqlError:
    q = QSqlQuery(QSqlDatabase.database("pmdatabase"))  # 接受用户名和密码作为参数，创建一个QsqQUERY，准备执行插入操作
    q.prepare(insert_user_sql)  # 绑定用户名和密码值到SQL语句中，然后执行插入操作
    q.addBindValue(username)
    q.addBindValue(password)
    if not q.exec():  # 如果插入成功，返回一个没有错误的qsqlerror对象，否则返回有错误的
        return q.lastError()
    return q.lastError()


def insertDevice(device_id: str, device_name: str) -> QSqlError:  # 将设备的名称和ID插入到device表中
    q = QSqlQuery(QSqlDatabase.database("pmdatabase"))
    q.prepare(insert_device_sql)
    q.addBindValue(device_id)
    q.addBindValue(device_name)
    if not q.exec():
        return q.lastError()
    return q.lastError()


def allDevices():  # 查询数据库以获得所有的设备名称，并将他们存储到一个字符串列表中返回
    q = QSqlQuery(QSqlDatabase.database("pmdatabase"))
    q.prepare(get_device_sql)
    if not q.exec(get_device_sql):
        return []
    devices = []
    while q.next():
        devices.append(q.value(0))
    return devices


def initDb() -> QSqlError:  # 用于初始化数据库，创建一个内存中SQlite数据库连接，并执行user_sql创建user表格，然后调用insertuser插入到一个admin的用户到数据库中，
    db = QSqlDatabase.addDatabase("QSQLITE", "pmdatabase")
    db.setDatabaseName(":memory:")  # 数据库将被创建在内存中

    if not db.open():  # 如果数据库初始化成功，则函数返回一个表示没有错误的QsqlError对象，否则返回有错误的，终止数据初始化
        return db.lastError()
    q = QSqlQuery(db)  # 与数据库连接，执行sql查询
    if not q.exec(user_sql):  # 执行usersql定义的sql，创建user表，如果执行失败返回一个表述数据库错误的qsqlerror对象，并终止数据初始化
        return q.lastError()
    if not q.exec(device_sql):
        return q.lastError()
    insertUser("admin", "admin")  # 将名为admin的用户插入到user表中

    insertDevice("0001", "device1")


class PaceMakerDB:
    pass
