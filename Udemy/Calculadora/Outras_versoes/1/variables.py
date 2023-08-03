from pathlib import Path

ROOT_DIR = Path(__file__).parent
print(60*'-')
print(ROOT_DIR)
print(60*'-')

FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'