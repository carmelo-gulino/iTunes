from database.DB_connect import DBConnect
from model.album import Album


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_albums(d):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select a.*, sum(t.Milliseconds) tot_d
                    from album a , track t 
                    where a.AlbumId = t.AlbumId 
                    group by a.AlbumId 
                    having tot_d > %s
                    order by a.Title"""
        cursor.execute(query, (d, ))
        result = []
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_edges(albums_map):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinctrow t.AlbumId a1, t2.AlbumId a2 
                    from playlisttrack p , track t , playlisttrack p2 , track t2 
                    where p.PlaylistId = p2.PlaylistId and p2.TrackId = t2.TrackId 
                    and p.TrackId = t.TrackId and t2.AlbumId > t.AlbumId"""
        cursor.execute(query)
        result = []
        for row in cursor:
            if row["a1"] in albums_map and row["a2"] in albums_map:
                result.append((albums_map[row["a1"]], albums_map[row["a2"]]))
        cursor.close()
        cnx.close()
        return result

