from PySide6.QtSql import QSqlDatabase, QSqlError, QSqlQuery

user_sql = "create table users (username varchar(20) primary key, password varchar(20))"
insert_user_sql = "insert into users (username, password) values (?, ?)"

def insertUser(username: str, password: str) -> QSqlError:
    q = QSqlQuery(QSqlDatabase.database("pmdatabase"))
    q.prepare(insert_user_sql)
    q.addBindValue(username)
    q.addBindValue(password)
    if not q.exec():
        return q.lastError()
    return q.lastError()

def countUsers() -> int:
    db = QSqlDatabase.database("pmdatabase")
    query = QSqlQuery(db)
    query.prepare("SELECT COUNT(*) FROM users")
    if query.exec() and query.next():
        return query.value(0)
    return -1  # Return -1 or an appropriate error code in case of failure



def initDb() -> QSqlError:
    db = QSqlDatabase.addDatabase("QSQLITE", "pmdatabase")
    db.setDatabaseName(":memory:")

    if not db.open():
        return db.lastError()
    q = QSqlQuery(db)
    if not q.exec(user_sql):
        return q.lastError()
    insertUser("admin", "admin")

class PaceMakerDB:
    pass