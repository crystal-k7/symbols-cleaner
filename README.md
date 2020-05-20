# symbols-cleaner
cleaning special symbols

* 문자 정제
   - 특정 문자 제거(지정 옵션)
      - 한글, 영어, 숫자, -, & 제외하고 모두 제거
   - 특정 문자 치환
      - 옵션: 사용자 선택 문자 변환
      - 사용자 파일: 사용자가 변환하려는 문자가 특정 문자 제거 목록에 없을 시 추가해야함.
        (변환 과정에서 삭제될 수 있음)
         - 순서: html태그 > 사용자 파일 > 옵션 > 앞/뒤 공백 > 여러개 공백
         - 치환 문자가 특정 문자일때
            - \n 개행으로 줄을 나눌때 (1.1 적용)
            - 하나의 문자열을 여러 개로 복제해서 처리할때 (1.2 적용)
               - 한 라인에 여러개 있을 시 delete_list에 더 많은 갯수가 지워진걸로 표시됨.
                 (리스트 복제로 인한 문제)
    - 라인별 제거된 문자 -> 파일로 저장

# 필터 옵션
- user 사전 사용
- 특문 제거
- 영어 제거
- 숫자 제거
- '-' 제거 안함
- '&' 제거
해당 옵션 조정시 .py 파일을 수정
사용자 사전은 pattern.txt에 정규식으로 변환할 텍스트와 함께 구성
ex)
제거할정규식=바꿀문자 or 공백 or 아무것도 적지 않음

# 사용 방법
* 단일 파일
```
from  file_parder import Stopword

inputpath = "필터_하고싶은_파일명.txt"
outputpath = "필터_완료한_파일명.txt"

sp = Stopword()
sp.one_file_main(inputpath, outputpath)
```

* 다수 파일
```
from  file_parder import Stopword

inputpath = "필터가_필요한_폴더명"
outputpath = "필터후_저장될_폴더명"

sp = Stopword()
sp.many_file_main(inputpath, outputpath)
```

- 사용자 사전의 파일 위치를 받는 코드가 추가될 필요가 있음