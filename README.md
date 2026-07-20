# 📰 News Headline Scraper (Streamlit Web App)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

A clean, modern web application that scrapes **real news headlines** from any news website. Built with **Streamlit** for the GUI, **Requests** for fetching data, and **BeautifulSoup** for parsing HTML.

**Optimized for Dawn.com** – it extracts the actual news titles (ignoring ads, menus, and useless placeholder text).

---

## 🚀 Features

- ✅ **Real Headline Extraction**: Fetches actual story headlines using CSS selectors (targets `<h2 class="story__title">` for Dawn.com).
- ✅ **Interactive Web Interface**: User-friendly design built with Streamlit.
- ✅ **Robust Error Handling**: Catches invalid URLs, network timeouts, connection errors, and parsing failures gracefully.
- ✅ **Fast & Lightweight**: Executes scraping in seconds with real-time loading spinners.
- ✅ **Fallback Support**: If the `<h2>` selector doesn't work, it automatically falls back to `<h3>` tags.

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Web Framework**: [Streamlit](https://streamlit.io/)
- **HTTP Client**: [Requests](https://docs.python-requests.org/)
- **HTML Parser**: [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

---

## 📂 File Structure

```bash
news-scraper-streamlit/
│
├── app.py                 # Main Python script with GUI and scraping logic
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation (this file)
