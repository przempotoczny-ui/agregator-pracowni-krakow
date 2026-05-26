import requests
from bs4 import BeautifulSoup
import json
import datetime
import os

def scrape_bip_pracownie():
    # To jest docelowo scraper BIPu
    # W pierwszej iteracji (dopóki nie znamy dokładnego URL bieżącego naboru), 
    # generujemy bezpieczny, ale pusty zrzut danych, żeby GitHub Actions nie psuł frontendu.
    print("Rozpoczynam przeszukiwanie BIP Kraków w poszukiwaniu ofert pracowni twórczych...")
    
    # URL to the main BIP culture section or search (placeholder until specific nabór is active)
    url = "https://www.bip.krakow.pl/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    offers = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # W przyszłości: tutaj dodamy logikę beautifulsoup parsującą tabele z ofertami KD-19
        # np: soup = BeautifulSoup(response.text, 'html.parser')
        # ...
        
        print(f"Znaleziono {len(offers)} nowych ofert.")
        
    except Exception as e:
        print(f"Błąd podczas scrapowania: {e}")
        
    return offers

def save_data(offers):
    # Ścieżka względem głównego folderu repozytorium
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data.json')
    
    # Zapiszmy pustą tablicę lub nowo pobrane oferty
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(offers, f, ensure_ascii=False, indent=4)
        
    print(f"Zapisano plik {filepath}")

if __name__ == "__main__":
    offers = scrape_bip_pracownie()
    save_data(offers)
