import json

def check():
    with open('config.json.example', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    required = ["host", "port", "log_level"]
    missing = [k for k in required if k not in data]
    
    if missing:
        print(f"ОШИБКА: Отсутствуют ключи: {missing}")
        exit(1)
    
    print("Конфигурация корректна: все ключи на месте")

def get_public_config(data):
    public_config = {
        "host": data.get("host"),
        "port": data.get("port"),
        "log_level": data.get("log_level")
    }
    return public_config
if __name__ == "__main__":
    check()