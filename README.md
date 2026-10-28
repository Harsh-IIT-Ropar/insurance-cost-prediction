# [TODO: Project title = your final problem statement]

[TODO: One line, e.g. "Predicts healthcare insurance charges from patient and lifestyle factors using linear regression (pandas, matplotlib, scikit-learn)."]

![AI101 Mini-Project](https://img.shields.io/badge/AI101-Mini--Project-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)

**Course:** AI101: Data Science and AI Essentials with Python, School of AI and Data Engineering, IIT Ropar
**Team no.:** [TODO]

## Team and roles

| Member | Entry no. | GitHub handle | Role |
|---|---|---|---|
| Rakshith A Y | 2026DAB1303 | [TODO @handle] | Video Lead |
| Nikhil Meena | 2026MCB1549 | [TODO @handle] | Execution Lead |
| Harsh Raj | 2026AIB1041 | [TODO @handle] | Documentation lead |
| Prem Kiran Gedala | 2026EEB1394 | [TODO @handle] | PPT Lead |

Roles to assign among the four: Documentation lead, Execution lead, PPT lead, Video lead.
*All four members contributed code (see commit history).*

## Problem and dataset

- **Problem:** [TODO: what is predicted or clustered, and why it matters]
- **Task:** [TODO: e.g. linear regression with `charges` as the target]
- **Dataset:** Healthcare Insurance Cost Prediction Dataset (Kaggle, by miadul): https://www.kaggle.com/datasets/miadul/healthcare-insurance-cost-prediction-dataset
- **File used:** `data/medical_insurance_cost_dataset_enhanced.csv`
- **Size:** 7,500 rows, 22 columns
- **Columns:**
  - Identifier: `customer_id`
  - Demographics: `age`, `gender`, `children`, `marital_status`, `region`, `occupation`, `annual_income_usd`
  - Lifestyle: `smoker`, `exercise_level`, `alcohol_consumption_per_week`, `sleep_hours`, `stress_level`
  - Health: `bmi`, `blood_pressure`, `cholesterol`, `diabetes`, `chronic_diseases`
  - Healthcare use: `doctor_visits_per_year`, `hospitalizations_last_year`
  - Insurance and cost: `insurance_plan`, `annual_medical_cost_usd`

## Project structure

```
[TODO: repo-name]/
├── data/
│   └── medical_insurance_cost_dataset_enhanced.csv
├── src/
│   ├── main.py            # entry point
│   └── [TODO: other scripts]
├── outputs/               # plots are saved here
├── docs/
│   └── [TODO: slides file]
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Tested on Python [TODO: version, e.g. 3.11] ([TODO: operating systems tested]).

```bash
git clone [TODO: repo URL]
cd [TODO: repo-name]
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Library versions are pinned in `requirements.txt`.

## How to run

1. Run `python src/main.py`
2. The script prints the model metrics and saves plots in `outputs/`
3. Expected runtime: [TODO]

## Expected output

[TODO: add a terminal screenshot, e.g. `![Expected output](docs/expected_output.png)`]

Plots saved in `outputs/`:
- [TODO: plot file names]

## Results

| Metric | Value |
|---|---|
| R² (test set) | [TODO] |
| RMSE | [TODO] |
| MAE | [TODO] |

[TODO: 2-3 lines on the key findings]

## Links

- Slides (5 slides): [TODO: `docs/<file>`]
- Video (max 5 min): [TODO: unlisted YouTube or Drive link]

## AI-use disclosure

- Claude (Anthropic): used by Harsh Raj for guidance on repo setup and for a first draft of this README's structure; reviewed and edited by Harsh Raj.
- [TODO: each other member adds the tool, what it was used for, and how they checked it]
- No AI was used to generate the dataset or the results.
