from .DbContext import get_connection

class PesananMitra:
    def __init__(self, id_pemesanan=None, id_mitra=None, deskripsi_pesanan=None):
        self.id_pemesanan = id_pemesanan
        self.id_mitra = id_mitra
        self.deskripsi_pesanan = deskripsi_pesanan

    @staticmethod
    def create(id_pemesanan, id_mitra, deskripsi_pesanan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO pesanan_mitra (id_pemesanan, id_mitra, deskripsi_pesanan)
                    VALUES (%s, %s, %s)
                """, (id_pemesanan, id_mitra, deskripsi_pesanan))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM pesanan_mitra")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    PesananMitra(
                        id_pemesanan = row[index["id_pemesanan"]],
                        id_mitra = row[index["id_mitra"]],
                        deskripsi_pesanan = row[index["deskripsi_pesanan"]],
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_pemesanan, id_mitra, deskripsi_pesanan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE pesanan_mitra
                    SET deskripsi_pesanan=%s
                    WHERE id_pemesanan = %s AND id_mitra = %s
                """, (deskripsi_pesanan, id_pemesanan, id_mitra))
                conn.commit()

    @staticmethod
    def delete(id_pemesanan, id_mitra):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM pesanan_mitra WHERE id_pemesanan = %s AND id_mitra = %s", (id_pemesanan, id_mitra))
                conn.commit()
