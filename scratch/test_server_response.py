import urllib.request

def main():
    url = "http://localhost:65097/evenements.html"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print("--- SERVER RESPONSE RECEIVED ---")
            print(f"Content Length: {len(html)}")
            print("First 500 characters:")
            print(html[:500])
            print("...")
            print("Last 500 characters:")
            print(html[-500:])
    except Exception as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    main()
