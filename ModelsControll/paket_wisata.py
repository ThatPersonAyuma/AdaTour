from .DbContext import get_connection

class PaketWisata:
    def __init__(self, id_paket=None, nama=None, deskripsi=None, durasi_hari=None):
        self.id_paket = id_paket
        self.nama = nama
        self.deskripsi = deskripsi
        self.durasi_hari = durasi_hari

    @staticmethod
    def create(nama, deskripsi, durasi_hari):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO paket_wisata (nama, deskripsi, durasi_hari)
                    VALUES (%s, %s, %s)
                """, (nama, deskripsi, durasi_hari))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM paket_wisata")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    PaketWisata(
                        id_paket = row[index["id_paket"]], 
                        nama = row[index["nama"]], 
                        deskripsi = row[index["deskripsi"]], 
                        durasi_hari = row[index["durasi_hari"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_paket, nama, deskripsi, durasi_hari):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE paket_wisata
                    SET nama=%s, deskripsi=%s, durasi_hari=%s
                    WHERE id_paket = %s
                """, (nama, deskripsi, durasi_hari, id_paket))
                conn.commit()

    @staticmethod
    def delete(id_paket):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM paket_wisata WHERE id_paket = %s", (id_paket,))
                conn.commit()
