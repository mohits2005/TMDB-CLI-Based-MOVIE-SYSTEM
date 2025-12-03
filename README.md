# TMDB-CLI-Based-MOVIE-SYSTEM
TMDB CLI Tool is a simple command-line application built in Python that fetches and displays movie information directly in the terminal using The Movie Database (TMDB) API. It supports multiple categories such as Popular, Top Rated, Upcoming, and Now Playing movies.

# TMDB CLI Tool

A simple command-line application to fetch and display movie data from the TMDB API.

## Features
- Get Now Playing movies
- Get Popular movies
- Get Top Rated movies
- Get Upcoming movies
- Graceful error handling
- Pretty terminal output

## Installation

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Add your TMDB API Key to `.env` file:
   TMDB_API_KEY=your_key_here

## Usage

python tmdb.py --type popular  
python tmdb.py --type top  
python tmdb.py --type upcoming  
python tmdb.py --type playing  

