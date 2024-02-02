import marimo

__generated_with = "0.1.88"
app = marimo.App()


@app.cell
def __():
    # Marimo
    import marimo as mo
    # Data Handling
    import numpy as np
    import pandas as pd
    # Data Visualisation
    import matplotlib.pyplot as plt
    # Machine Learning
    from sklearn.model_selection import train_test_split as tts
    import xgboost as xgb
    # Tools
    #from tools import ...
    return mo, np, pd, plt, tts, xgb


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
