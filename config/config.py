import json , os
class Read():
    def read_config():
        path = os.getcwd() + '\\config\\config.json'
        with open(path , "r" , encoding = "utf-8") as f:
            return json.loads(f.read())
        