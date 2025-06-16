from .DbContext import get_connection

class Destinasi:
    def __init__(self, id_destinasi=None, nama=None, deskripsi=None, lokasi=None, kontak=None, password=None):
        self.id_destinasi = id_destinasi
        self.nama = nama
        self.deskripsi = deskripsi
        self.lokasi = lokasi
        self.kontak = kontak
        self.password = password

    @staticmethod
    def create(nama, deskripsi, lokasi, kontak, password):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO destinasi (nama, deskripsi, lokasi, kontak, password)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nama, deskripsi, lokasi, kontak, password))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM destinasi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    Destinasi(
                        id_destinasi = row[index["id_destinasi"]],
                        nama = row[index["nama"]],
                        deskripsi = row[index["deskripsi"]],
                        lokasi = row[index["lokasi"]],
                        kontak = row[index["kontak"]],
                        password = row[index["password"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_destinasi, nama, deskripsi, lokasi, kontak, password):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE destinasi
                    SET nama=%s, deskripsi=%s, lokasi=%s, kontak=%s, password=%s
                    WHERE id_destinasi = %s
                """, (nama, deskripsi, lokasi, kontak, password, id_destinasi))
                conn.commit()

    @staticmethod
    def delete(id_destinasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM destinasi WHERE id_destinasi = %s", (id_destinasi,))
                conn.commit()
