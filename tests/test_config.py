import unittest
import json
from config_check import validate_config, get_public_config

class TestConfig(unittest.TestCase):
    
    def test_valid_config(self):
        data = {"host": "localhost", "port": 8080, "log_level": "INFO", "timeout": 30, "retries": 3}
        self.assertEqual(validate_config(data), [])

    def test_missing_keys(self):
        data = {"host": "localhost"}
        errors = validate_config(data)
        self.assertTrue(len(errors) > 0)

    def test_port_type(self):
        data = {"host": "localhost", "port": "8080", "log_level": "INFO", "timeout": 30, "retries": 3}
        self.assertIn("port", str(validate_config(data)))

    def test_port_range_min(self):
        data = {"host": "localhost", "port": 0, "log_level": "INFO", "timeout": 30, "retries": 3}
        self.assertIn("диапазоне", str(validate_config(data)))

    def test_port_range_max(self):
        data = {"host": "localhost", "port": 70000, "log_level": "INFO", "timeout": 30, "retries": 3}
        self.assertIn("диапазоне", str(validate_config(data)))

    def test_host_present(self):
        data = {"port": 8080, "log_level": "INFO", "timeout": 30, "retries": 3}
        self.assertIn("host", str(validate_config(data)))

    def test_log_level_present(self):
        data = {"host": "localhost", "port": 8080, "timeout": 30, "retries": 3}
        self.assertIn("log_level", str(validate_config(data)))

    def test_timeout_present(self):
        data = {"host": "localhost", "port": 8080, "log_level": "INFO", "retries": 3}
        self.assertIn("timeout", str(validate_config(data)))

    def test_retries_present(self):
        data = {"host": "localhost", "port": 8080, "log_level": "INFO", "timeout": 30}
        self.assertIn("retries", str(validate_config(data)))

    def test_multiple_errors(self):
        data = {"port": "bad", "log_level": "INFO"}
        errors = validate_config(data)
        self.assertTrue(len(errors) >= 2)

    def test_secret_is_not_exposed(self):
        data = {
            "host": "localhost", 
            "port": 8080, 
            "log_level": "INFO", 
            "timeout": 30, 
            "retries": 3,
            "secret": "super_secret_password"
        }
        public_data = get_public_config(data)
        
        self.assertNotIn("secret", public_data, "ОШИБКА: Секрет попал в вывод конфигурации!")