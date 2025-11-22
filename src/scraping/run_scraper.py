from web_scraper import WebScraper
import requests

def main():

    webscraper = WebScraper()
    urls_to_scrape = [
        "https://liquipedia.net/fighters/Street_Fighter_6/Tier_1_Tournaments",
        "https://liquipedia.net/fighters/Street_Fighter_6/Tier_2_Tournaments",
        "https://liquipedia.net/fighters/Street_Fighter_6/Tier_3_Tournaments"
    ]
    lp_tourney_urls = []

    for url in urls_to_scrape:
        lp_tourney_urls += webscraper.grab_urls(url)

    try:
        api_url = "http://localhost:3000/tournaments/index"
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching indexed tournaments: {e}")
        data = []

    indexed_tourneys = {item["liquidpedia_url"] for item in data}
    lp_tourney_urls = [url for url in lp_tourney_urls if url not in indexed_tourneys]
    webscraper.write_to_csv(webscraper.grab_slugs(lp_tourney_urls), "out")


if __name__ == "__main__":
    main()