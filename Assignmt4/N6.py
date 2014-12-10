# -*- coding: utf-8 -*-
def factorial(N):
    if N == 1:           # 종결 조건
        return 1         # 종결 조건이 만족할 때의 반환 값
    return N * factorial(N-1)  # 재귀 호출

print factorial(4)
