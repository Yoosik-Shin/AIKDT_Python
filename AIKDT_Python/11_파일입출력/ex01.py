'''
  파일 입출력
  - 텍스트 파일 생성하기
'''

# 파일 열기 : open(파일명, 모드, 옵션)
# 모드
# r       : 읽기모드
# w       : 쓰기모드
# a       : 추가모드
# ---------------------
# t       : 텍스트모드
# b       : 바이너리모드

# 옵션
# - encoding    : 파일을 인코딩하는 방식을 지정
# - newline     : 파일에서 사용하는 줄 바꿈 문자를 지정하는 속성
#                 None / '' . '\n',...
# - buffering   : 버퍼 사용 설정(byte 단위)
#               * 버퍼링 사용 안함 - 0
#               * 라인모드 - 1
#               * 버퍼크기 - 1보다 큰 정수 ex) 1024
# - errors      : 인코딩 및 디코딩 처리과정에서 발생하는 에러 처리방법 지정
#                 'strict' (에러발생) 'ignore' (무시) 'replace' (마커로 에러확인)


# 파일 출력
# - 파일 경로   : ~/hello.txt
# - 모드        : 'wt' (쓰기 모드 - 기존내용을 덮어쓰기함.)

path = 'C:/SYS/AIKDT_Python/11_파일입출력/file/'
# 파일 열기
file = open(path + 'hello.txt', 'wt', encoding='UTF-8')

# 파일 내에서 출력 : write()
file.write('안녕하세요')
file.write('\n')
file.write('파일 입출력 내용을 학습합니다.')

# 덮어쓰기 실험용
# file.write('')
# file.write('\n')
# file.write('')

print('파일이 생성되었습니다.')

# 파일 닫기
file.close()