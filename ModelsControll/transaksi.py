from .DbContext import get_connection

class Transaksi:
    def __init__(self, id_transaksi=None, id_pemesanan=None, tanggal_transaksi=None, total_harga=None, status_pembayaran=None):
        self.id_transaksi = id_transaksi
        self.id_pemesanan = id_pemesanan
        self.tanggal_transaksi = tanggal_transaksi
        self.total_harga = total_harga
        self.status_pembayaran = status_pembayaran

    @staticmethod
    def create(id_pemesanan, tanggal_transaksi, total_harga, status_pembayaran):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO transaksi (id_pemesanan, tanggal_transaksi, total_harga, status_pembayaran)
                    VALUES (%s, %s, %s, %s)
                """, (id_pemesanan, tanggal_transaksi, total_harga, status_pembayaran))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM transaksi")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    Transaksi(
                        id_transaksi = row[index["id_transaksi"]],
                        id_pemesanan = row[index["id_pemesanan"]],
                        tanggal_transaksi = row[index["tanggal_transaksi"]],
                        total_harga = row[index["total_harga"]],
                        status_pembayaran = row[index["status_pembayaran"]],
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_transaksi, id_pemesanan, tanggal_transaksi, total_harga, status_pembayaran):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE transaksi
                    SET id_pemesanan=%s, tanggal_transaksi=%s, total_harga=%s, status_pembayaran=%s
                    WHERE id_transaksi = %s
                """, (id_pemesanan, tanggal_transaksi, total_harga, status_pembayaran, id_transaksi))
                conn.commit()

    @staticmethod
    def delete(id_transaksi):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM transaksi WHERE id_transaksi = %s", (id_transaksi,))
                conn.commit()
