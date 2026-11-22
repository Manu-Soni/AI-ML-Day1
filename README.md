# House Price Prediction

A beginner-friendly machine learning example that uses scikit-learn's linear
regression model to estimate a house price from its size.

## Project files

- `house_prediction.py` trains the model, shows two example predictions, and
  prompts you to enter a house size of your own.
- `requirements.txt` lists the Python package needed to run the project.

## Requirements

- Python 3.9 or newer
- pip

## Setup and run

Open a terminal in this project folder, then run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
source .venv/bin/activate
```

Install the dependency and run the program:

```bash
python -m pip install -r requirements.txt
python house_prediction.py
```

When prompted, enter a positive house size in square feet. The program prints
the estimated price in lakh rupees. The training set contains only five
example houses, so these predictions are for learning purposes and should not
be used as real property valuations.

## How the model works

1. `HOUSE_SIZES` contains the house sizes used for training.
2. `HOUSE_PRICES` contains the corresponding prices, in lakh rupees.
3. `train_model()` fits a straight-line relationship between size and price.
4. `predict_price()` formats a single size in the shape scikit-learn expects
   and returns its predicted price.
