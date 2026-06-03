import pandas as pd
import requests
import time

all_shows = []
headers = {'User-Agent': 'Mozilla/5.0'}

# Loop from 1973 to 2026
for year in range(1973, 2027):
    url = f"https://www.kissconcerthistory.com/{year}/{year}.php"
    print(f"Scraping {year}...")
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            tables = pd.read_html(response.text)
            # We specifically grab Table 1, which we know contains the show data
            if len(tables) > 1:
                df = tables[1]
                df['Tour_Year'] = year
                all_shows.append(df)
                print(f"  -> Found {len(df)} shows.")
            else:
                print(f"  -> No data table found.")
        else:
            print(f"  -> Page not found.")
    except Exception as e:
        print(f"  -> Error: {e}")
        
    time.sleep(1) # Be a polite bot

# Save the final masterpiece
if all_shows:
    final_df = pd.concat(all_shows, ignore_index=True)
    final_df.to_csv("shows.csv", index=False)
    print("✅ MASTER DATABASE CREATED: shows.csv")