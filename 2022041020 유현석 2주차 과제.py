num_students = 5
num_subjects = 3

students = []

for i in range(num_students):
    name = input(f"{i+1}번째 학생 이름: ")
    scores = []

    while len(scores) < num_subjects:
        try:
            input_scores = list(map(int, input(f"{name}의 {num_subjects}과목 점수 입력 (공백으로 구분): ").split()))
            if any(score < 0 or score > 100 for score in input_scores):
                print("잘못된 점수입니다. 0~100 사이의 값을 입력하세요.")
                continue
            if len(input_scores) != num_subjects:
                print(f"{num_subjects}개의 점수를 입력해야 합니다.")
                continue
            scores = input_scores
        except ValueError:
            print("숫자로 된 점수를 정확히 입력하세요.")

    total = sum(scores)
    avg = total / num_subjects
    

    if avg >= 95:
        grade = 'A+'
    elif avg >= 90:
        grade = 'A'
    elif avg >= 85:
        grade = 'B+' 
    elif avg >= 80:
        grade = 'B'
    elif avg >= 75:
        grade = 'C+'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    students.append({"name": name, "scores": scores, "total": total, "avg": avg, "grade": grade, "rank": 1})


for i in range(num_students):
    for j in range(num_students):
        if students[i]["total"] < students[j]["total"]:
            students[i]["rank"] += 1


print("\n학생 성적표")
print("="*50)
print(f"{'이름':<6}{'총점':<5}{'평균':<5}{'학점':<4}{'등수':<4}")
print("="*50)

for s in students:
    print(f"{s['name']:<8}{s['total']:<6}{s['avg']:<8.2f}{s['grade']:<4}{s['rank']:<4}")
