import logging

logging.basicConfig(level=logging.INFO)

class AlbumExtractor:
    def __init__(self, token=None):
        self.token = token or "mock_token"

    def extract(self, album_id: str):
        logging.info(f"Fetching album data for {album_id}")
        try:
            data = {
                "id": album_id,
                "name": "Future Nostalgia",
                "artist": "Dua Lipa",
                "release_date": "2020-03-27",
                "tracks": [
                    {"id": "3PfIrDoz19wz7qK7tYeu62", "name": "Don't Start Now"},
                    {"id": "6WrI0LAC5M1Rw2MnX2ZvEg", "name": "Levitating"},
                ],
                "url": f"https://open.spotify.com/album/{album_id}",
            }
            return data
        except Exception as e:
            logging.error(f"Error extracting album data: {e}")
            return {"error": str(e)}