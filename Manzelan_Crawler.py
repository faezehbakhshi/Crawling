import os
import time
import yaml
import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

class WebsiteCrawler:
    def __init__(self, base_url, config_path):
        self.base_url = base_url
        self.config = self._load_config(config_path)
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    @staticmethod
    def _load_config(config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def _crawl_for_pages(self, page_number):
        url = f"{self.base_url}?page={page_number}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            time.sleep(1)  # Delay to avoid server overload
            return response.text
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def _parse_html(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find('table', class_='table')
        rows = table.find_all('tr')[1:]  # Skip header row
        data = [[td.get_text(strip=True) for td in tr.find_all('td')] for tr in rows]
        return pd.DataFrame(data, columns=self.config['table_columns'])

    def _save_to_database(self, dataframe):
        engine = create_engine(self.config['database_uri'])
        dataframe.to_sql(name=self.config['table_name'], con=engine, index=False,
                         if_exists='append', schema=self.config['schema'])

    def crawl_website(self, start_page, end_page):
        for page_number in range(start_page, end_page + 1):
            html_content = self._crawl_for_pages(page_number)
            if html_content:
                dataframe = self._parse_html(html_content)
                self._save_to_database(dataframe)

if __name__ == '__main__':
    BASE_URL = "http://www.manzelan.com/realEstate/realEstateList.php/"
    CONFIG_PATH = "config/db_configs.yaml"

    crawler = WebsiteCrawler(BASE_URL, CONFIG_PATH)
    crawler.crawl_website(2072, 6000)