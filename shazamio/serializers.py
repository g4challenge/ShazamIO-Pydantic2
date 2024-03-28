from typing import Union, List

from shazamio.schemas.base import BaseDataModel
from shazamio.factory_misc import FACTORY_ARTIST
from shazamio.factory_misc import FACTORY_TRACK
from shazamio.schemas.artist.views.full_albums import FullAlbumsModel
from shazamio.schemas.artists import ArtistInfo
from shazamio.schemas.artists import ArtistResponse
from shazamio.schemas.artists import ArtistV2
from shazamio.schemas.models import ResponseTrack
from shazamio.schemas.models import TrackInfo
from shazamio.schemas.models import YoutubeData
from shazamio.schemas.album import AlbumModel


class Serialize:
    @classmethod
    def track(cls, data):
        return FACTORY_TRACK.load(data, TrackInfo)

    @classmethod
    def youtube(cls, data):
        return FACTORY_TRACK.load(data, YoutubeData)

    @classmethod
    def artist_v2(cls, data) -> ArtistResponse:
        return ArtistResponse.parse_obj(data)

    @classmethod
    def artist_albums(cls, data) -> FullAlbumsModel:
        return FullAlbumsModel.parse_obj(data)

    @classmethod
    def artist(cls, data):
        return FACTORY_ARTIST.load(data, Union[ArtistV2, ArtistInfo])

    @classmethod
    def full_track(cls, data):
        return FACTORY_TRACK.load(data, ResponseTrack)

    @classmethod
    def album_info(cls, data) -> BaseDataModel[List[AlbumModel]]:
        return BaseDataModel[List[AlbumModel]].parse_obj(data)
