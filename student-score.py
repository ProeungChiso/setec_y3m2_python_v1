name = input("Enter your name: ")

subjects = [
    "Math", 
    "Physics", 
    "History", 
    "Khmer"
]

scores = {}

for subject in subjects:
    score = float(input(f"Enter your {subject.lower()} score: "))
    scores[subject] = score

total_score = sum(scores.values())
average_score = total_score / len(subjects)

print(f"Student Name: {name}")
print(f"Total Score: {total_score:.2f}")
print(f"Average Score: {average_score:.2f}")