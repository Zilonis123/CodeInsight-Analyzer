
import magic


def is_text_file(file_path: str) -> bool:
    # check if a file is a text file
    mime = magic.Magic()
    file_type = mime.from_file(file_path)

    return "text" in file_type.lower()