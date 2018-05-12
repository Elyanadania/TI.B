from app import db


class matkul(db.Model):
    kode_matkul = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_dosen = db.Column(db.String(50), nullable=False)
    jurusan = db.column(db.String,(50), nullable=False)
    kelas = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(50), nullable=False)
    


class dosen(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nip = db.Column(db.String(50), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    jenis_kelamin = db.Column(db.String(100), nullable=False)
    ttl = db.Column(db.String(50), nullable=False)
    alamat = db.Column(db.String(50), nullable=False)