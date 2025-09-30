# IMDb Top Rated Scraper

My first attempt at making a web scraper. This gets the top 25 items in IMDb filtered based on year and category.

## See for yourself

 1. **Clone the repository:**
    ```bash
    git clone [https://github.com/Shanwis/IMDb-Top-Rated-Web-Scraper](https://github.com/Shanwis/IMDb-Top-Rated-Web-Scraper)
    cd IMDb-Top-Rated-Web-Scraper
    ```

2.  **(Recommended) Create and activate a virtual environment:**
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    All dependencies are listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The script is run from the command line. You must provide a year. The type of content is optional and defaults to movies.

### Examples

**1. Get the top movies from 2023:**
```bash
python3 imdb_scraper.py --year 2023