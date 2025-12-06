"""
utils.py
Helper functions.
"""
import matplotlib.pyplot as plt
import seaborn as sns

def plot_pred_vs_actual(y_true, y_pred, title="Pred vs Actual"):
    import pandas as pd
    df = pd.DataFrame({'true': y_true, 'pred': y_pred})
    plt.figure(figsize=(8,4))
    sns.lineplot(data=df)
    plt.title(title)
    plt.show()