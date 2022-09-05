# tkinter를 사용하기 위한 import
from tkinter import *
from tkinter import ttk
import tkinter.simpledialog

login = False

# 로그인 여부
while not login:
    result = tkinter.simpledialog.askstring(" ", "로그인하시겠습니까?")
    # 로그인 여부 묻기에 yes 시 다음 창으로 넘어감
    if result == 'yes':
        login = True
    # 로그인 여부 묻기에 no 시 Bye 뜨고 종료
    elif result == 'no':
        tkinter.messagebox.showinfo(" ", "Bye")
        break
    # 로그인 여부 묻기에서 커서로 X를 누르거나 Cancel을 누르면 Bye 뜨고 종료
    elif result is None:
        break
    # 로그인 여부 묻기에서 yes 또는 no를 입력하지않을시 경고문
    else:
        tkinter.messagebox.showwarning("경고", "yes no 로만 대답하세요")

if login:
    # tkinter 객체 생성
    window = Tk()

    w = 280
    h = 170

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # 사용자 id와 password를 저장하는 변수 생성
    user_id, password1, password2 = StringVar(), StringVar(), StringVar()

    lines = open("idpass.txt", "r").read().splitlines()

    # dictionary (딕셔너리 : 사전 ) 생성
    id_pass_list = {}

    for line_number in range(0, len(lines), 3):
        # lines 리스트의 0번째 , 3번째 , 6번째 ~ lines 안에 id 들
        id = lines[line_number]
        # lines 리스트의 1, 4, 7, 10 번째 리스트에 저장값 - 1차 비번
        pass1 = lines[line_number + 1]
        # lines 리스트의 2, 5, 8, 11 번째 리스트에 저장값 - 2차 비번
        pass2 = lines[line_number + 2]

        # 위에서 따온 각각의 아이디와 비번들을 사전에 저장.
        # 이미 존재하는 아이디면 덮어씌워진다, 하지만 회원가입에서 그런 상황이 발생하지 않게 방지한다
        id_pass_list[id] = pass1, pass2


    def pressEnter(event):
        check_data()


    # 사용자 id와 password를 비교하는 함수
    def check_data():
        # 사용자가 입력한 아이디가 사전에 있을 경우 check 에 ( 1차 비번, 2차 비번 ) 저장
        # 사용자가 입력한 아이디가 사전에 없을 경우 check 에 None 저장
        check = id_pass_list.get(user_id.get())

        # 존재하는 아이디일 경우 check에 ( 1차 비번, 2차 비번 ) 이 할당됨
        # 고로 아이디가 존재할 경우 check 는 None 이 아니게된다.
        if check is not None:

            # 사용자가 입력한 값과 저장되어있는 값이 일치 한지 비교
            if check[0] == password1.get() and check[1] == password2.get():
                print("Login 성공")
            else:
                print("1차 혹은 2차 비밀번호가 틀렸습니다.")

        # 존재하지 않는 아이디일 경우 check에 ( 1차 비번 , 2차 비번 )이 활당되지 않음
        # 아이디가 존재하지 않을 경우 check 는 None 이 된다.
        elif check is None:
            print("존재하지않는 아이디 입니다.")

        else:
            print("check_data 오류")


    def sign_up():
        print("sign-up 작업중")


    # id와 password, 그리고 확인 버튼의 UI를 만드는 부분
    ttk.Label(window, text="ID        : ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Label(window, text="Password1 : ").grid(row=1, column=0, padx=10, pady=10)
    ttk.Label(window, text="Password2 : ").grid(row=2, column=0, padx=10, pady=10)
    ttk.Entry(window, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)
    ttk.Entry(window, textvariable=password1).grid(row=1, column=1, padx=10, pady=10)
    ttk.Entry(window, textvariable=password2).grid(row=2, column=1, padx=10, pady=10)
    ttk.Button(window, text="Login", command=check_data).grid(row=3, column=1, padx=10, pady=10)
    ttk.Button(window, text="Sign-Up", command=sign_up).grid(row=3, column=0, padx=10, pady=10)

    window.bind('<Return>', pressEnter)
    window.title("로그인 창")
    window.mainloop()
