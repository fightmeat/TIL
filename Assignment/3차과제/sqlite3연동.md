```python

import sqlite3
# isolation_level=None 옵션을 주게되면 쿼리문에 대해서 자동 커밋을 합니다.
# 보통 단어장인데 커밋누르고 하지는 않으니까 해줘야겠죠?

## DB 파일 생성 및 연결
conn = sqlite3.connect(cd,isolation_level=None)

## 커서 연결
cursor = conn.cursor()

```
