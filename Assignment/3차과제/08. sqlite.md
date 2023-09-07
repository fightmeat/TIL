## 그러면 최종적으로는 sqlite로 짠 코드는 이렇게 되겠네요
### 근데 이러면 결국 pickle을 import 할 이유가 없네요 .pkl파일 대신에 .db파일이 생기니까

```python

import sqlite3
import random

DB_NAME = "vocabulary.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vocabulary (
        word TEXT PRIMARY KEY,
        meanings TEXT
    )
    """)
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT word, meanings FROM vocabulary")
    data = {row[0]: row[1].split(', ') for row in cursor.fetchall()}
    conn.close()
    return data

def save_data(vocabulary):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for word, meanings in vocabulary.items():
        meanings_str = ', '.join(meanings)
        cursor.execute("INSERT OR REPLACE INTO vocabulary (word, meanings) VALUES (?, ?)", (word, meanings_str))

    conn.commit()
    conn.close()

def add_word(vocabulary):
    word = input("추가할 단어를 입력하세요: ").strip()
    meaning = input(f"{word}의 뜻을 입력하세요: ").strip()
    word = word.lower()

    if word in vocabulary:
        if meaning not in vocabulary[word]:
            vocabulary[word].append(meaning)
        else:
            print(f"'{meaning}' 은 중복되는 뜻이에요.")
    else:
        vocabulary[word] = [meaning]

    return vocabulary

def delete_word(vocabulary):
    word = input("삭제할 단어를 입력하세요: ").strip()
    meaning = input(f"{word}의 뜻을 삭제하려면 뜻을 입력하세요 (전체 삭제는 그냥 Enter): ").strip()

    if word in vocabulary:
        if meaning:
            if meaning in vocabulary[word]:
                vocabulary[word].remove(meaning)
                if not vocabulary[word]:
                    del vocabulary[word]
            else:
                print(f"'{meaning}' 는 '{word}'의 뜻에 없어요.")
        else:
            del vocabulary[word]
    else:
        print(f"'{word}' 는 단어장에 없습니다.")

    return vocabulary

def search_language(vocabulary):
    language = input("검색할 단어나 뜻을 입력하세요: ").strip()
    results = {}

    for word, meanings in vocabulary.items():
        if language == word or language in meanings:
            results[word] = meanings

    if results:
        for word, meanings in results.items():
            print(f"{word} : {', '.join(meanings)}")
    else:
        print("검색된 단어나 뜻이 없습니다.")

def list_language(vocabulary):
    zero = 0
    total_words = len(vocabulary)
    print(f"총 단어 수: {total_words}\n")

    while True:
        if zero < len(vocabulary):
            for word, meanings in list(vocabulary.items())[zero:zero+10]:
                print(f"{word} : {', '.join(meanings)}")
            choice = input("\n다음 페이지를 볼꺼면 y를 눌러주세요. 메뉴로 나가려면 q를 눌러주세요: ").lower().strip()

            if choice == 'y':
                zero += 10
            elif choice == 'q':
                print("메뉴로 돌아갑니다.")
                break
            else:
                print("잘못된 입력입니다. 'y' 또는 'q'를 입력해주세요.")
                continue
        else:
            print("더 이상 단어가 없습니다.")
            break

def random_test(vocabulary):
    while True:
        if not vocabulary:
            print("테스트할 단어가 없습니다. 먼저 단어를 추가해주세요.")
            return

        word, meanings = random.choice(list(vocabulary.items()))
        meanings = [meaning.strip() for meaning in meanings]

        if random.choice([True, False]):
            print(f"'{word}'의 뜻은 무엇인가요?")
            answer = input("뜻을 입력하세요 (메뉴로 돌아가려면 'q' 입력, 여러 답을 입력할 때는 쉼표로 구분): ").lower().strip()
            if answer == "q":
                print("메뉴로 돌아갑니다.")
                return
            answer_list = [ans.strip() for ans in answer.split(',')]

            if not all(ans in meanings for ans in answer_list):
                print(f"틀렸습니다. 정답은 {', '.join(meanings)} 입니다.")
            else:
                print(f"정답입니다! 정답은 {', '.join(meanings)} 입니다.")
        else:
            selected_meaning = random.choice(meanings)
            print(f"이 뜻을 가진 단어는 무엇인가요? : {selected_meaning}")
            answer = input("단어를 입력하세요 (메뉴로 돌아가려면 'q' 입력): ").lower().strip()
            if answer == "q":
                print("메뉴로 돌아갑니다.")
                return
            if answer == word:
                print(f"정답입니다! 정답은 '{word}' 입니다.")
            else:
                print(f"틀렸습니다. 정답은 '{word}' 입니다.")
        print("\n다음 문제!\n")

def main():
    setup_database()
    vocabulary = load_data()

    while True:
        print("\n영어 단어장 프로그램\n")
        print("1. 단어 추가")
        print("2. 단어 삭제")
        print("3. 단어 검색")
        print("4. 전체 단어 보기")
        print("5. 단어 랜덤 테스트")
        print("6. 종료")

        choice = input("원하시는 기능의 번호를 입력하세요: ").strip()
        if choice == "1":
            vocabulary = add_word(vocabulary)
        elif choice == "2":
            vocabulary = delete_word(vocabulary)
        elif choice == "3":
            search_language(vocabulary)
        elif choice == "4":
            list_language(vocabulary)
        elif choice == "5":
            random_test(vocabulary)
        elif choice == "6":
            save_data(vocabulary)
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
