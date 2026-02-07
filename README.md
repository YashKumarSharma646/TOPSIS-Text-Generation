# Applying TOPSIS to Select the Best Text Generation Model

## Overview

This project applies the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method to rank multiple pre-trained text generation models using a structured multi-criteria decision-making approach.

Rather than selecting a model based on a single performance metric, this work evaluates models across multiple dimensions including language quality and computational efficiency, and produces an objective ranking.

---

## Problem Statement

When selecting a pre-trained text generation model, multiple criteria must be considered:

- Some metrics should be maximized (e.g., BLEU, ROUGE)
- Some metrics should be minimized (e.g., Perplexity, Inference Time, Model Size)

The challenge is to determine the best model when criteria conflict with one another.

TOPSIS provides a mathematical framework to rank alternatives based on their relative distance from an ideal best and ideal worst solution.

---

## Models Compared

- GPT-2  
- DistilGPT2  
- T5-Small  
- FLAN-T5-Base  

---

## Evaluation Criteria

| Criterion        | Type       | Objective |
|------------------|------------|------------|
| Perplexity       | Cost (-)   | Lower is better |
| BLEU Score       | Benefit (+)| Higher is better |
| ROUGE-L Score    | Benefit (+)| Higher is better |
| Inference Time   | Cost (-)   | Lower is better |
| Model Size (MB)  | Cost (-)   | Lower is better |

---

## Criteria Weights

The following weights were assigned to reflect the relative importance of each criterion:

[0.25, 0.25, 0.20, 0.15, 0.15]

Greater emphasis is placed on language quality metrics (Perplexity, BLEU, ROUGE) while also considering computational efficiency (Time and Size).

---

## TOPSIS Methodology

The ranking process follows these steps:

1. Construct the decision matrix  
2. Normalize the matrix using vector normalization  
3. Apply weights to the normalized matrix  
4. Determine the Ideal Best and Ideal Worst solutions  
5. Compute Euclidean distances from both ideals  
6. Calculate the TOPSIS score  
7. Rank alternatives based on the score  

Final score formula:

Ci = S- / (S+ + S-)

Where:
- S+ = Distance from ideal best  
- S- = Distance from ideal worst  

A higher score indicates a better alternative.

---

## Project Structure

```
TOPSIS-Text-Generation/
│
├── data/
│   └── decision_matrix.csv
│
├── results/
│   ├── normalized_matrix.csv
│   ├── weighted_matrix.csv
│   └── topsis_scores.csv
│
├── outputs/
│   ├── ranking_plot.png
│   ├── heatmap.png
│   └── analysis.html
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── topsis.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Visualization

### Model Ranking

![Ranking Plot](outputs/ranking_plot.png)

### Normalized Decision Matrix Heatmap

![Heatmap](outputs/heatmap.png)

---

## Final Ranking

Refer to `results/topsis_scores.csv` for the complete ranking output.

The model with the highest TOPSIS score is considered the most balanced and optimal alternative under the selected criteria and weights.

---

## Detailed Analysis Notebook

A step-by-step explanation of the methodology and intermediate matrices is available here:

[View Full Analysis (HTML)](outputs/analysis.html)

---

## How to Run

Clone the repository and execute:

pip install -r requirements.txt
python main.py


This will:

- Load the decision matrix  
- Apply TOPSIS  
- Generate ranking scores  
- Save intermediate matrices  
- Produce visualization plots  

---

## Why TOPSIS?

- Handles conflicting criteria effectively  
- Provides objective mathematical ranking  
- Balances performance and computational constraints  
- Suitable for model selection in practical machine learning systems  

---

## Future Work

- Automate metric extraction from real model evaluations  
- Extend comparison to larger language models  
- Include additional evaluation metrics such as BERTScore  
- Develop an interactive dashboard for dynamic model comparison  

---

## Author

Yash Sharma  
B.Tech Data Science  
Sixth Semester