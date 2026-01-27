# Project Overview: My Top 10 Movies Website (Day 64)

## Program Description
This application is a Flask-based website that allows users to create a curated list of their favorite movies. It utilizes:
- **Flask**: For the web framework.
- **Flask-SQLAlchemy**: For database interactions (SQLite).
- **Flask-WTF**: For form handling.
- **Flask-Bootstrap**: For styling.
- **The Movie Database (TMDB) API**: To fetch movie details (title, year, description, poster).

**Key Features:**
- **Home Page**: Lists movies from the database, sorted by rating.
- **Add Movie**: detailed flow where the user searches for a title, selects the correct movie from TMDB results, and saves it to the local database.
- **Edit Movie**: Allows updating the personal rating and review.
- **Delete Movie**: Removes a movie from the list.

## Observed Problems & TODOs

### 1. Critical Logic Errors in `add_movie` Route
**File:** `day_64_build_a_list_site/main.py`
**Lines:** 85-88
- **Malformed URL**: `f'https://api.themoviedb.org/3/movie/{id}'` needs correct formatting.
- **Incorrect API Response Handling**: `movie['results']` does not exist in the single movie detail response.
- **Undefined Variable**: `data` is used but never defined.
- **Confused Logic**: `movie['results'][id]` attempts to access a list structure that doesn't match the API response for a single movie.

### 2. Hardcoded Secrets & Global Variable Scope Issues
**File:** `day_64_build_a_list_site/main.py`
**Lines:** 24, 29, 33
- **API Key**: The TMDB Bearer token is hardcoded.
- **Global Variables**: `URL`, `HEADERS`, and `PARAMS` (which uses an undefined `query`) are defined globally, which might cause issues or be harder to maintain. `PARAMS` specifically relies on `query` which is not available at the module level.

### 3. Missing Ranking Logic
**File:** `day_64_build_a_list_site/main.py`
**Line:** 102 (approx, inside `home` route)
- The `home` route sorts by rating but does not update the `ranking` field (1 to 10) in the database.

### 4. Data Type Mismatch
**File:** `day_64_build_a_list_site/main.py`
**Line:** 59
- `EditForm.rating` is a `StringField`, but `Movie.rating` is a `Float`. This allows users to enter non-numeric text, which could cause errors.

## Recommended Order of Operations

1.  **Fix `add_movie` Logic**: Resolve the critical crashes in the add movie flow.
2.  **Fix Scope Issues**: Move `URL`, `HEADERS`, `PARAMS` inside the function or correct their definition.
3.  **Implement Ranking**: Update the `home` route to calculate and save rankings.
4.  **Refactor Forms**: Change the rating field to a numeric type.