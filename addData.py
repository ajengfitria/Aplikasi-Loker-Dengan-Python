from PyQt5.QtSql import *

def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Lokerindo')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        #Insert to loker table
        sql = '''INSERT INTO loker VALUES(1, 'Back-End Developer', 'Shoppe','Jakarta',20000000,'2020-07-30'),
        (2, 'Product Designer', 'Bukalapak','Bandung',9000000,'2020-08-05'),
        (3, 'Product Owner', 'Tokopedia','Jakarta',15000000,'2020-07-25'),
        (4, 'Researcher', 'GoJek','Jakarta',8000000,'2020-08-20'),
        (5, 'Android Developer', 'Telkom','Yogyakarta',7000000,'2020-07-16')'''
        query.exec_(sql)

        #Insert to akun table
        sql = '''INSERT INTO akun VALUES(1, 'Ajeng Fitria', 'ajengfitria80@gmail.com','Cilacap','admin123',081328963818,'Perempuan','Mahasiswa','Coba','Pyhton Programmer')'''
        query.exec_(sql)
        if(query.exec_):
            print('Data berhasil dimasukkan')

    else:
        print('ERROR: ' + db.lastError().text())

connect()