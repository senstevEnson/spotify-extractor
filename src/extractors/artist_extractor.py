import requests
import logging

logging.basicConfig(level=logging.INFO)

class ArtistExtractor:
    BASE_URL = "https://api.spotify.com/v1/artists/"

    def __init__(self, token=None):
        self.token = token or "mock_token"

    def extract(self, artist_id: str):
        logging.info(f"Fetching artist data for {artist_id}")
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            # Mocked response for demo; replace with real API in production
            data = {
                "id": artist_id,
                "name": "Bad Bunny",
                "followers": 95289827,
                "genres": ["reggaeton", "latin trap"],
                "url": f"https://open.spotify.com/artist/{artist_id}",
                "topTracks": [
                    {"id": "3sK8wGT43QFpWrvNQsrQya", "name": "DtMF", "playcount": 736953579}
                ],
            }
            return data
        except Exception as e:
            logging.error(f"Error extracting artist data: {e}")
            return {"error": str(e)}