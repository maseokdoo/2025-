# -*- coding: utf-8 -*-

# 입력 함수
def stu_info_input():
    for i in range(stu_num):
        print(f"\n{i+1}번째 학생 정보를 입력하세요.\n")
        student_info[i] = [0] * 9  # 각 학생 정보 초기화
        student_info[i][0] = int(input("학번: "))
        student_info[i][1] = input("이름: ")
        student_info[i][2] = int(input("영어: "))
        student_info[i][3] = int(input("C-언어: "))
        student_info[i][4] = int(input("파이썬: "))

# 총점/평균 계산 함수
def total_avg_calculate():
    for h in range(len(student_info)):
        student_info[h][5] = student_info[h][2] + student_info[h][3] + student_info[h][4]
        student_info[h][6] = student_info[h][5] / 3

# 학점 계산 함수
def grade_calculate():
    for j in range(len(student_info)):
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

# 등수 계산 함수
def rank_calculate():
    for i in range(len(student_info)):
        student_info[i][8] = 1  # 등수를 1로 초기화
    for k in range(len(student_info)):
        for l in range(len(student_info)):
            if student_info[k][5] < student_info[l][5]:
                student_info[k][8] += 1

# 출력 함수
def print_student_info():
    print("\n성적관리 프로그램")
    print("=" * 88)
    print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
    print("=" * 88)
    for m in range(len(student_info)):
        print(f"{student_info[m][0]:<12}{student_info[m][1]:<9}{student_info[m][2]:<10}{student_info[m][3]:<10}{student_info[m][4]:<10}{student_info[m][5]:<10}{student_info[m][6]:<10.1f}{student_info[m][7]:<10}{student_info[m][8]:<10}")
    count_80more()

# 탐색 함수
def search_stu():
    print("찾고자 하는 학생의 이름과 학번을 입력하세요.")
    tmp_name = input("이름 : ")
    tmp_hakbun = int(input("학번 : "))
    for c1 in range(len(student_info)):
        if tmp_name == student_info[c1][1] and tmp_hakbun == student_info[c1][0]:
            print("=" * 88)
            print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
            print("=" * 88)
            print(f"{student_info[c1][0]:<12}{student_info[c1][1]:<9}{student_info[c1][2]:<10}{student_info[c1][3]:<10}{student_info[c1][4]:<10}{student_info[c1][5]:<10}{student_info[c1][6]:<10.1f}{student_info[c1][7]:<10}{student_info[c1][8]:<10}")
            return
    print("찾고자 하는 학생의 정보가 없습니다.")

# 정렬(총점) 함수
def SortTotalScore():
    student_info.sort(key=lambda x: -x[5])

# 80점 이상 학생 수 카운트 함수
def count_80more():
    tmp_80more = 0
    for c2 in range(len(student_info)):
        if student_info[c2][6] > 80:
            tmp_80more += 1
    if tmp_80more == 0:
        print("80점이상인 학생이 없습니다.")
    else:
        print(f"80점이상 학생 수 : {tmp_80more}")

# 삭제 함수
def delete_stu_info():
    if len(student_info) == 0:
        print("삭제할 학생 정보가 없습니다.")
        return
    print("삭제하고자 하는 학생의 이름과 학번을 입력하세요.")
    del_name = input("이름 : ")
    del_hakbun = int(input("학번 : "))
    for c3 in range(len(student_info)):
        if del_name == student_info[c3][1] and del_hakbun == student_info[c3][0]:
            del student_info[c3]
            return
    print("삭제하고자 하는 학생의 정보가 없습니다.")

# 삽입 함수
def insert_stu():
    MAX_STUDENTS = 5  # 최대 학생 수 제한
    if len(student_info) >= MAX_STUDENTS:
        print(f"최대 {MAX_STUDENTS}명까지 입력 가능합니다. 더 이상 학생을 추가할 수 없습니다.")
        return
    print("새롭게 삽입하고자 하는 학생의 정보를 입력하세요.")
    tmp_hakbun = int(input("학번: "))
    tmp_name = input("이름: ")
    tmp_eng = int(input("영어: "))
    tmp_clang = int(input("C-언어: "))
    tmp_py = int(input("파이썬: "))
    tmp_total = tmp_eng + tmp_clang + tmp_py
    tmp_avg = tmp_total / 3
    if tmp_avg >= 95:
        tmp_grade = 'A+'
    elif tmp_avg >= 90:
        tmp_grade = 'A'
    elif tmp_avg >= 85:
        tmp_grade = 'B+'
    elif tmp_avg >= 80:
        tmp_grade = 'B'
    elif tmp_avg >= 75:
        tmp_grade = 'C+'
    elif tmp_avg >= 70:
        tmp_grade = 'C'
    elif tmp_avg >= 60:
        tmp_grade = 'D'
    else:
        tmp_grade = 'F'
    student_info.append([tmp_hakbun, tmp_name, tmp_eng, tmp_clang, tmp_py, tmp_total, tmp_avg, tmp_grade, 1])

# 초기 설정
student_info = []  # 동적 리스트
stu_num = 0
insert_check = 0

while True:
    print("성적관리프로그램에 오신걸 환영합니다.")
    print("===== 메뉴 =====")
    print("1. 학생 정보 입력")
    print("2. 전체 학생 정보 보기")
    print("3. 학생 정보 검색")
    print("4. 학생 정보 삽입")
    print("5. 학생 정보 삭제")
    print("6. 프로그램 종료")
    print("\n")
    menu_check = int(input("원하는 메뉴를 입력하세요 : "))

    if menu_check == 1:
        stu_num = int(input("입력할 학생 수를 입력하세요 (최대 5명): "))
        if stu_num > 5:
            print("최대 5명까지 입력 가능합니다. 다시 시도해주세요.")
            continue
        insert_check += 1
        student_info = [[] for _ in range(stu_num)]  # 리스트 초기화
        stu_info_input()
        total_avg_calculate()
        grade_calculate()
        rank_calculate()
    elif menu_check == 2:
        if insert_check != 0 and len(student_info) != 0:
            SortTotalScore()
            rank_calculate()  # 출력 전 등수 재계산
            print_student_info()
        else:
            print("학생의 정보를 먼저 입력해주세요.")
    elif menu_check == 3:
        if insert_check != 0 and len(student_info) != 0:
            rank_calculate()
            search_stu()
        else:
            print("학생의 정보를 먼저 입력해주세요.")
    elif menu_check == 4:
        if insert_check != 0:
            insert_stu()
            total_avg_calculate()
            grade_calculate()
            rank_calculate()  # 삽입 후 등수 재계산
        else:
            print("학생의 정보를 먼저 입력해주세요.")
    elif menu_check == 5:
        if insert_check != 0:
            delete_stu_info()
            if len(student_info) > 0:  # 삭제 후 학생이 남아있을 때만 계산
                total_avg_calculate()
                grade_calculate()
                rank_calculate()  # 삭제 후 등수 재계산
        else:
            print("학생의 정보를 먼저 입력해주세요.")
    elif menu_check == 6:
        exit()