from .DbContext import get_connection

class Pemesanan:
    def __init__(self, id_pemesanan=None, id_user=None, id_paket=None, tanggal_pesan=None, tanggal_berangkat=None, jumlah_orang=None):
        self.id_pemesanan = id_pemesanan
        self.id_user = id_user
        self.id_paket = id_paket
        self.tanggal_pesan = tanggal_pesan
        self.tanggal_berangkat = tanggal_berangkat
        self.jumlah_orang = jumlah_orang

    @staticmethod
    def create(id_user, id_paket, tanggal_pesan, tanggal_berangkat, jumlah_orang):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO pemesanan (id_user, id_paket, tanggal_pesan, tanggal_berangkat, jumlah_orang)
                    VALUES (%s, %s, %s, %s, %s)
                """, (id_user, id_paket, tanggal_pesan, tanggal_berangkat, jumlah_orang))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM pemesanan")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    Pemesanan(
                        id_pemesanan =row[index["id_pemesanan"]], 
                        id_user =row[index["id_user"]], 
                        id_paket =row[index["id_paket"]], 
                        tanggal_pesan =row[index["tanggal_pesan"]], 
                        tanggal_berangkat =row[index["tanggal_berangkat"]], 
                        jumlah_orang =row[index["jumlah_orang"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_pemesanan, id_user, id_paket, tanggal_pesan, tanggal_berangkat, jumlah_orang):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE pemesanan
                    SET id_user=%s, id_paket=%s, tanggal_pesan=%s, tanggal_berangkat=%s, jumlah_orang=%s
                    WHERE id_pemesanan = %s
                """, (id_user, id_paket, tanggal_pesan, tanggal_berangkat, jumlah_orang, id_pemesanan))
                conn.commit()

    @staticmethod
    def delete(id_pemesanan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM pemesanan WHERE id_pemesanan = %s", (id_pemesanan,))
                conn.commit()
