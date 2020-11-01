import re
import sys
import pathlib
import shutil


def handle_image(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "images"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/path.name)


def handle_video(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "videos"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name)


def handle_document(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "documents"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name)


def handle_archive(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "archives"
    name, _ = split_extension(path.name)
    target_folder.mkdir(exist_ok=True)
    archive_folder = target_folder / name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(path.absolute()), str(archive_folder.absolute()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    path.unlink()


def handle_folder(path: pathlib.Path):
    try:
        path.rmdir()
    except OSError:
        pass


IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
ARCHIVES = []
FOLDERS = []
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
CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "e", "u", "ja")
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r"\W", "_", t_name)
    return t_name


def split_extension(file_name: str):
    ext_start = 0
    for idx, char in enumerate(file_name):
        if char == ".":
            ext_start = idx
    name = file_name[:ext_start]
    extension = file_name[ext_start+1:].upper()
    if not ext_start:
        return file_name, ""
    return name, extension


def scan(folder: pathlib.Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("images", "videos", "documents", "archives"):
                FOLDERS.append(item)
                scan(item)
            continue

        name, extension = split_extension(file_name=item.name)
        new_name = normalize(name)
        new_item = folder / ".".join([new_name, extension.lower()])
        item.rename(new_item)
        if extension:
            try:
                container = REGISTERED_EXTENSIONS[extension]
                container.append(new_item)
            except KeyError:
                continue


def main() -> None:
    path = sys.argv[1]
    print(f"Start in {path}")
    folder = pathlib.Path(path)
    scan(folder)

    for file in IMAGES:
        handle_image(file, folder)

    for file in VIDEO:
        handle_video(file, folder)

    for file in DOCUMENTS:
        handle_document(file, folder)

    for file in ARCHIVES:
        handle_archive(file, folder)

    for f in FOLDERS[::-1]:
        handle_folder(f)


if __name__ == "__main__":
    main()
