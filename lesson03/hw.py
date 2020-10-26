import os
import sys

# Это первый аргумент, считаем, что это валидный адрес в файловой сиситеме
path = sys.argv[1]
print(f"Start in {path}")

# Это список имен файлов и папок в path.
files = os.listdir(path)

IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
OTHER = []
EXTENSIONS = set()

REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
}
for file in files:
    unknown = True
    for extension in REGISTERED_EXTENSIONS.items():
        ext, container = extension
        if file.upper().endswith(ext):
            EXTENSIONS.add(ext)
            container.append(file)
            unknown = False
            break
    if unknown:
        OTHER.append(file)

print(f"Images: {IMAGES}")
print(f"Video files: {VIDEO}")
print(f"Documents: {DOCUMENTS}")
print(f"Audio files: {AUDIO}")
print(f"Unknown files: {OTHER}")
print(f"There are files of types: {EXTENSIONS}")
