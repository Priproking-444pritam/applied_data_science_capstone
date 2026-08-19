# SpaceX Falcon 9 First Stage Landing Prediction

**Applied Data Science Capstone — IBM Data Science Professional Certificate**

Author: Pritam Acharya

## Overview

SpaceX advertises Falcon 9 rocket launches at a cost of $62 million, compared to other providers' costs of upwards of $165 million each. Much of the savings comes from SpaceX's ability to reuse the first stage of the rocket. This project builds a full data science pipeline — from raw data collection through to a trained classification model — to predict whether the Falcon 9 first stage will land successfully, which is a strong proxy for estimating launch cost.

## Pipeline

| # | Notebook | What it does |
|---|---|---|
| 1 | [`1_jupyter-labs-spacex-data-collection-api.ipynb`](notebooks/1_jupyter-labs-spacex-data-collection-api.ipynb) | Collects historical launch data from the [SpaceX REST API v4](https://github.com/r-spacex/SpaceX-API) |
| 2 | [`2_jupyter-labs-webscraping.ipynb`](notebooks/2_jupyter-labs-webscraping.ipynb) | Scrapes the Falcon 9 launch table from Wikipedia with BeautifulSoup |
| 3 | [`3_jupyter-labs-spacex-Data-wrangling.ipynb`](notebooks/3_jupyter-labs-spacex-Data-wrangling.ipynb) | Cleans the data and derives the binary landing-success `Class` label |
| 4 | [`4_jupyter-labs-eda-sql.ipynb`](notebooks/4_jupyter-labs-eda-sql.ipynb) | Loads the data into SQLite and explores it with SQL |
| 5 | [`5_jupyter-labs-eda-dataviz.ipynb`](notebooks/5_jupyter-labs-eda-dataviz.ipynb) | Visual EDA with Matplotlib/Seaborn, plus feature engineering (one-hot encoding) |
| 6 | [`6_lab_jupyter_launch_site_location.ipynb`](notebooks/6_lab_jupyter_launch_site_location.ipynb) | Interactive map of launch sites with Folium |
| 7 | [`7_dash_app_verification.ipynb`](notebooks/7_dash_app_verification.ipynb) | Verifies the data logic behind the interactive dashboard |
| 8 | [`8_SpaceX_Machine_Learning_Prediction.ipynb`](notebooks/8_SpaceX_Machine_Learning_Prediction.ipynb) | Trains and compares Logistic Regression, SVM, Decision Tree, and KNN classifiers |

Plus a standalone interactive dashboard: [`dash_app/spacex_dash_app.py`](dash_app/spacex_dash_app.py) (Plotly Dash).

## Key results

- Collected and cleaned **90 Falcon 9 launches** (through November 2020) from the SpaceX API, cross-checked against Wikipedia's launch records.
- Landing success rate climbed from **0%** (2010-2013) to **60-90%** (2017 onward) as SpaceX matured its booster-recovery process.
- **KSC LC-39A** and **VAFB SLC-4E** both show a ~77% landing success rate; **CCAFS SLC-40** (the busiest pad, with the most early flights) sits at 60%.
- After hyperparameter tuning with `GridSearchCV` across 4 model families, **Logistic Regression, SVM, and KNN all tied at 83.3% test accuracy**; Decision Tree lagged at 72.2%.

## Setup

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

Open any notebook in `notebooks/` with Jupyter or VS Code and run all cells. Notebooks 1 and 2 pull live data from the SpaceX API and Wikipedia respectively when you have an internet connection; both fall back to the cached CSVs in `data/` if the live source is unreachable, so every notebook can always be re-run end-to-end.

To run the interactive dashboard:

```bash
cd dash_app
python spacex_dash_app.py
```

Then open `http://127.0.0.1:8050` in your browser.

## Repository structure

```
notebooks/    8 Jupyter notebooks, one per pipeline stage
data/         Datasets at each stage (raw, wrangled, feature-engineered) + SQLite db
dash_app/     Standalone Plotly Dash interactive dashboard
```

## Acknowledgments

- **IBM** and **Coursera** for the Applied Data Science Capstone course structure and methodology.
- **[r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)** for the public launch data API.
- Wikipedia contributors for the maintained [List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches).
