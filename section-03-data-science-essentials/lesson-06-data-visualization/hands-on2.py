import matplotlib.pyplot as plt


# Scatter Plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]
plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Study hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()
