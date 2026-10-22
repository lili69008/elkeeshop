import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

file_path = r"C:\Users\lyies\.gemini\antigravity\brain\a44ca3e1-2903-468d-8e12-9f5db0ad0571\.system_generated\steps\400\content.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in file: {len(lines)}")

# Search for alma
for i, line in enumerate(lines):
    line_lower = line.lower()
    if 'alma' in line_lower:
        clean_line = line.strip().encode('utf-8', errors='replace').decode('utf-8')
        print(f"Line {i+1}: {clean_line[:150]}")
