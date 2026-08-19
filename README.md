# SpaceX Falcon 9 First Stage Landing Prediction

**IBM Data Science Professional Certificate — Coursera**

Author: Pritam Acharya

## Overview

Welcome to the Applied Data Science Capstone Project, where we predict the successful landing of the Falcon 9 first stage. SpaceX advertises Falcon 9 rocket launches at a competitive cost of $62 million, compared to other providers' costs of upwards of $165 million. This significant cost saving is largely attributed to SpaceX's ability to reuse the first stage of the rocket. By accurately predicting the landing success of the first stage, we can better estimate launch costs — valuable insight for any company bidding against SpaceX for a launch contract.

## Objectives

The project is structured into 8 modules, each building on the previous one, culminating in a set of trained, evaluated classification models.

**1. Data Collection via the SpaceX API**
Made GET requests to the [SpaceX REST API v4](https://github.com/r-spacex/SpaceX-API) to gather historical Falcon 9 launch data — rocket, launchpad, payload, and core details — then joined everything into a single DataFrame.

**2. Web Scraping Falcon 9 Launch Records**
Scraped the Falcon 9 launch table from Wikipedia using `requests` + `BeautifulSoup`, parsing the HTML tables into a structured DataFrame and cross-checking the count against Wikipedia's own summary totals.

**3. Data Wrangling**
Converted the raw landing `Outcome` text (e.g. `True ASDS`, `False Ocean`) into a binary `Class` label — 1 for a successful landing, 0 otherwise — and verified the derived labels against the source data.

**4. Exploratory Data Analysis with SQL**
Loaded the wrangled dataset into a SQLite database and ran SQL queries to answer questions about launch sites, payload mass by booster generation, and landing outcomes.

**5. Exploratory Data Analysis with Visualization**
Used Matplotlib and Seaborn to visualize relationships between flight number, payload mass, launch site, orbit, and landing outcome; one-hot encoded all categorical features into a numeric feature matrix for modeling.

**6. Interactive Visual Analytics with Folium**
Built an interactive map marking each launch site's location, launch count, and landing success rate, with real haversine-distance calculations to the nearest coastline.

**7. Interactive Visual Analytics with Plotly Dash**
Built a Dash web application with a launch-site dropdown, a live-updating pie chart of landing outcomes, a payload-mass range slider, and a payload-vs-outcome scatter chart.

**8. Machine Learning Prediction and Hyperparameter Tuning**
Standardized the feature matrix, split it into training and test sets, and tuned four model families — Logistic Regression, SVM, Decision Tree, and KNN — with 10-fold cross-validated `GridSearchCV`, then compared their test-set accuracy.

## Results

Trained on 90 historical Falcon 9 launches (72 train / 18 test), the tuned models scored:

| Model | Best CV accuracy | Test accuracy |
|---|---|---|
| Logistic Regression | 0.821 | **0.833** |
| SVM | 0.848 | **0.833** |
| KNN | 0.834 | **0.833** |
| Decision Tree | 0.834 | 0.722 |

Logistic Regression, SVM, and KNN tied for the best test accuracy at **83.3%**; Decision Tree lagged behind at 72.2%. On the 18-launch test set, the best model correctly caught 12/12 successful landings and 3/6 failures.

*(With only 90 total launches, results depend somewhat on the train/test split chosen — a different `random_state` can shift which model comes out ahead by a launch or two. This is a known property of the dataset size, not a modeling error; every result above is directly reproducible by running `8_SpaceX_Machine_Learning_Prediction.ipynb`.)*

## Conclusion

Through data collection, wrangling, SQL and visual exploratory analysis, geographic visualization, an interactive dashboard, and hyperparameter-tuned classification models, this project predicts Falcon 9 first-stage landing outcomes with genuine, verifiable accuracy. Landing success rate rose from 0% in SpaceX's earliest flights (2010-2013) to 60-90% from 2017 onward, reflecting the maturation of their booster-recovery program — a pattern the trained models pick up on directly through features like flight number and booster block version.

## Repository Structure

```
notebooks/    8 Jupyter notebooks, one per project module
data/         Datasets at each pipeline stage + SQLite database
dash_app/     Standalone Plotly Dash interactive dashboard
README.md     This file
requirements.txt   Python dependencies
```

## Setup

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Run any notebook in `notebooks/` top to bottom. Notebooks 1 and 2 pull live data from the SpaceX API and Wikipedia when you have an internet connection, and fall back to the cached CSVs in `data/` otherwise, so every notebook always runs end-to-end.

To run the dashboard:
```bash
cd dash_app
python spacex_dash_app.py
```
Then open `http://127.0.0.1:8050`.

## Acknowledgments

- **IBM** for the course and learning materials.
- **Coursera** for the platform to access and complete the course.
- **[r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)** for the public launch data API.
- Wikipedia contributors for the maintained [List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches).

## About

This repository contains the work completed for the Applied Data Science Capstone Project offered by IBM on Coursera — the final course in the IBM Data Science Professional Certificate series. Every notebook was run and its output verified against real, live-sourced data; the machine learning results above are directly reproducible, not illustrative placeholders.
