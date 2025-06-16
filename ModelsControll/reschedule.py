from .DbContext import get_connection

class Reschedule:
    def __init__(self, id_reschedule=None, id_user=None, id_jadwal_keberangkatan=None, tanggal_permintaan=None, tanggal_baru=None, alasan=None, status_pengajuan=None):
        self.id_reschedule = id_reschedule
        self.id_user = id_user
        self.id_jadwal_keberangkatan = id_jadwal_keberangkatan
        self.tanggal_permintaan = tanggal_permintaan
        self.tanggal_baru = tanggal_baru
        self.alasan = alasan
        self.status_pengajuan = status_pengajuan

    @staticmethod
    def create(id_user, id_jadwal_keberangkatan, tanggal_permintaan, tanggal_baru, alasan, status_pengajuan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO reschedule (id_user, id_jadwal_keberangkatan, tanggal_permintaan, tanggal_baru, alasan, status_pengajuan)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (id_user, id_jadwal_keberangkatan, tanggal_permintaan, tanggal_baru, alasan, status_pengajuan))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reschedule")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}
                
                return [
                    Reschedule(
                        id_reschedule = row[index["id_reschedule"]],
                        id_user = row[index["id_user"]],
                        id_jadwal_keberangkatan = row[index["id_jadwal_keberangkatan"]],
                        tanggal_permintaan = row[index["tanggal_permintaan"]],
                        tanggal_baru = row[index["tanggal_baru"]],
                        alasan = row[index["alasan"]],
                        status_pengajuan = row[index["status_pengajuan"]],
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_reschedule, id_user, id_jadwal_keberangkatan, tanggal_permintaan, tanggal_baru, alasan, status_pengajuan):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE reschedule
                    SET id_user=%s, id_jadwal_keberangkatan=%s, tanggal_permintaan=%s, tanggal_baru=%s, alasan=%s, status_pengajuan=%s
                    WHERE id_reschedule = %s
                """, (id_user, id_jadwal_keberangkatan, tanggal_permintaan, tanggal_baru, alasan, status_pengajuan, id_reschedule))
                conn.commit()

    @staticmethod
    def delete(id_reschedule):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM reschedule WHERE id_reschedule = %s", (id_reschedule,))
                conn.commit()
