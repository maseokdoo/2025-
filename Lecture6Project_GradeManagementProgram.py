# -*- coding: utf-8 -*-

##################

#프로그램 : 성적관리프로그램

#작성자 : 소프트웨어학부/유현석

#작성일 : 2025/04/11

#프로그램 설명 : 3개의 과목에 대해 n명의 학생의 점수를 관리하는 프로그램

###################

#{'총점':<8}{'평균':<8}{'학점':<8}{'등수':
class stu_list:
    def __init__(self):
        self.hakbun = 0
        self.name = 0
        self.eng_score = 0
        self.Clang_score = 0
        self.py_score = 0
        self.total = 0
        self.avg = 0
        self.hakjum = 0
        self.rank = 0
        
        

# -*- coding: utf-8 -*-

# 입력 함수
def stu_info_input():
    for i in range(stu_num):
        print(f"\n{i+1}번째 학생 정보를 입력하세요.\n")
        student_info[i].hakbun = int(input("학번: "))
        student_info[i].name = input("이름: ")
        student_info[i].eng_score = int(input("영어: "))
        student_info[i].Clang_score = int(input("C-언어: "))
        student_info[i].py_score = int(input("파이썬: "))

# 총점/평균 계산 함수
def total_avg_calculate():
    for h in range(len(student_info)):
        student_info[h].total = student_info[h].eng_score + student_info[h].Clang_score + student_info[h].py_score
        student_info[h].avg = student_info[h].total / 3

# 학점 계산 함수
def grade_calculate():
    for j in range(len(student_info)):
        if student_info[j].avg >= 95:
            student_info[j].hakjum = 'A+'
        elif student_info[j].avg >= 90:
            student_info[j].hakjum = 'A'
        elif student_info[j].avg >= 85:
            student_info[j].hakjum = 'B+'
        elif student_info[j].avg >= 80:
            student_info[j].hakjum = 'B'
        elif student_info[j].avg >= 75:
            student_info[j].hakjum = 'C+'
        elif student_info[j].avg >= 70:
            student_info[j].hakjum = 'C'
        elif student_info[j].avg >= 60:
            student_info[j].hakjum = 'D'
        else:
            student_info[j].hakjum = 'F'

# 등수 계산 함수
def rank_calculate():
    for i in range(len(student_info)):
        student_info[i].rank = 1  # 등수를 1로 초기화
    for k in range(len(student_info)):
        for l in range(len(student_info)):
            if student_info[k].total < student_info[l].total:
                student_info[k].rank += 1

# 출력 함수
def print_student_info():
    print("\n성적관리 프로그램")
    print("=" * 88)
    print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
    print("=" * 88)
    for m in range(len(student_info)):
        print(f"{student_info[m].hakbun:<12}{student_info[m].name:<9}{student_info[m].eng_score:<10}{student_info[m].Clang_score:<10}{student_info[m].py_score:<10}{student_info[m].total:<10}{student_info[m].avg:<10.1f}{student_info[m].hakjum:<10}{student_info[m].rank:<10}")
    count_80more()

# 탐색 함수
def search_stu():
    print("찾고자 하는 학생의 이름과 학번을 입력하세요.")
    tmp_name = input("이름 : ")
    tmp_hakbun = int(input("학번 : "))
    for c1 in range(len(student_info)):
        if tmp_name == student_info[c1].name and tmp_hakbun == student_info[c1].hakbun:
            print("=" * 88)
            print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
            print("=" * 88)
            print(f"{student_info[c1].hakbun:<12}{student_info[c1].name:<9}{student_info[c1].eng_score:<10}{student_info[c1].Clang_score:<10}{student_info[c1].py_score:<10}{student_info[c1].total:<10}{student_info[c1].avg:<10.1f}{student_info[c1].hakjum:<10}{student_info[c1].rank:<10}")
            return
    print("찾고자 하는 학생의 정보가 없습니다.")

# 정렬(총점) 함수
def SortTotalScore():
    student_info.sort(key=lambda stu_list: stu_list.total, reverse=True)

# 80점 이상 학생 수 카운트 함수
def count_80more():
    tmp_80more = 0
    for c2 in range(len(student_info)):
        if student_info[c2].avg > 80:
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
        if del_name == student_info[c3].name and del_hakbun == student_info[c3].hakbun:
            del student_info[c3]
            return
    print("삭제하고자 하는 학생의 정보가 없습니다.")

# 삽입 함수
def insert_stu():
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
    student_info.append(0)
    student_info[len(student_info)-1] = stu_list()
    student_info[len(student_info)-1].hakbun = tmp_hakbun
    student_info[len(student_info)-1].name = tmp_name
    student_info[len(student_info)-1].eng_score = tmp_eng
    student_info[len(student_info)-1].Clang_score = tmp_clang
    student_info[len(student_info)-1].py_score = tmp_py
    student_info[len(student_info)-1].total = tmp_total
    student_info[len(student_info)-1].avg = tmp_avg
    student_info[len(student_info)-1].hakjum = tmp_grade
    student_info[len(student_info)-1].rank = 1


# 초기 설정
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
        stu_num = int(input("입력할 학생 수를 입력하세요"))
        global student_info
        student_info = [0 for _ in range(stu_num)]
        for i in range(stu_num):
            student_info[i] = stu_list()
        insert_check += 1
        stu_info_input()
        total_avg_calculate()
        grade_calculate()
        rank_calculate()
        SortTotalScore()
    elif menu_check == 2:
        if insert_check != 0 and len(student_info) != 0:
            rank_calculate()  # 출력 전 등수 재계산
            SortTotalScore()
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
            SortTotalScore()
        else:
            print("학생의 정보를 먼저 입력해주세요.")
    elif menu_check == 5:
        if insert_check != 0:
            delete_stu_info()
            if len(student_info) > 0:  # 삭제 후 학생이 남아있을 때만 계산
                total_avg_calculate()
                grade_calculate()
                rank_calculate()  # 삭제 후 등수 재계산
                SortTotalScore()
        else:
            print("학생의 정보를 먼저 입력해주세요.")
    elif menu_check == 6:
        exit()