import sys

# Reconfigure stdout to use utf-8 to prevent console encoding errors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

file_path = r"C:\Users\lyies\.gemini\antigravity\brain\a44ca3e1-2903-468d-8e12-9f5db0ad0571\.system_generated\steps\379\content.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in file: {len(lines)}")

# Search for alma-ring or tresor-ring
for i, line in enumerate(lines):
    if 'alma-ring' in line.lower() or 'tresor-ring' in line.lower():
        clean_line = line.strip().encode('utf-8', errors='replace').decode('utf-8')
        print(f"Line {i+1}: {clean_line[:200]}")
        # Print surrounding 5 lines
        start = max(0, i - 5)
        end = min(len(lines), i + 6)
        print("Surrounding lines:")
        for j in range(start, end):
            clean_surround = lines[j].strip().encode('utf-8', errors='replace').decode('utf-8')
            print(f"  {j+1}: {clean_surround[:200]}")
        print("-" * 50)
