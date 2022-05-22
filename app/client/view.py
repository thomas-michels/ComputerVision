"""
    Module for save file
"""

def save_file(files):
    with open("app/static/images/image.jpg", "wb") as image:
            image.write(files[0])
            image.close()

    return {"file_sizes": [len(file) for file in files]}
