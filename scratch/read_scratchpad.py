import os

def main():
    folder = "C:/Users/lyies/.gemini/antigravity/brain/670b9af0-cf4f-4e9b-bfc1-2de0fc05fd9b/browser"
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return
        
    for f in os.listdir(folder):
        if f.endswith('.md'):
            path = os.path.join(folder, f)
            print(f"--- File: {f} ---")
            with open(path, 'r', encoding='utf-8') as file_obj:
                print(file_obj.read())

if __name__ == "__main__":
    main()
