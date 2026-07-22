import json
from os.path import join, abspath, dirname

password_path = join(dirname(abspath(__file__)), "..", "your_password.json")

def my_password(password: str) -> bool:
    try :
        with open(password_path, "r") as f:
            pass_dict = json.load(f)

            f.close()
        
        if pass_dict["password"] == "":
            pass_dict["password"] = password
            
            with open(password_path, "w") as f:
                json.dump(pass_dict, f)

                f.close()

            return True
        
        if pass_dict["password"] == password:
            return True
        
        return False
    
    except Exception as e:
        print(e)
        return False

def set_password(password: str) -> bool:
    try :
        with open(password_path, "r") as f:
            pass_dict = json.load(f)

            f.close()
        
        pass_dict["password"] = password
        
        with open(password_path, "w") as f:
            json.dump(pass_dict, f)

            f.close()

        return True
        
        if pass_dict["password"] == password:
            return True
        
        return False
    
    except Exception as e:
        print(e)
        return False
            