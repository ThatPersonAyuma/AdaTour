from .DbContext import get_connection

class Akomodasi:
    def __init__(self, id_akomodasi=None, nama=None, bintang=None, tipe=None, kapasitas=None, alamat=None, kota=None, kontak=None, email=None, password=None):
        self.id_akomodasi = id_akomodasi
        self.nama = nama
        self.tipe = tipe
        self.bintang = bintang
        self.alamat = alamat
        self.kota = kota
        self.kontak = kontak
        self.email = email
        self.password = password

    @staticmethod
    def create(nama, tipe,bintang,alamat, kota, kontak, email, password):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO akomodasi (nama, tipe, bintang, alamat, kota, kontak, email, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (nama, tipe, bintang, alamat, kota, kontak, email, password))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM akomodasi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    Akomodasi(
                        id_akomodasi = row[index["id_akomodasi"]],
                        nama = row[index["nama"]],
                        tipe = row[index["tipe"]],
                        kapasitas = row[index["kapasitas"]],
                        alamat = row[index["alamat"]],
                        kota = row[index["kota"]],
                        kontak = row[index["kontak"]],
                        email = row[index["email"]],
                        password = row[index["password"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_akomodasi, nama, tipe, kapasitas, alamat, kota, kontak, email, password):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE akomodasi
                    SET nama=%s, tipe=%s, kapasitas=%s, alamat=%s, kota=%s, kontak=%s, email=%s, password=%s
                    WHERE id_akomodasi = %s
                """, (nama, tipe, kapasitas, alamat, kota, kontak, email, password, id_akomodasi))
                conn.commit()

    @staticmethod
    def delete(id_akomodasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM akomodasi WHERE id_akomodasi = %s", (id_akomodasi,))
                conn.commit()
