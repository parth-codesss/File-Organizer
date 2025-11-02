# WAP of File Organizer
import os
import shutil

path = "C:\\Parth\\"
files = os.listdir(path)

categories = {
    "images": ['.jpeg', '.png'],
    "document": ['.txt'],
    "videos": ['.mp3', '.mp4']
}

for file in files:
    source = os.path.join(path, file)

    if os.path.isdir(source):
        continue

    name, ext = os.path.splitext(file)
    ext = ext.lower()

    found = False

    for category, extension in categories.items():
        if ext in extension:
            dest = os.path.join(path, category)
            found = True
            break

    if not found:
        dest = os.path.join(path, "others")

    os.makedirs(dest, exist_ok=True)

    if not os.path.exists(os.path.join(dest, file)):
        shutil.move(source, dest)

print("Files organized successfully...")
