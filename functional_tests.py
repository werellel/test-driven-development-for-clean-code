from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): # !
    def setUp(self): # 2
        self.browser = webdriver.Firefox()
        
    def tearDown(self): # 3
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self): # 4
        # 에디스는 작업 목록 오라인 앱이 나왔다는 소식을 듣고 웹 사이트를 확인하러 간다.
        self.browser.get('http://localhost:8888')
        
        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn("To-Do", self.browser.title) # 5
        self.fail("Finish the test!") # 6
        
        # 그녀는 바로 작업을 추가하기로 한다.
if __name__ == "__main__": # 7
    unittest.main(warnings='ignore') # 8