import mimetypes

def is_text_file(file_path: str) -> bool:
    # check if a file is a text file
    mime: str = mimetypes.guess_type(file_path)[0]

    isText = "text" in mime or ".json" in file_path # account for .json displaying as "application/json"
    return isText