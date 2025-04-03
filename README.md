# 414_final

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Final project for 414 project using the GSS data.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         414_final and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── 414_final   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes 414_final a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

## Project Description:

This project will investigate the relationship between **social acceptance and loneliness**. Using data from the GSS, particuarlly looking at how social frequency (how often an indvidiual sees their peers throughout a year) and poor mental health days (the number of poor mental health days in a month) relate and whether this relationship is mediated by life satisfaction (including self-satisfaction, career satisfaction and career satisfaction). The analysis involves data cleaning, feature engineering, statistical modeling, and visualization.

## Dependencies

To ensure reproducibility, the following dependencies should be installed:
- Python 3.8+
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- statsmodels
- jupyter
Install all dependencies by using
"pip install -r requirements.txt"

## Environment Setup
To create and activate a virtual enviroment:
    python -m venv env
    source env/bin/activate
Then instal dependencies
    pip install -r requirements.txt


## Running the Data Processing Pipeline
To clean and preprocess the dataset:
    python src/dataset.py
    python src/features.py
This script:
- Loads raw data from data/raw/
- Processes and transforms it into data/processed/

## Training and Evaluating Models
To train the model and evaluate performance:
    python src/modeling/train.py
    python src/modeling/predict.py
This:
- Trains a model using processed features
- Saves the trained model to models/
- Generates predictions and evaluation metrics

## Reproducing Results
To reproduce the full work
    make all  # If using Makefile # OR manually run:
    python src/dataset.py
    python src/features.py
    python src/modeling/train.py
    python src/modeling/predict.py


## Contributors:
    Brynn Saffer -  University of Maryland
--------

