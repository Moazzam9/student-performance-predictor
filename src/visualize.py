import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("data/students.csv")


data.columns = data.columns.str.strip()


sns.scatterplot(x=data["hours_study"], y=data["final_score"])
plt.title("Study Hours vs Final Score")
plt.xlabel("Hours of Study")
plt.ylabel("Final Score")
plt.show()