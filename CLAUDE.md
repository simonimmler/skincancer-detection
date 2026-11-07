# CLAUDE.md

Course project *Advanced Topics in AI* (Politechnika Wrocławska, WS 2026/27), author Simon Immler.
Question: how much does ImageNet pretraining help on HAM10000 with 5, 10 or 20 labelled lesions
per class? ResNet-18 in three regimes: frozen features, fine-tuning, from scratch (control).

## Working with Simon

- Simon writes the implementation himself. Explain, review and debug, but do not write the
  project code for him unless he asks for it explicitly.

## Design (from the report, `main.tex` in ShareLaTeX)

- Split only by `lesion_id`, never by image: 60 / 20 / 20 % of the lesions, stratified by diagnosis.
- Label budget k = 5, 10, 20 lesions per class, one image each; at least 3 seeds per cell.
- Fix hyperparameters on validation before any test evaluation.
- Headline metric: macro-F1 (plus balanced accuracy and per-class recall), mean ± std over seeds.
- `data/` and run results are not tracked.
- Course rule: group members may share code, but explanations, conclusions and recommendations
  must be individual.

## Milestones

a dataset (w/c 19 Oct) · b models (w/c 2 Nov) · c experiments, at least 2 test scenarios
(w/c 16 Nov) · d results (w/c 30 Nov) · e discussion (w/c 14 Dec) · f final report + talk
(w/c 11 and 18 Jan 2027)
