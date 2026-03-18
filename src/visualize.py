import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data/students.csv")
data.columns = data.columns.str.strip()


sns.set(style="whitegrid")


plt.figure(figsize=(8, 5))
sns.scatterplot(x=data["hours_study"], y=data["final_score"], s=100, color="dodgerblue")
plt.title("Study Hours vs Final Score", fontsize=14)
plt.xlabel("Hours of Study", fontsize=12)
plt.ylabel("Final Score", fontsize=12)
plt.tight_layout()
plt.show()


sns.pairplot(data, vars=["hours_study", "sleep_hours", "attendance",
                         "previous_score", "extracurricular",
                         "class_participation", "stress_level"],
             hue="final_score", palette="viridis")
plt.suptitle("Feature Correlations with Final Score", fontsize=16, y=1.02)
plt.show()