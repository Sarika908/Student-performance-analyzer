import matplotlib.pyplot as plt

def plot_marks(df):
    plt.figure()
    plt.bar(df["name"], df["total"])
    plt.title("Student Total Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()

def plot_grades(df):
    plt.figure()
    df["grade"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Grade Distribution")
    plt.ylabel("")
    plt.show()

def plot_subjects(df):
    plt.figure()
    df[["math","science","english"]].mean().plot(kind="bar")
    plt.title("Subject Average")
    plt.ylabel("Marks")
    plt.show()