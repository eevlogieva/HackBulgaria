import sys
import unittest

sys.path.append("..")

import sql_manager
import start
import hashlib


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '123123')

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?)', ('Dinko',))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_register_weak_password_no_letters(self):
        self.assertFalse(start.valid_password('Bat Georgi', '123'))

    def test_register_weak_password_no_digits(self):
        self.assertFalse(start.valid_password('Bat Georgi', 'asadsdss'))

    def test_register_weak_password_no_symbols(self):
        self.assertFalse(start.valid_password('Bat Georgi', '123jhsdsj'))

    def test_register_weak_password_substring(self):
        self.assertFalse(start.valid_password('Bat Georgi', '1Bat Georgi8'))

    def test_register_weak_password_less_than_8(self):
        self.assertFalse(start.valid_password('Bat Georgi', '1a&Gj'))

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_sql_injection(self):
        self.assertFalse(sql_manager.login("'OR 1 = 1 --", "12343fd"))

    def test_login_sql_injection_drop(self):
        self.assertFalse(sql_manager.login("asdass", "' OR 1 = 1; DROP TABLE clients --"))

    def test_hash_password(self):
        sql_manager.register('Tester2', '123AsSas&')
        hashed_pass = hashlib.sha1(b'123AsSas&').hexdigest()
        sql_manager.cursor.execute('SELECT password FROM clients WHERE username = ?', ('Tester2',))
        pass_in_db = sql_manager.cursor.fetchone()[0]
        self.assertEqual(hashed_pass, pass_in_db)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
