import logging

logging.basicConfig(level=logging.INFO)

class TrackExtractor:
    def __init__(self, token=None):
        self.token = token or "mock_token"

    def extract(self, track_id: str):
        logging.info(f"Fetching track data for {track_id}")
        try:
            data = {
                "id": track_id,
                "name": "Blinding Lights",
                "artist": "The Weeknd",
                "album": "After Hours",
                "duration_ms": 200040,
                "playcount": 1845093800,
                "url": f"https://open.spotify.com/track/{track_id}",
            }
            return data
        except Exception as e:
            logging.error(f"Error extracting track data: {e}")
            return {"error": str(e)}