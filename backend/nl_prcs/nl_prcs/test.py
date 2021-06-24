import sys
from konlpy.tag import Kkma
from icecream import ic
kkma = Kkma()
ic(kkma.pos('한국어 분석을 시작합니다 재미있어요~~'))