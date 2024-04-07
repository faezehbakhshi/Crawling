# Website Crawler

## Overview

This project implements a website crawler for extracting data from websites with similar HTML structure. It is designed to fetch data from a specific website, parse HTML content, and store the extracted data into a PostgreSQL database. The crawler is built using Python and utilizes libraries such as `requests`, `BeautifulSoup`, `pandas`, and `sqlalchemy`.

## Features

- Fetch HTML content from a specified range of pages on the target website.
- Parse HTML content to extract tabular data.
- Store extracted data into a PostgreSQL database.
- Supports configurable mapping of column names from website HTML to DataFrame and database.

## Setup

1. **Clone the repository:**
    ```
    git clone https://github.com/yourusername/website-crawler.git
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Configure the database connection and website URL:**
    - Edit `config/db_configs.yaml` file to provide your PostgreSQL database connection details and table configuration.
    - Update the `base_url` variable in the script with the URL of the website you want to crawl.

## Usage

Run the `crawler.py` script to start crawling the website:
```
python crawler.py
```
The crawler will fetch HTML content from the specified range of pages, parse it, and store the extracted data into the configured PostgreSQL database.

## Configuration

- `config/db_configs.yaml`: Contains database connection details and table configuration.
- `crawler.py`: Defines the crawler class and main crawling logic. Modify `base_url` in this file to crawl a different website.
