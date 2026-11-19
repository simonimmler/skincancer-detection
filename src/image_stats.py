from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image

data = Path("data")
metadata = pd.read_csv(data / "HAM10000_metadata")
paths = {p.stem: p for p in data.rglob("*.jpg")}

rows = []
for image_id in metadata["image_id"]:
    with Image.open(paths[image_id]) as img:
        rgb = np.asarray(img.convert("RGB"), dtype=float)
        gray = np.asarray(img.convert("L"), dtype=float)
        saturation = np.asarray(img.convert("HSV"))[..., 1] / 255

    mean_rgb = rgb.reshape(-1, 3).mean(axis=0)
    h, w = gray.shape[0] // 10, gray.shape[1] // 10
    corners = np.stack([gray[:h, :w], gray[:h, -w:], gray[-h:, :w], gray[-h:, -w:]])

    rows.append({
        "image_id": image_id,
        "brightness": gray.mean(),              # mean luminance, 0-255
        "contrast": gray.std(),                 # RMS contrast, 0-255
        "saturation": saturation.mean(),        # mean HSV saturation, 0-1
        "red": mean_rgb[0] / mean_rgb.sum(),    # colour cast: share of R, G, B
        "green": mean_rgb[1] / mean_rgb.sum(),
        "blue": mean_rgb[2] / mean_rgb.sum(),
        "dark_corners": (corners < 20).mean(),  # share of near-black corner pixels (vignette)
    })

stats = metadata.merge(pd.DataFrame(rows), on="image_id").round(4)
stats.to_csv(data / "image_stats.csv", index=False)
print(stats.groupby("dataset")[["brightness", "contrast", "saturation", "dark_corners"]].mean())
