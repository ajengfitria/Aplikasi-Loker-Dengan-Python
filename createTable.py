from PyQt5.QtSql import *

def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Lokerindo')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        #Create table loker
        sql = '''Create TABLE loker(
            no integer not null primary key, 
            posisi varchar(50), 
            perusahaan varchar(50),
            penempatan varchar(50),
            gaji integer,
            deadline date
            )'''
        query.exec_(sql)
        #Create table akun
        sql = '''Create TABLE akun(
            id integer not null primary key, 
            nama varchar(50), 
            email varchar(50),
            alamat text,
            pass text,
            hp integer,
            gender varchar(15),
            pekerjaan varchar(50),
            pengalaman text,
            keahlian text
            )'''
        query.exec_(sql)
        #Create table lamaran
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
        if(query.exec_):
            print('Tabel berhasil dibuat')

    else:
        print('ERROR: ' + db.lastError().text())

connect()