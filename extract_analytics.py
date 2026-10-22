import sys
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []

    def handle_data(self, data):
        clean_data = data.strip()
        if clean_data:
            self.text_content.append(clean_data)

def extract_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parser = TextExtractor()
        parser.feed(content)
        
        # Also look for interesting JSON blocks
        json_blocks = re.findall(r'<script type="text/json" data-serialized-id="server-data">(.*?)</script>', content, re.DOTALL)
        
        with open('extracted_analytics_data.txt', 'w', encoding='utf-8') as out:
            out.write("--- TEXT CONTENT ---\n")
            for line in parser.text_content:
                out.write(line + "\n")
            
            if json_blocks:
                out.write("\n--- JSON DATA BLOCKS ---\n")
                for block in json_blocks:
                    out.write(block + "\n")
                    
        print("Extraction complete. Results in extracted_analytics_data.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_from_html(sys.argv[1])
    else:
        print("Usage: python script.py <html_file>")
