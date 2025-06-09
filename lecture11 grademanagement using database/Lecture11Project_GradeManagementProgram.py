# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import sys

##################

#프로그램 : 성적관리프로그램(데이터베이스 기반)

#작성자 : 소프트웨어학부/유현석

#작성일 : 2025/06/09

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

def get_db_connection():
    """데이터베이스 연결을 생성하고 반환하는 함수"""
    try:
        conn = sqlite3.connect('grade_management.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"데이터베이스 연결 오류: {e}")
        sys.exit(1)

def init_db():
    """데이터베이스와 테이블을 초기화하는 함수"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            hakbun INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            eng_score INTEGER CHECK (eng_score >= 0 AND eng_score <= 100),
            clang_score INTEGER CHECK (clang_score >= 0 AND clang_score <= 100),
            py_score INTEGER CHECK (py_score >= 0 AND py_score <= 100),
            total INTEGER,
            avg REAL,
            hakjum TEXT,
            rank INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"데이터베이스 초기화 오류: {e}")
        sys.exit(1)
    finally:
        conn.close()

def validate_score(score):
    """점수의 유효성을 검사하는 함수"""
    try:
        score = int(score)
        if 0 <= score <= 100:
            return score
        raise ValueError("점수는 0에서 100 사이여야 합니다.")
    except ValueError as e:
        print(f"잘못된 점수 입력: {e}")
        return None

def calculate_total_avg(eng_score, clang_score, py_score):
    """총점과 평균을 계산하는 함수"""
    total = eng_score + clang_score + py_score
    avg = total / 3
    return total, avg

def calculate_grade(avg):
    """평균 점수에 따른 학점을 계산하는 함수"""
    if avg >= 95:
        return 'A+'
    elif avg >= 90:
        return 'A'
    elif avg >= 85:
        return 'B+'
    elif avg >= 80:
        return 'B'
    elif avg >= 75:
        return 'C+'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def update_ranks():
    """학생들의 등수를 업데이트하는 함수"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        UPDATE students
        SET rank = (
            SELECT COUNT(*) + 1
            FROM students s2
            WHERE s2.total > students.total
        )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"등수 계산 오류: {e}")
        conn.rollback()
    finally:
        conn.close()

def sort_by_total():
    """총점 기준으로 학생들을 정렬하는 함수"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM students ORDER BY total DESC')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"정렬 오류: {e}")
        return []
    finally:
        conn.close()

def count_students_above_80():
    """80점 이상인 학생 수를 계산하는 함수"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT COUNT(*) FROM students WHERE avg > 80')
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"카운트 오류: {e}")
        return 0
    finally:
        conn.close()

def search_student(hakbun, name):
    """학번과 이름으로 학생을 검색하는 함수
    
    Args:
        hakbun (int): 검색할 학번
        name (str): 검색할 이름
        
    Returns:
        list: 검색된 학생 정보 리스트
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM students WHERE hakbun = ? AND name = ?', (hakbun, name))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"검색 오류: {e}")
        return []
    finally:
        conn.close()

def print_search_results(students):
    """검색 결과를 출력하는 함수
    
    Args:
        students (list): 검색된 학생 정보 리스트
    """
    if not students:
        print("검색 결과가 없습니다.")
        return
        
    print("\n검색 결과:")
    print("=" * 88)
    print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
    print("=" * 88)
    
    for student in students:
        print_student_info(student)

def insert_student(hakbun, name, eng_score, clang_score, py_score):
    """새로운 학생 정보를 추가하는 함수"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        total, avg = calculate_total_avg(eng_score, clang_score, py_score)
        hakjum = calculate_grade(avg)
        
        cursor.execute('''
        INSERT INTO students (hakbun, name, eng_score, clang_score, py_score, total, avg, hakjum)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (hakbun, name, eng_score, clang_score, py_score, total, avg, hakjum))
        
        conn.commit()
        update_ranks()
        return True
    except sqlite3.Error as e:
        print(f"삽입 오류: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_student(hakbun, name):
    """학생 정보를 삭제하는 함수"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM students WHERE hakbun = ? AND name = ?', (hakbun, name))
        if cursor.rowcount > 0:
            conn.commit()
            update_ranks()
            return True
        return False
    except sqlite3.Error as e:
        print(f"삭제 오류: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def print_student_info(student):
    """학생 정보를 출력하는 함수"""
    print(f"{student['hakbun']:<12}{student['name']:<9}{student['eng_score']:<10}{student['clang_score']:<10}{student['py_score']:<10}{student['total']:<10}{student['avg']:<10.1f}{student['hakjum']:<10}{student['rank']:<10}")

def print_all_students():
    """모든 학생 정보를 출력하는 함수"""
    students = sort_by_total()
    
    print("\n성적관리 프로그램")
    print("=" * 88)
    print(f"{'학번':<11}{'이름':<8}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<8}{'등수':<8}")
    print("=" * 88)
    
    for student in students:
        print_student_info(student)
    
    count = count_students_above_80()
    if count == 0:
        print("80점이상인 학생이 없습니다.")
    else:
        print(f"80점이상 학생 수 : {count}")

def input_student_info():
    """학생 정보를 입력받는 함수"""
    try:
        stu_num = int(input("입력할 학생 수를 입력하세요: "))
        if stu_num <= 0:
            print("학생 수는 1명 이상이어야 합니다.")
            return
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        return

    for i in range(stu_num):
        print(f"\n{i+1}번째 학생 정보를 입력하세요.\n")
        try:
            hakbun = int(input("학번: "))
            name = input("이름: ")
            eng_score = validate_score(input("영어: "))
            clang_score = validate_score(input("C-언어: "))
            py_score = validate_score(input("파이썬: "))
            
            if None in (eng_score, clang_score, py_score):
                print("입력을 취소합니다.")
                return
            
            if insert_student(hakbun, name, eng_score, clang_score, py_score):
                print("학생 정보가 성공적으로 입력되었습니다.")
            else:
                print("학생 정보 입력에 실패했습니다.")
                
        except ValueError as e:
            print(f"입력 오류: {e}")
            continue

def main():
    """메인 프로그램"""
    init_db()
    
    while True:
        print("\n성적관리프로그램에 오신걸 환영합니다.")
        print("===== 메뉴 =====")
        print("1. 학생 정보 입력")
        print("2. 전체 학생 정보 보기")
        print("3. 학생 정보 검색")
        print("4. 학생 정보 삽입")
        print("5. 학생 정보 삭제")
        print("6. 프로그램 종료")
        print("\n")
        
        try:
            menu_check = int(input("원하는 메뉴를 입력하세요 : "))
            
            if menu_check == 1:
                input_student_info()
            elif menu_check == 2:
                print_all_students()
            elif menu_check == 3:
                try:
                    hakbun = int(input("학번을 입력하세요: "))
                    name = input("이름을 입력하세요: ")
                    students = search_student(hakbun, name)
                    print_search_results(students)
                except ValueError:
                    print("올바른 학번을 입력해주세요.")
            elif menu_check == 4:
                print("새로운 학생 정보를 입력하세요.")
                try:
                    hakbun = int(input("학번: "))
                    name = input("이름: ")
                    eng_score = validate_score(input("영어: "))
                    clang_score = validate_score(input("C-언어: "))
                    py_score = validate_score(input("파이썬: "))
                    
                    if None in (eng_score, clang_score, py_score):
                        print("입력을 취소합니다.")
                        continue
                    
                    if insert_student(hakbun, name, eng_score, clang_score, py_score):
                        print("학생 정보가 성공적으로 입력되었습니다.")
                    else:
                        print("학생 정보 입력에 실패했습니다.")
                except ValueError as e:
                    print(f"입력 오류: {e}")
            elif menu_check == 5:
                print("삭제할 학생의 정보를 입력하세요.")
                try:
                    hakbun = int(input("학번: "))
                    name = input("이름: ")
                    
                    if delete_student(hakbun, name):
                        print("학생 정보가 성공적으로 삭제되었습니다.")
                    else:
                        print("해당 학생을 찾을 수 없습니다.")
                except ValueError as e:
                    print(f"입력 오류: {e}")
            elif menu_check == 6:
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 메뉴를 선택했습니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()