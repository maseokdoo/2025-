student_info = [[1] * 9 for i in range(5)]

#입력 함수
def stu_info_input() :
    for i in range(5) :
        print("\n")
        print(f"{i+1}번째 학생 정보를 입력하세요.\n")
        student_info[i][0] = int(input("학번: "))
        student_info[i][1] = input("이름: ")
        student_info[i][2] = int(input("영어:"))
        student_info[i][3] = int(input("C-언어:"))
        student_info[i][4] = int(input("파이썬: "))

#총점/평균 계산 함수
def total_avg_calculate() :
    for h in range(5) :
        student_info[h][5] = student_info[h][2] + student_info[h][3] + student_info[h][4]
        student_info[h][6] = student_info[h][5] / 3

#학점계산 함수
def grade_calculate() :
    for j in range(5) :
        if student_info[j][6] >= 95:
            student_info[j][7] = 'A+'
        elif student_info[j][6] >= 90:
            student_info[j][7] = 'A'
        elif student_info[j][6] >= 85:
            student_info[j][7] = 'B+' 
        elif student_info[j][6] >= 80:
            student_info[j][7] = 'B'
        elif student_info[j][6] >= 75:
            student_info[j][7] = 'C+'
        elif student_info[j][6] >= 70:
            student_info[j][7] = 'C'
        elif student_info[j][6] >= 60:
            student_info[j][7] = 'D'
        else:
            student_info[j][7] = 'F'

#등수계산 함수
def rank_calculate() :
    for k in range(5) :
        for l in range(5) :
            if student_info[k][5] < student_info[l][5] :
                student_info[k][8] += 1 

#출력 함수
def print_student_info() :
    print("\n성적관리 프로그램")
    print("="*88)
    print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
    print("="*88)
    for m in range(5) :
        print(f"{student_info[m][0]:<12}{student_info[m][1]:<9}{student_info[m][2]:<10}{student_info[m][3]:<10}{student_info[m][4]:<10}{student_info[m][5]:<10}{student_info[m][6]:<10.1f}{student_info[m][7]:<10}{student_info[m][8]:<10}")

stu_info_input()
total_avg_calculate()
grade_calculate()
rank_calculate()
print_student_info()


