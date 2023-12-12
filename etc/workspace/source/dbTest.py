import cx_Oracle as cx

conn = cx.connect("scott", "1234", "localhost:1521/xe")
cursor = conn.cursor()

# 자원닫기
def close():
    cursor.close()
    conn.close()
    
# 회원정보조회
def listMember():
    cursor.execute("select * from member")
    rs = cursor.fetchall()
    
    # sw = 0 # 0과 1
    
    if len(rs) == 0:
        print("등록된 회원정보가 존재하지 않습니다.")
    else:
        for row in rs:
            print(row)
            
# 회원등록처리
def insert(userid, userpass, username):
    sql = "insert into member values(:1, :2, :3)"
    cursor.execute(sql, [userid, userpass, username])
    print("회원등록이 완료되었습니다.")
    conn.commit()
    
# 회원정보수정
## 회원아이디가 일치하는 사람에 한하여 수정을 한다.
def update(userid, userpass, username):
    sql = "update member set userpass = :1, username = :2 where userid = :3"
    cursor.execute(sql, [userpass, username, userid])
    print("회원정보가 수정되었습니다.")
    conn.commit()
    
# 회원정보삭제
def delete(userid):
    sql = "delete from member where userid = :1"
    cursor.execute(sql, [userid])
    conn.commit()
    
# id체크
def id_check(userid):
    sql = "select * from member"
    cursor.execute(sql)
    
    sw = 0 # 0(회원없음), 1(회원있음)
    for row in cursor:
        if row[0] == userid:
            sw = 1
    
    return sw
    
    
    
    
    
    
    
    
    