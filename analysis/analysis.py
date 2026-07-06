import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    return df

def process(df):
    df["total"] = df[["math","science","english"]].sum(axis=1)
    df["avg"] = df["total"] / 3

    def grade(x):
        if x >= 90: return "A+"
        elif x >= 75: return "A"
        elif x >= 60: return "B"
        elif x >= 40: return "C"
        else: return "Fail"

    df["grade"] = df["avg"].apply(grade)
    return df

def class_summary(df):
    return df.groupby("class")[["math","science","english","total"]].mean()