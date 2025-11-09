import re

def parse_query(query: str):
    """
    Parse Spotify query or URL to detect entity type and ID.
    Examples:
        artist:4q3ewBCX7sLwd24euuV69X
        https://open.spotify.com/track/3PfIrDoz19wz7qK7tYeu62
    """
    patterns = {
        "artist": r"(?:artist[:/])([A-Za-z0-9]+)",
        "album": r"(?:album[:/])([A-Za-z0-9]+)",
        "track": r"(?:track[:/])([A-Za-z0-9]+)",
        "playlist": r"(?:playlist[:/])([A-Za-z0-9]+)",
    }

    for kind, pattern in patterns.items():
        match = re.search(pattern, query)
        if match:
            return {"type": kind, "id": match.group(1)}

    raise ValueError("Unable to parse query. Supported: artist, album, track, playlist.")