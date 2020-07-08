from PyQt5.QtSql import *

def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Lokerindo')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        sql = '''Create TABLE lamaran(
            noLam integer not null primary key,
            idAkun integer,
            posisi varchar(50), 
            perusahaan varchar(50),
            penempatan varchar(50),
            tglSubmit date,
            status varchar(30),
            cv varchar(30)
            )'''
        query.exec_(sql)

    else:
        print('ERROR: ' + db.lastError().text())

connect()