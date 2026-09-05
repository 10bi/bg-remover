from pathlib import Path

from google.colab import files
from PIL import Image
from rembg import remove


def remove_background():
    uploaded_files = files.upload()

    for filename in uploaded_files:
        input_path = Path(filename)
        output_path = Path(f"{input_path.stem}_no_bg.png")

        with Image.open(input_path) as image:
            result = remove(image)
            result.save(output_path, "PNG")

        print(f"Background removed: {output_path}")

        files.download(output_path)


remove_background()
