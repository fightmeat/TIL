import pickle

# 도서 등록
def add_book(no, subject, content): # no = '1'
    data = get_all_book()
    assert no not in data
    
    data[no] = {'no':no, 'subject':subject, 'content':content}
    
    with open('book.pickle', 'ab') as f:
        pickle.dump(data, f)


# 도서 정보 읽기
def get_all_book():
    try:
        with open("book.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError as e:
        return {}
    
# 도서 검색
def get_book(no):
    data = get_all_book()
    return data[no]