import logging

logging.basicConfig(level=logging.INFO)

class PlaylistExtractor:
    def __init__(self, token=None):
        self.token = token or "mock_token"

    def extract(self, playlist_id: str):
        logging.info(f"Fetching playlist data for {playlist_id}")
        try:
            data = {
                "id": playlist_id,
                "name": "Top Global 50",
                "followers": 12234355,
                "tracks": [
                    {"id": "5KawlOMHjWeUjQtnuRs22c", "name": "Save Your Tears"},
                    {"id": "6habFhsOp2NvshLv26DqMb", "name": "Blinding Lights"},
                ],
                "url": f"https://open.spotify.com/playlist/{playlist_id}",
            }
            return data
        except Exception as e:
            logging.error(f"Error extracting playlist data: {e}")
            return {"error": str(e)}