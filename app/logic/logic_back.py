import json
from os.path import join

def my_password(password: str):
    with open(join("..", "your_password.json"), "r") as f:
        pass_dict = json.load(f)

        f.close()
    


    if pass_dict["password"] == "":
        pass_dict["password"] = password
        
        with open(join("..", "your_password.json"), "w") as f:
            json.dump(pass_dict, f)

            f.close()

        return True
    
    if pass_dict["password"] == password:
        return True
    
    return False
            