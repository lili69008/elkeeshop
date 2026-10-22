import urllib.request
import urllib.error

def main():
    url = "http://localhost:65097/evenements.html"
    try:
        print(f"Connecting to {url}...")
        response = urllib.request.urlopen(url, timeout=5)
        print("Success!")
        print("Status code:", response.getcode())
        print("Headers:", dict(response.info()))
        html = response.read(1000)
        print("First 1000 chars of HTML:")
        print(html.decode('utf-8', errors='ignore'))
    except urllib.error.URLError as e:
        print("Failed to connect:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
