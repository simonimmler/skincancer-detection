# HAM10000 with few labels — does ImageNet knowledge help?

Project for *Advanced Topics in AI* (Politechnika Wrocławska, winter 2026/27).
How much does an ImageNet-pretrained network help when only 5, 10 or 20 labelled dermatoscopic
lesions per class are available?

One backbone (ResNet-18, 7 classes), three training regimes:

| regime | initial weights | trained parameters | question |
|---|---|---|---|
| `frozen` | ImageNet-1k | linear head only | are ImageNet features useful as they are? |
| `finetune` | ImageNet-1k | all | does adapting them help further? |
| `scratch` | random | all | control: what does the data alone teach? |

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Put the dataset into `data/` (see [data/README.md](data/README.md)).

## Milestones

The report is written in ShareLaTeX (`main.tex`, one section per milestone); this repo holds
the code.

| | content | week of |
|---|---|---|
| a | dataset | 19 Oct 2026 |
| b | models | 2 Nov 2026 |
| c | experiments (at least 2 test scenarios) | 16 Nov 2026 |
| d | results | 30 Nov 2026 |
| e | discussion and conclusions | 14 Dec 2026 |
| f | final report and short talk | 11 / 18 Jan 2027 |
