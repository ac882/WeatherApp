import ui
from os import path

def create_api_file():
    print("create api")
    path_ = ".env"
    if path.exists(path_):
        print("path exists")
    else:
        with open(path_, mode = "w") as f:
            f.write("API_KEY = YOUR_API_KEY")

def check_api_exists():
    with open('.env','r') as f:
        for line in f:
            for word in line.split():
                if word == "YOUR_API_KEY":
                    print("You did not insert an api key")
                    return True
    

if __name__ == "__main__":
    create_api_file()
    if check_api_exists() == True:
        exit()
    ui.initUI()