import asyncio
from shazamio import Shazam, Serialize, GenreMusic


async def main():
    shazam = Shazam()
    top_rock_in_the_world = await shazam.top_world_genre_tracks(
        genre=GenreMusic.ROCK, limit=10
    )

    serialized = Serialize.playlists(top_rock_in_the_world)
    print(serialized)

    for playlist in top_rock_in_the_world["data"]:
        serialized = Serialize.playlist(data=playlist)
        print(serialized)


loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(main())
