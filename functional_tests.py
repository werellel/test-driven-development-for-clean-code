from selenium import webdriver
browser = webdriver.Firefox()

# 에디스는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
# 해당 웹 사이트를 확인하러 간다.
browser.get('http://localhost:8000')

# 웹 페이지 타이틀과 헤더가 'To-DO'를 표시하고 있다.
assert 'To-Do' in browser.title

# 바로 작업을 추가하기로 한다.

# 공작깃털 사기라고 텍스트 상자에 입력

# 엔터키를 치면 페이지가 갱신되고 작업 목록에 아이템이 추가된다.

#...

# 만족하고 잠에 든다.
browser.quit()