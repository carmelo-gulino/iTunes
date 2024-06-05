from dataclasses import dataclass


@dataclass
class Album:
    AlbumId: int
    Title: str
    ArtistId: int
    tot_d: int

    def __hash__(self):
        return hash(self.AlbumId)

    def __str__(self):
        return f'{self.AlbumId} - {self.tot_d}'

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId
