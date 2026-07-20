import streamlit as st
import requests
from bs4 import BeautifulSoup

# Set page configuration (Title and layout)
st.set_page_config(
    page_title="News Headline Scraper",
    page_icon="📰",
    layout="centered"
)

def scrape_real_headlines(url: str) -> list:
    """
    Fetches the webpage, parses it, and extracts REAL news headlines.
    Specifically optimized for Dawn.com (targeting <h2 class='story__title'>).

    Args:
        url (str): The URL of the news website.

    Returns:
        list: A list of cleaned real headline strings.

    Raises:
        ValueError: If the URL is empty.
        requests.exceptions.RequestException: If the network request fails.
        Exception: If no headlines are found.
    """
    if not url.strip():
        raise ValueError("URL cannot be empty.")

    # Mimic a real browser to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Send GET request
    response = requests.get(url, headers=headers, timeout=10)

    # Raise exception if status code is not 200
    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"Server returned status code: {response.status_code}")

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # ----------------------------------------------------------------
    # TARGETING REAL HEADLINES:
    # Dawn.com ke asli headlines <h2 class="story__title"> mein hain.
    # Agar kisi aur site ke liye run karna hai, toh yahan selector change karein.
    # ----------------------------------------------------------------
    headline_tags = soup.find_all('h2', class_='story__title')

    # Agar asli headlines nahi milin, toh fallback ke taur par <h3> check karein (optional)
    if not headline_tags:
        headline_tags = soup.find_all('h3')

    if not headline_tags:
        raise Exception("No news headlines found on this page. The website structure might have changed.")

    # Extract clean text
    headlines = []
    for tag in headline_tags:
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

# ------------------------------------------------------------------
# STREAMLIT UI (Frontend)
# ------------------------------------------------------------------
def main():
    st.title("📰 Real News Headline Scraper")
    st.markdown("Extract the latest **real news headlines** from any website (optimized for Dawn.com).")

    # Input field for URL
    url = st.text_input("Enter News Website URL:", value="https://www.dawn.com/")

    # Fetch Button
    if st.button("🚀 Fetch Real Headlines"):
        if url:
            with st.spinner("Fetching headlines... Please wait..."):
                try:
                    # Call the scraping function
                    headlines = scrape_real_headlines(url)

                    # Display results
                    st.success(f"Successfully fetched {len(headlines)} headlines from {url}!")
                    st.divider()

                    # Display headlines in a clean numbered list
                    for idx, headline in enumerate(headlines, start=1):
                        st.markdown(f"**{idx}.** {headline}")

                except ValueError as e:
                    st.error(f"⚠️ Input Error: {e}")
                except requests.exceptions.ConnectionError:
                    st.error("🌐 Connection Error: Failed to connect. Check your internet.")
                except requests.exceptions.Timeout:
                    st.error("⏱️ Timeout Error: The server took too long to respond.")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Request Error: {e}")
                except Exception as e:
                    st.error(f"⚠️ Parsing Error: {e}")
        else:
            st.warning("Please enter a valid URL first!")

if __name__ == "__main__":
    main()
