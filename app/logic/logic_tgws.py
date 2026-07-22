from python_on_whales import DockerClient
from os.path import join

from enum import Enum

from logic.logic_back import my_password

from pathlib import Path

LOGIC_DIR = Path(__file__).parent.resolve()

COMPOSE_FILE_PATH = LOGIC_DIR.parent.parent


docker = DockerClient(compose_files=[join(COMPOSE_FILE_PATH, "docker-compose.yml")])



def restart_tgws(password: str) -> bool:
    try :
        is_pass = my_password(password)
        print(is_pass)
        if is_pass:
            docker.compose.down(services=["tg-ws-proxy"])
            docker.compose.up(services=["tg-ws-proxy"], detach=True)
            return True
    except Exception as e:
        print(e)
        return False

class TypeReturn:
    SERVER = "server"
    PORT = "port"
    SECRET = "secret"

def get_proxy_url(type_return: str | None = None) -> str:

    
    try :
        logs = docker.logs(container="tg-ws-proxy")
        proxy_table = "\n".join(logs.splitlines()[:12])

        first_symbol = proxy_table.find("tg://proxy?")
        proxy_url = str(proxy_table[first_symbol:]).split("\n")[0]

        if type_return is None:
            return str(proxy_url)
        else :
            list_type = proxy_url.split("&")

            match type_return:
                case TypeReturn.SERVER:
                    server_text = list_type[0]
                    first_symbol_type = server_text.find("=")
                    result = server_text[first_symbol_type + 1:]
                case TypeReturn.PORT:
                    port_text = list_type[1]
                    first_symbol_type = port_text.find("=")
                    result = port_text[first_symbol_type + 1:]
                case TypeReturn.SECRET:
                    secret_text = list_type[2]
                    first_symbol_type = secret_text.find("=")
                    result = secret_text[first_symbol_type + 1:]

            return str(result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(get_proxy_url(TypeReturn.SERVER))
    print(get_proxy_url(TypeReturn.PORT))
    print(get_proxy_url(TypeReturn.SECRET))