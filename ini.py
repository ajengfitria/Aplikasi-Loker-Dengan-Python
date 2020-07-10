from PyQt5.QtSql import *

def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Lokerindo')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        id, nama, email = range(3)
        query.exec_ ('SELECT * FROM akun')
        print('Output data\t: ')
        print('No.\tnama\tNo.HP')
        while query.next():
            id = query.value(id)
            nama = query.value(nama)
            email = query.value(email)
            print('%d\t%s\t%s' % (id,nama,email))

    else:
        print('ERROR: ' + db.lastError().text())

connect()