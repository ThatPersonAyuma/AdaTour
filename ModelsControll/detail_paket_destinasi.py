from .DbContext import get_connection

class DetailPaketDestinasi:
    def __init__(self, id_detail_paket_destinasi=None, id_paket=None, id_destinasi=None):
        self.id_detail_paket_destinasi = id_detail_paket_destinasi
        self.id_paket = id_paket
        self.id_destinasi = id_destinasi

    @staticmethod
    def create(id_paket, id_destinasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO detail_paket_destinasi (id_paket, id_destinasi)
                    VALUES (%s, %s)
                """, (id_paket, id_destinasi))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM detail_paket_destinasi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    DetailPaketDestinasi(
                        id_detail_paket_destinasi = row[index["id_detail_paket_destinasi"]],
                        id_paket = row[index["id_paket"]],
                        id_destinasi = row[index["id_destinasi"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_detail_paket_destinasi, id_paket, id_destinasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE detail_paket_destinasi
                    SET id_paket=%s, id_destinasi=%s
                    WHERE id_detail_paket_destinasi = %s
                """, (id_paket, id_destinasi, id_detail_paket_destinasi))
                conn.commit()

    @staticmethod
    def delete(id_detail_paket_destinasi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM detail_paket_destinasi WHERE id_detail_paket_destinasi = %s", (id_detail_paket_destinasi,))
                conn.commit()
