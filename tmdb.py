import argparse
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMBD_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie"

MOVIE_TYPES = {
    "popular": "popular",
    "top": "top_rated",
    "upcoming": "upcoming",
    "playing": "now_playing"
}


def fetch_movies(movie_type):

    if movie_type not in MOVIE_TYPES:
        print("Invalid Type of the movie!, Use popular, top, upcoming, playing")
        return
    
    endpoint = f"{BASE_URL}/{MOVIE_TYPES[movie_type]}"
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}

    try:
        res = requests.get(endpoint, params=params)
        res.raise_for_status()
        data = res.json()

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return
    
    print(f"\n Showing {movie_type.upper()} movies:\n")
    for movie in data.get("results", [])[:10]:
        print(f"{movie["title"]}  ({movie.get('vote_average')})")
        print(f"Release: {movie.get('release_date')}")
        print()

def main():

    parser = argparse.ArgumentParser(description="TMBD CLI TOOL")
    parser.add_argument("--type", required=True, help="popular | top | upcoming | playing")
    args = parser.parse_args()

    fetch_movies(args.type)

if __name__ == "__main__":
    main()
    