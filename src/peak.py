from pathlib import Path
import random

import pandas as pd
from PIL import Image, ImageDraw

data = Path("data")
metadata = pd.read_csv(data / "HAM10000_metadata")
paths = list(data.rglob("*.jpg"))
diagnoses = metadata.set_index("image_id")["dx"]

preview = Image.new("RGB", (900, 460), "white")
draw = ImageDraw.Draw(preview)

for i, path in enumerate(random.sample(paths, 6)):
    x, y = (i % 3) * 300, (i // 3) * 230

    with Image.open(path) as img:
        img.thumbnail((290, 200))
        preview.paste(img, (x, y))

    draw.text(
        (x + 5, y + 205),
        f"{path.stem} | {diagnoses[path.stem]}",
        fill="black",
    )

preview.show()