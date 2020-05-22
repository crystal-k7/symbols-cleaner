# symbols-cleaner
텍스트 정제를 위한 Python lib 입니다.<br>
일반 특문과 별개로 &#60 ;(&#60;) &#62 ;(&#62;) &#34 ;(&#34;) &#38 ;(&#38;) 등의 html 특수문자들은 별도 옵션 없이 제거됩니다.<br>
파일을 받아서 정제 후 새로운 파일로 결과를 저장해 줍니다.<br>
어떤 문자가 제거 되었는지도 별도의 파일로 써줍니다. (추후 옵션으로 뺄 예정입니다.)<br>
진행 사항은 로그 파일에 남습니다. (추후 옵션으로 뺄 예정입니다.)

# 필터 옵션
True면 제거하는 기본 옵션들 (default: ALL False)<br>
필터 우선순위는 사용자 > 기본 필터
* 기본 옵션
  - 사용자 사전 사용
  - 영어 제거
  - 숫자 제거
  - 한글 제거
  - '-' 제거
  - '&' 제거
```
from file_parser import Stopword

Stopword(user_dict=True, del_eng=False, del_num=False, del_kor=False, del_hypen=False, del_emper=False)
```

* 사용자 사전
  - 사용자 사전은 pattern.txt 파일 기반으로 변환
  - 변환하고 싶은 문자(정규식)와 변환할 문자를 함께 구성<br>
ex) 제거할정규식=바꿀문자 or 공백 or 아무것도 적지 않음
  - 개행으로 치환도 가능
  - 하나의 문자열을 여러개로 처리하는 것도 가능<br>
 여러개의 결과가 복제되어 결과에 저장<br>
 (한 라인에 여러개 있을 시 delete_list에 더 많은 갯수가 지워진걸로 표시됨)
```
^=
%=퍼센트
```

# 사용 방법
* 단일 파일
```
from file_parser import Stopword

sp = Stopword()

inputpath = "필터_하고싶은_파일명.txt"
outputpath = "필터_완료한_파일명.txt"

sp.one_file_main(inputpath, outputpath)
```

* 다수 파일
```
from file_parser import Stopword

sp = Stopword()

inputpath = "필터가_필요한_폴더명"
outputpath = "필터후_저장될_폴더명"

sp.many_file_main(inputpath, outputpath)
```
