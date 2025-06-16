from .DbContext import get_connection

class JadwalKeberangkatan:
    def __init__(self, id_jadwal_keberangkatan=None, id_pemesanan=None, id_user=None, tanggal_berangkat=None, catatan=None):
        self.id_jadwal_keberangkatan = id_jadwal_keberangkatan
        self.id_pemesanan = id_pemesanan
        self.id_user = id_user
        self.tanggal_berangkat = tanggal_berangkat
        self.catatan = catatan

    @staticmethod
    def create(id_pemesanan, id_user, tanggal_berangkat, catatan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO jadwal_keberangkatan (id_pemesanan, id_user, tanggal_berangkat, catatan)
                    VALUES (%s, %s, %s, %s)
                """, (id_pemesanan, id_user, tanggal_berangkat, catatan))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jadwal_keberangkatan")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    JadwalKeberangkatan(
                        id_jadwal_keberangkatan = row[index["id_jadwal_keberangkatan"]],
                        id_pemesanan = row[index["id_pemesanan"]],
                        id_user = row[index["id_user"]],
                        tanggal_berangkat = row[index["tanggal_berangkat"]],
                        catatan = row[index["catatan"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_jadwal_keberangkatan, id_pemesanan, id_user, tanggal_berangkat, catatan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE jadwal_keberangkatan
                    SET id_pemesanan=%s, id_user=%s, tanggal_berangkat=%s, catatan=%s
                    WHERE id_jadwal_keberangkatan = %s
                """, (id_pemesanan, id_user, tanggal_berangkat, catatan, id_jadwal_keberangkatan))
                conn.commit()

    @staticmethod
    def delete(id_jadwal_keberangkatan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM jadwal_keberangkatan WHERE id_jadwal_keberangkatan = %s", (id_jadwal_keberangkatan,))
                conn.commit()
