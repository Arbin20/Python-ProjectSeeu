import os
import json
import datetime
import unittest
import run              
from run import app, app_info, global_game_reset, current_game
from flask import Flask, url_for, session

class TestFlaskRoutes(unittest.TestCase):
   
    
    @classmethod
    def setUpClass(cls): #Create a file at the start of this group of tests
        print("setUpClass - TestFlaskRoutes")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass - TestFlaskRoutes")
    
    def test_index(self):
        """ Test routing for HOME page """
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_index route -- PASS")
        
    def test_register(self):
        """ Test routing for REGISTER page """
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_register route -- PASS")

    def test_halloffame(self):
        """ Test routing for HALL OF FAME page """
        tester = app.test_client(self)
        response = tester.get('/halloffame', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_halloffame route -- PASS")

    def test_about(self):
        """ Test routing for ABOUT page """
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_about -- PASS")

    def test_contact(self):
        """ Test routing for CONTACT page """
        tester = app.test_client(self)
        response = tester.get('/contact3', content_type='html/text') 
        self.assertEqual(response.status_code, 404)
        print("test_contact -- PASS")

    # INACTIVE
    def test_game_over(self):
     
        pass
    

    # Test Page Contents
    def test_index_page_loads(self):
        """ Test HOME page loads correctly"""
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b"Description" in response.data)
        print("test_index_page_loads route -- PASS")
        
  
    def test_login_correct_input(self):
    
        pass
        
    def test_login_correct_set_to_True(self):
        """ Test LOGIN set to True"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="user1"), follow_redirects=True)
        self.assertEqual(app_info["logged"], True)
        print("test_login_correct_set_to_True route -- PASS")

    # Test login button - incorrect input
    def test_login_incorrect_input(self):
        """ Test LOGIN with correct input works well"""
        tester = app.test_client(self)
        response = tester.post('/login', 
                                data=dict(username="wronguser"), 
                                follow_redirects=True)
        self.assertIn(b"That username does not exist. Please register first.", response.data)
        print("test_login_incorrect_input route -- PASS")
    
    def test_login_incorrect_set_to_False(self):
        """ Test LOGIN incorrect set to False"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="wronguser"), follow_redirects=True)
        self.assertEqual(app_info["logged"], False)
        print("test_login_incorrect_set_to_False route -- PASS")
        
    # Test login button - empty input
    def test_login_empty_input(self):
        """ Test LOGIN with No Input input works well"""
        tester = app.test_client(self)
        response = tester.post('/login', 
                                data=dict(username=""), 
                                follow_redirects=True)
        self.assertIn(b"Enter a username to log in", response.data)
        print("test_login_empty_input route -- PASS")
    
    def test_login_empty_set_to_False(self):
        """ Test LOGIN empty set to False"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username=""), follow_redirects=True)
        self.assertEqual(app_info["logged"], False)
        print("test_login_empty_set_to_False route -- PASS")

    def test_logout_set_to_False(self):
        """ Test LOGOUT set to False"""
        tester = app.test_client(self)
        response = tester.post('/logout', data=dict(username=""), follow_redirects=True)
        self.assertEqual(app_info["logged"], False)
        print("test_logout_set_to_False route -- PASS")


class TestFlaskRoutesRequireLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls): #Create a file at the start of this group of tests
        print("setUpClass - TestFlaskRoutesRequireLogin -- These are not active")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass - TestFlaskRoutesRequireLogin -- These are not active")
        
   
class TestLogInLogout(unittest.TestCase):
    '''
    Test suite for run.py
    Testing Login and Logout
    '''
    pass

class TestFileReadAppend(unittest.TestCase):
    '''
    Test suite for run.py
    Test fucntions that open, read or add data to files
    '''
    @classmethod
    def setUpClass(cls): #Create a file at the start of this group of tests
        with open("data/test_users.txt", "a") as addusernames:
            addusernames.write("test_user1" + "\n")  # Create three test users
            addusernames.write("test_user2" + "\n")
            addusernames.write("test_user3" + "\n")
        print("setUpClass - TestFileReadAppend")
        
        
        
        
        with open("data/test_json.json", "a") as addusernames:
            data = '[ {"id":1,"source":"albania.png","answer":"Albania"},{"id":2,"source":"germany.png","answer":"Germany"},{"id":3,"source":"belgium.png","answer":"Belgium"}]'
            addusernames.write(data)
        print("test_user.txt created with 3 users.")

    @classmethod
    def tearDownClass(cls):
        os.remove("data/test_users.txt")
        os.remove("data/test_json.json")
        print("tearDownClass - TestFileReadAppend")

    def test_read_from_file(self):
        """ Read from a text and json files """
        data = run.read_from_file("test_users.txt")
        self.assertIn("test_user1", data)
        self.assertIn("test_user2", data)
        self.assertIn("test_user3", data)
        self.assertNotIn("test_user4", data)
        print("test_read_from_file Read from TEXT file -- PASS")
        
       
        
        
class TestOtherFunctions(unittest.TestCase):
   
    def test_store_game_info(self):
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        empty = {
            "user":"test_user",
            # "user":"user1",
            "number_of_games":5,
            "date_best_game":"",    
            "points_best_game":29,
            "total_user_points":50,
            "games_played":[]}      
        run.gained_points = 30
        run.user_data = empty
        run.store_game_info()
        

        
        self.assertEqual(run.user_data["number_of_games"], 6)
        self.assertEqual(run.user_data["points_best_game"], 30)
        self.assertEqual(run.user_data["total_user_points"], 80)
        
        self.assertEqual(run.user_data["date_best_game"], today)
        self.assertEqual(run.user_data["games_played"], [(today, 30)])
        print("test_store_game_info -- PASS")
        
        

if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
