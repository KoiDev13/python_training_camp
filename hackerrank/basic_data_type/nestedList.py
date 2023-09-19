if __name__ == '__main__':
    names = []
    scores = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    for student in zip(names, scores):
        students.append(student)
    students1 = sorted(students, key=lambda x: (x[1], x[0]))
    unique_scores = set(scores)
    second_lowest_score = sorted(unique_scores)[1]
    # print(students1)
    for student in students1:
        if student[1] == second_lowest_score:
            print(student[0])