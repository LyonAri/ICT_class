# 08_tk_dict01A.py 에서 파일 읽어와서 단어의 뜻을 확인하기
from tkinter import *
import pandas as pd
import os
global dat

print(os.getcwd())  # 현재 작업 디렉터리를 확인
path = 'C:\\Users\\user\\Documents\\test\\test'
os.chdir(path)      # 현재 작업 디렉터리를 변경하겠다.
print(os.getcwd())  

# D:\Github\CLASS_PY_LIB_LEVELUP_code\06_class_PY_LIB_code

#%%
dat = pd.read_excel("./vocafruit.xlsx")
print(dat.shape, dat)

def click():
    word=entry.get()
    output.delete(0.0, END)

    try:
        def_word=dat.loc[ dat['word']==word , 'def' ].values[0]
    except:
        def_word='단어의 뜻을 찾을 수 없습니다.'

    output.insert(END, def_word)

# 메인 :
window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이블 
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="#FCE4EC")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
btn = Button(window, text="제출", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

# 04 설명 레이블
lable2 = Label(window, text="\n의미:")
lable2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="#F3E5F5")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()