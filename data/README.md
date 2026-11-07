# Data folder

Put the HAM10000 files here (they are not part of the repository):

1. Harvard Dataverse, DOI [10.7910/DVN/DBW86T](https://doi.org/10.7910/DVN/DBW86T)
   – accept the terms, download `HAM10000_images_part_1.zip`, `HAM10000_images_part_2.zip`
   and the metadata file (download it in its original format, `HAM10000_metadata.csv`;
   a tab-separated `.tab` download works too — rename it to `HAM10000_metadata.csv`, the loader
   detects the separator).
2. Unzip both image archives below this folder. Any sub-folder layout is fine: the loader
   searches `data/` recursively for `<image_id>.jpg`.

Expected result:

```
data/
  HAM10000_metadata.csv
  HAM10000_images_part_1/ISIC_0024306.jpg ...
  HAM10000_images_part_2/ISIC_0029306.jpg ...
```

Columns used: `lesion_id` (groups images of the same lesion), `image_id`, `dx` (diagnosis:
akiec, bcc, bkl, df, mel, nv, vasc). `dx_type`, `age`, `sex` and `localization` are not used.
