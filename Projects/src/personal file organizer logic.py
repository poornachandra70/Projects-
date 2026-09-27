files = [
    "resume.pdf",
    "photo.jpg",
    "notes.txt",
    "project.py",
    "database.sql",
    "movie.mp4"
]

categories = {
    "Documents": [".pdf", ".txt", ".docx"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Code": [".py", ".java", ".sql"],
    "Videos": [".mp4", ".mkv"]
}

for file in files:

    category_found = False

    for category, extensions in categories.items():

        for extension in extensions:

            if file.endswith(extension):
                print(file, "->", category)
                category_found = True
                break

        if category_found:
            break

    if not category_found:
        print(file, "-> Other")