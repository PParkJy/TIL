'''
i_ls = 0, 4 일때의 Zc 입력받아 *.proto 파일 생성하는게 목적
나중에 C로 다시 구현해야할 것 같음

5G 표준 문서 기준 rows(i), cols(j)
-> base graph 1 : 46, 68
-> base graph 2 : 42, 52
-> shift value 계산 : mod(V_ij, Zc)
                    : 인덱스가 주어진 곳 즉, V_ij가 주어진 곳의 proto matrix 값은 1, 나머지는 0
                    : 0인 곳의 shit value는 -1로 작성

input = base graph의 종류, i_ls, Zc
output = 5G_BG(num)_iLS(num)_Zc(num).proto 이름으로 바로 알아볼 수 있게 작성
'''

import csv

#사용자의 입력 처리
def get_input():
    while 1:
        BG = int(input("사용할 LDPC base graph의 종류(1 or 2): ")) #1이나 2 입력
        if BG == 1 or BG == 2:
            break
        print("잘못된 수를 입력함")

    while 1:
        iLS = int(input("index iLS의 값: ")) #0이나 4 입력
        if iLS >= 0 and iLS <= 7 and type(iLS) is int:
            break 
        print("잘못된 수를 입력함")
    
    while 1:
        Zc = int(input("lifting size Zc의 값: "))
        if iLS == 0:
            if Zc in [2, 4, 8, 16, 32, 64, 128, 256]:
                break
        elif iLS == 1:
            if Zc in [3, 6, 12, 24, 48, 96, 192, 384]:
                break
        elif iLS == 2:
            if Zc in [5, 10, 20, 40, 80, 160, 320]:
                break
        elif iLS == 3:
            if Zc in [7, 14, 28, 56, 112, 224]:
                break
        elif iLS == 4:
            if Zc in [9, 18, 36, 72, 144, 288]:
                break
        elif iLS == 5:
            if Zc in [11, 22, 44, 88, 176, 352]:
                break
        elif iLS == 6:
            if Zc in [13, 26, 52, 104, 208]:
                break
        elif iLS == 7:
            if Zc in [15, 30, 60, 120, 240]:
                break
        print("잘못된 수를 입력함")
    
    return BG, iLS, Zc


#base graph의 정보를 담은 csv 파일 읽어오기
def read_BG(filename, iLS, rows, cols):
    f = open(filename, 'r', encoding="utf-8-sig")
    BG_data = []
    col_idx = []
    row_idx = []
    value = []

    for line in csv.reader(f):
        #line[0] = row index(i)
        #line[1] = col index(j)
        #line[2] = iLS = 2-2인 V_ij
        #line[6] = iLS = 6-2인 V_ij
        row_idx.append(int(line[0]))
        col_idx.append(int(line[1]))
        value.append(int(line[iLS+2]))

    for i in range(rows):
        for j in range(cols):
            BG_data.append([i, j, 0])

    for i in range(len(row_idx)):
        idx = BG_data.index([row_idx[i], col_idx[i], 0])
        BG_data[idx][2] = 1

    return BG_data, value


#mod 연산하고 proto 파일 만들기
def write_proto(BG_data, value, rows, cols, Zc, savename):
    shift = []
    f = open(savename, "w")

    depth = 0 #depth가 뭐더라
    
    for data in BG_data:
        if depth < data[2]:
            depth = data[2]

    f.write("ROWS=" + str(rows) + "\n")
    f.write("COLS=" + str(cols) + "\n")
    f.write("DEPTH=" + str(depth) + "\n")
    f.write("ZFACTOR=" + str(Zc) + "\n")
    f.write("\nL1\n")

    cnt = 0
    for data in BG_data:
        if data[2] == 0:
            shift.append(-1)
        elif data[2] == 1:
            shift.append(value[cnt] % Zc)
            cnt += 1 
         
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            f.write(str(shift[cnt]) + "\t")
            cnt += 1
        f.write("\n")

    f.close()
    print(savename + " 파일이 저장되었습니다.")
              

#===================main=======================
BG, iLS, Zc = get_input()

if BG == 1:
    filename = "../data/csv/5G_BG1.csv"
    rows = 46
    cols = 68

else:
    filename = "../data/csv/5G_BG2.csv"
    rows = 42
    cols = 52

savename = "../data/proto/5G_BG" + str(BG) +"_iLS" + str(iLS) + "_Zc" + str(Zc) + ".proto" 

BG_data, value = read_BG(filename, iLS, rows, cols)
write_proto(BG_data, value, rows, cols, Zc, savename)



'''
보완할 점
- csv 파일은 수동 작업을 만들었으므로 오류 있을 수 있음ㅎㅎ
- if문, for문의 과다한 사용
'''
