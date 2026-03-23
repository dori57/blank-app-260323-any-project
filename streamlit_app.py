import streamlit as st
import random

# 문제 생성 함수들
def generate_addition_problems(n):
    problems = []
    ranges = [
        (1, 9),
        (10, 99),
        (100, 999),
        (1000, 9999)
    ]
    for _ in range(n):
        range_a, range_b = random.choice(ranges)
        a = random.randint(range_a, range_b)
        b = random.randint(range_a, range_b)
        problem = f"{a} + {b} = ?"
        answer = a + b
        problems.append((problem, answer))
    return problems

def generate_subtraction_problems(n):
    problems = []
    ranges = [
        (1, 9),
        (10, 99),
        (100, 999),
        (1000, 9999)
    ]
    for _ in range(n):
        range_a, range_b = random.choice(ranges)
        a = random.randint(range_a, range_b)
        b = random.randint(range_a, range_b)
        if a < b:
            a, b = b, a
        problem = f"{a} - {b} = ?"
        answer = a - b
        problems.append((problem, answer))
    return problems

def generate_multiplication_problems(n):
    problems = []
    ranges = [
        ((1, 9), (1, 9)),
        ((10, 99), (1, 9)),
        ((10, 99), (10, 99)),
        ((100, 999), (1, 9)),
    ]
    for _ in range(n):
        (range_a_min, range_a_max), (range_b_min, range_b_max) = random.choice(ranges)
        a = random.randint(range_a_min, range_a_max)
        b = random.randint(range_b_min, range_b_max)
        problem = f"{a} × {b} = ?"
        answer = a * b
        problems.append((problem, answer))
    return problems

def generate_division_problems(n):
    problems = []
    ranges = [
        ((1, 9), (1, 10)),
        ((10, 99), (2, 10)),
        ((100, 999), (2, 10)),
        ((10, 99), (10, 99)),
    ]
    for _ in range(n):
        (range_b_min, range_b_max), (range_c_min, range_c_max) = random.choice(ranges)
        b = random.randint(range_b_min, range_b_max)
        c = random.randint(range_c_min, range_c_max)
        a = b * c
        problem = f"{a} ÷ {b} = ?"
        answer = c
        problems.append((problem, answer))
    return problems

st.title("🧮 기본 연산 연습 프로젝트")

# 사이드바 메뉴
st.sidebar.title("프로젝트 메뉴")
menu = st.sidebar.radio(
    "폴더 선택:",
    ("소개", "기본연산")
)

if menu == "소개":
    st.header("프로젝트 소개")
    st.write("""
    이 프로젝트는 어린이들이나 초보자들이 덧셈, 뺄셈, 곱셈, 나눗셈과 같은 기본적인 수학 연산을 재미있게 연습할 수 있도록 설계되었습니다.

    ## 프로젝트 목표
    - 기본적인 수학 연산 능력 향상
    - 문제 해결 능력 개발
    - 재미있는 학습 경험 제공

    ## 포함된 연산
    - **덧셈**: 자연수 덧셈 문제 연습
    - **뺄셈**: 자연수 뺄셈 문제 연습
    - **곱셈**: 자연수 곱셈 문제 연습
    - **나눗셈**: 자연수 나눗셈 문제 연습

    각 연산별로 다양한 난이도의 문제를 제공하며, 정답 확인 기능이 포함되어 있습니다.

    ## 시작하기
    왼쪽 사이드바의 '기본연산' 메뉴에서 원하는 연산을 선택하여 연습을 시작하세요!

    **Streamlit**을 사용하여 웹 기반으로 쉽게 접근할 수 있습니다.
    """)

elif menu == "기본연산":
    st.sidebar.subheader("연산 선택")
    operation = st.sidebar.radio(
        "연습할 연산을 선택하세요:",
        ("덧셈", "뺄셈", "곱셈", "나눗셈")
    )

    if operation == "덧셈":
        st.header("덧셈 연습")
        if st.button("새 문제 생성"):
            problems = generate_addition_problems(5)
            for i, (problem, answer) in enumerate(problems, 1):
                st.write(f"**문제 {i}:** {problem}")
                if st.button(f"답 보기 {i}", key=f"add_{i}"):
                    st.write(f"답: {answer}")
    elif operation == "뺄셈":
        st.header("뺄셈 연습")
        if st.button("새 문제 생성"):
            problems = generate_subtraction_problems(5)
            for i, (problem, answer) in enumerate(problems, 1):
                st.write(f"**문제 {i}:** {problem}")
                if st.button(f"답 보기 {i}", key=f"sub_{i}"):
                    st.write(f"답: {answer}")
    elif operation == "곱셈":
        st.header("곱셈 연습")
        if st.button("새 문제 생성"):
            problems = generate_multiplication_problems(5)
            for i, (problem, answer) in enumerate(problems, 1):
                st.write(f"**문제 {i}:** {problem}")
                if st.button(f"답 보기 {i}", key=f"mul_{i}"):
                    st.write(f"답: {answer}")
    elif operation == "나눗셈":
        st.header("나눗셈 연습")
        if st.button("새 문제 생성"):
            problems = generate_division_problems(5)
            for i, (problem, answer) in enumerate(problems, 1):
                st.write(f"**문제 {i}:** {problem}")
                if st.button(f"답 보기 {i}", key=f"div_{i}"):
                    st.write(f"답: {answer}")
