import json
import sys
from pathlib import Path
from extractors.artist_extractor import ArtistExtractor
from extractors.playlist_extractor import PlaylistExtractor
from extractors.album_extractor import AlbumExtractor
from extractors.track_extractor import TrackExtractor
from utils.query_parser import parse_query
from utils.format_converter import FormatConverter

CONFIG_PATH = Path(__file__).parent / "config" / "settings.json"

def load_settings():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️  settings.json not found. Using defaults.")
        return {"output_format": "json"}

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <query_or_url> [output_format]")
        sys.exit(1)

    query = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else None

    settings = load_settings()
    output_format = output_format or settings.get("output_format", "json")

    parsed = parse_query(query)
    entity_type = parsed["type"]
    identifier = parsed["id"]

    print(f"🔍 Extracting {entity_type} data for {identifier}...")

    if entity_type == "artist":
        data = ArtistExtractor().extract(identifier)
    elif entity_type == "playlist":
        data = PlaylistExtractor().extract(identifier)
    elif entity_type == "album":
        data = AlbumExtractor().extract(identifier)
    elif entity_type == "track":
        data = TrackExtractor().extract(identifier)
    else:
        print("Unknown entity type. Supported: artist, album, track, playlist")
        sys.exit(1)

    converter = FormatConverter()
    output_data = converter.convert(data, output_format)

    output_path = Path("output") / f"{identifier}.{output_format}"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_data)

    print(f"✅ Extraction complete. Saved to {output_path}")

if __name__ == "__main__":
    main()