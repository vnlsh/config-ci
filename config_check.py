import json
import sys

REQUIRED_KEYS = ["host", "port", "log_level", "timeout", "retries"]

def validate_config(data):
    """Проверяет конфигурацию и возвращает список ошибок"""
    errors = []
    
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        errors.append(f"Отсутствуют ключи: {missing}")
        
    if "port" in data and not isinstance(data["port"], int):
        errors.append("port должен быть целым числом")
        
    if isinstance(data.get("port"), int) and not (1 <= data["port"] <= 65535):
        errors.append("port должен быть в диапазоне 1-65535")
        
    return errors

def get_public_config(data):
    """Возвращает конфигурацию для вывода в API (без секретов)"""
    public_config = {
        "host": data.get("host"),
        "port": data.get("port"),
        "log_level": data.get("log_level")
    }
    return public_config

def check():
    """Читает файл и проверяет его (для запуска из консоли)"""
    try:
        with open('config.json.example', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        sys.exit(1)
        
    errors = validate_config(data)
    if errors:
        for err in errors:
            print(f"ОШИБКА: {err}")
        sys.exit(1)
    
    print("Конфигурация корректна: все ключи на месте")

if __name__ == "__main__":
    check()