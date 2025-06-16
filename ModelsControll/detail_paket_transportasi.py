from .DbContext import get_connection

class DetailPaketTransportasi:
    def __init__(self, id_paket=None, id_transportasi=None, deskripsi_perjalanan=None):
        self.id_paket = id_paket
        self.id_transportasi = id_transportasi
        self.deskripsi_perjalanan = deskripsi_perjalanan

    @staticmethod
    def create(id_paket, id_transportasi, deskripsi_perjalanan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO detail_paket_transportasi (id_paket, id_transportasi, deskripsi_perjalanan)
                    VALUES (%s, %s, %s)
                """, (id_paket, id_transportasi, deskripsi_perjalanan))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM detail_paket_transportasi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    DetailPaketTransportasi(
                        id_paket = row[index["id_paket`"]],
                        id_transportasi = row[index["id_transportasi`"]],
                        deskripsi_perjalanan = row[index["deskripsi_perjalanan`"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_paket, id_transportasi, deskripsi_perjalanan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE detail_paket_transportasi
                    SET deskripsi_perjalanan=%s
                    WHERE id_paket=%s AND id_transportasi=%s
                """, (deskripsi_perjalanan, id_paket, id_transportasi))
                conn.commit()

    @staticmethod
    def delete(id_paket, id_transportasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM detail_paket_transportasi
                    WHERE id_paket = %s AND id_transportasi = %s
                """, (id_paket, id_transportasi))
                conn.commit()
