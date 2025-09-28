import requests
import argparse
from bs4 import BeautifulSoup

def main():

    parser = argparse.ArgumentParser(description="Scrape top titles from IMDb")
    parser.add_argument('-y', '--year', required = True, type=int, help='The year to search')
    parser.add_argument('-t', '--type', default='movies', help="The title type(movies, tv, video game)")

    args = parser.parse_args()

    year = str(args.year)
    type = args.type
    type_list = [item.strip() for item in type.split(',')]
    type_map = {
        "tv": "tv_series",
        "video games": "video_game",
        "video game": "video_game",
        "movies": "feature"
    }
    type_string = ",".join([type_map.get(i.lower(), i) for i in type_list])

    header = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    url = "https://www.imdb.com/search/title/?title_type=" + type_string + "&release_date=" + year + "," + year

    try:
        request = requests.get(url,headers = header)
        request.raise_for_status()

        soup = BeautifulSoup(request.text, 'html.parser')
        print(f"Top rated {type} in {year} on IMDb:")
        tag = soup.find_all('div', class_='ipc-metadata-list-summary-item__c')
        if len(tag) == 0:
            print("No results found!")
        else:
            for i in tag:
                final = i.find('h3','ipc-title__text ipc-title__text--reduced')
                print(final.text.strip())

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()