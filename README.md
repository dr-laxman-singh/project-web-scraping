# IPL Auction 2022 Web Scraper 🏏

A Python-based web scraping project that extracts IPL 2022 Auction data from the official IPL website and stores it in a CSV file using **BeautifulSoup**, **Requests**, and **Pandas**.

## 📌 Features

* Scrapes IPL 2022 Auction data directly from the IPL website.
* Extracts table headers and player auction details.
* Stores the scraped data in a Pandas DataFrame.
* Exports the data to a CSV file.
* Supports UTF-8 encoding for proper text handling.

## 🛠️ Technologies Used

* Python 3.x
* Requests
* BeautifulSoup4
* Pandas
* lxml

## 📂 Project Structure

```
MINI-PROJECT/
│
├── scraper.py
├── IPL Auction Status 2022.csv
├── requirements.txt
└── README.md
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dr-laxman-singh/project-web-scraping.git
cd MINI-PROJECT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests beautifulsoup4 pandas lxml
```

## ▶️ Usage

Run the script:

```bash
python scraper.py
```

After successful execution:

* Auction data will be displayed in the terminal.
* A CSV file named **"IPL Auction Status 2022.csv"** will be generated in the project directory.

## 📋 Output Example

| Team | Player          | Role          | Price     |
| ---- | --------------- | ------------- | --------- |
| CSK  | Ravindra Jadeja | All-rounder   | ₹16 Cr    |
| MI   | Ishan Kishan    | Wicket Keeper | ₹15.25 Cr |

*(Actual columns depend on the data available on the IPL website.)*

## 🔍 How It Works

1. Sends an HTTP request to the IPL Auction 2022 webpage.
2. Parses the HTML content using BeautifulSoup.
3. Locates the auction table.
4. Extracts headers and row data.
5. Creates a Pandas DataFrame.
6. Saves the extracted data as a CSV file.

## 📦 Required Libraries

```text
requests
beautifulsoup4
pandas
lxml
```

## ⚠️ Disclaimer

This project is intended for educational and learning purposes only. Data belongs to the official IPL website. Ensure compliance with the website's terms of service before scraping.

## 👨‍💻 Author

Developed as a Python Web Scraping project for learning data extraction, HTML parsing, and CSV data storage.

