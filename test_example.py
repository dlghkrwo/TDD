import unittest,example

x = 20

class TestExample(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('Starting Test Case')

    # @classmethod
    # def tearDownClass(cls):
    #     print('Test case End')  

    # def setUp(self):
    #     print('Set up')
    #     # self.instance = randomClass()
    #     # self.variable = 'something '
    # def tearDown(self):
    #     print("Tear Down")

    # @unittest.xxx 는 바로아래에 있는 함수를 테스트 할떄 사용함 (스킵, 예외 등)
    # @unittest.expectedFailure
    # @unittest.skip('Skipping becasue...')
    # @unittest.skipIf(x < 12, 'Skipping because x < 12')
    def test_greet_person(self):
        # print('Great person')
        #USE with self.subTest() : I can create the subTest for each test
        if x > 12:
            self.skipTest('Skipping because x > 12')
        with self.subTest('Uppercase J'):
            greeting_message = example.greet_person("Joe")
            self.assertEqual(greeting_message, "Welcome Joe")
        
        with self.subTest('Lowercase j'):
            self.assertEqual(example.greet_person("joe"), "Welcome Joe")

 
    def test_can_drink_alcohol(self):
        '''test can drink alcohol!!'''
        # print("Can Drink")
        with self.subTest():
            self.assertFalse(example.can_drink_alcohol(16))
        with self.subTest():    
            self.assertTrue(example.can_drink_alcohol(21))

        with self.assertRaises(TypeError) as cm:
            example.can_drink_alcohol("string")

        Exception_message = cm.exception.args[0]
        self.assertEqual(Exception_message, 'You need to enter a number!')

class TestExample2(unittest.TestCase):     
    
    def test_greet_person2(self):
        if x > 12:
            self.skipTest('Skipping because x > 12')
        with self.subTest('Uppercase J'):
            greeting_message = example.greet_person("Joe")
            self.assertEqual(greeting_message, "Welcome Joe")
        
        with self.subTest('Lowercase j'):
            self.assertEqual(example.greet_person("joe"), "Welcome Joe")

if __name__ == '__main__':
    unittest.main()