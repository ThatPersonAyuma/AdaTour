from .DbContext import get_connection

class Transportasi:
    def __init__(self, id_transportasi=None, nama=None, jenis=None, kapasitas=None, nomor_plat=None, kontak=None, email=None, password=None):
        self.id_transportasi = id_transportasi
        self.nama = nama
        self.jenis = jenis
        self.kapasitas = kapasitas
        self.nomor_plat = nomor_plat
        self.kontak = kontak
        self.email = email
        self.password = password

    @staticmethod
    def create(nama, jenis, kapasitas, nomor_plat, kontak, email, password):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO transportasi (nama, jenis, kapasitas, nomor_plat, kontak, email, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (nama, jenis, kapasitas, nomor_plat, kontak, email, password))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM transportasi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    Transportasi(
                        id_transportasi = row[index["id_transportasi"]],
                        nama = row[index["nama"]],
                        jenis = row[index["jenis"]],
                        kapasitas = row[index["kapasitas"]],
                        nomor_plat = row[index["nomor_plat"]],
                        kontak = row[index["kontak"]],
                        email = row[index["email"]],
                        password = row[index["password"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_transportasi, nama, jenis, kapasitas, nomor_plat, kontak, email, password):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE transportasi
                    SET nama=%s, jenis=%s, kapasitas=%s, nomor_plat=%s, kontak=%s, email=%s, password=%s
                    WHERE id_transportasi = %s
                """, (nama, jenis, kapasitas, nomor_plat, kontak, email, password, id_transportasi))
                conn.commit()

    @staticmethod
    def delete(id_transportasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM transportasi WHERE id_transportasi = %s", (id_transportasi,))
                conn.commit()
