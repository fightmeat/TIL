```python

def main():
    while True:
        print("\n영어 단어장 프로그램")
        print("1. 단어 추가")
        print("2. 단어 삭제")
        print("3. 전체 단어 보기")
        print("4. 단어 랜덤 테스트")
        print("5. 종료")
        
        choice = input("원하시는 번호를 입력하세요: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
if __name__ == "__main__":
    main()

```
```python
import sqlite3

class EnglishVocabulary:
    def __init__(self, db_path='vocabulary.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()
        
    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vocabulary (
                id INTEGER PRIMARY KEY,
                word TEXT NOT NULL UNIQUE,
                meaning TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        
    def add_word(self, word, meaning):
        try:
            self.cursor.execute('''
                INSERT INTO vocabulary (word, meaning) VALUES (?, ?)
            ''', (word, meaning))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"'{word}' is already in the vocabulary.")
            
    def get_meaning(self, word):
        self.cursor.execute('''
            SELECT meaning FROM vocabulary WHERE word = ?
        ''', (word,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def delete_word(self, word):
        self.cursor.execute('''
            DELETE FROM vocabulary WHERE word = ?
        ''', (word,))
        self.conn.commit()
    
    def list_words(self):
        self.cursor.execute('SELECT word, meaning FROM vocabulary')
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()

# 사용 예시
vocab = EnglishVocabulary()
vocab.add_word('apple', '사과')
print(vocab.get_meaning('apple'))
vocab.delete_word('apple')
print(vocab.list_words())
vocab.close()
```

