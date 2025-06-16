from .DbContext import get_connection

class DetailPaketAkomodasi:
    def __init__(self, id_paket=None, id_akomodasi=None, deskripsi_penginapan=None):
        self.id_paket = id_paket
        self.id_akomodasi = id_akomodasi
        self.deskripsi_penginapan = deskripsi_penginapan

    @staticmethod
    def create(id_paket, id_akomodasi, deskripsi_penginapan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO detail_paket_akomodasi (id_paket, id_akomodasi, deskripsi_penginapan)
                    VALUES (%s, %s, %s)
                """, (id_paket, id_akomodasi, deskripsi_penginapan))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM detail_paket_akomodasi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    DetailPaketAkomodasi(
                        id_paket = row[index["id_paket"]],
                        id_akomodasi = row[index["id_akomodasi"]],
                        deskripsi_penginapan = row[index["deskripsi_penginapan"]]
                    )
                    for row in rows
                ]
                
    @staticmethod
    def update(id_paket, id_akomodasi, deskripsi_penginapan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE detail_paket_akomodasi
                    SET deskripsi_penginapan=%s
                    WHERE id_paket=%s AND id_akomodasi=%s
                """, (deskripsi_penginapan, id_paket, id_akomodasi))
                conn.commit()

    @staticmethod
    def delete(id_paket, id_akomodasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM detail_paket_akomodasi
                    WHERE id_paket = %s AND id_akomodasi = %s
                """, (id_paket, id_akomodasi))
                conn.commit()
