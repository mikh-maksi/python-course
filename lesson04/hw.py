import sys
import pathlib


IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
OTHER = []
ARCHIVES = []
UNKNOWN = set()
EXTENSIONS = set()

REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'PDF': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}


def get_extension(file_name: str) -> str:
    ext_start = 0
    for idx, char in enumerate(file_name):
        if char == ".":
            ext_start = idx
    return file_name[ext_start+1:].upper()


def scan(folder: pathlib.Path):
    for item in folder.iterdir():
        if item.is_dir():
            scan(item)
            continue

        extension = get_extension(file_name=item.name)
        if not extension:
            OTHER.append(item.name)
        else:
            try:
                container = REGISTERED_EXTENSIONS[extension]
                EXTENSIONS.add(extension)
                container.append(item.name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(item.name)


if __name__ == "__main__":
    # Это первый аргумент, считаем, что это валидный адрес в файловой сиситеме
    path = sys.argv[1]
    print(f"Start in {path}")

    # Это список имен файлов и папок в path.
    arg = pathlib.Path(path)
    scan(arg)

    print(f"Images: {IMAGES}")
    print(f"Video files: {VIDEO}")
    print(f"Documents: {DOCUMENTS}")
    print(f"Audio files: {AUDIO}")
    print(f"Unknown files: {OTHER}")
    print(f"There are files of types: {EXTENSIONS}")
    print(f"Unknown file types: {UNKNOWN}")
