from bs4 import BeautifulSoup


def clean_html(html):

    if html is None:
        return ""

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(separator=" ")

    return text.strip()