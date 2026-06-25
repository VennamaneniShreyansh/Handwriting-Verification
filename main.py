from pathlib import Path

# Path to dataset
dataset_path = Path("data")   

folders = []
for folder in dataset_path.iterdir():
    if folder.is_dir():
        folders.append(folder)

print(f"Total Writers: {len(folders)}\n")

for folder in sorted(folders):
    image_files = [
        file for file in folder.iterdir()
        if file.is_file() and file.suffix.lower() in [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]
    ]

    print(f"{folder.name}: {len(image_files)} images")