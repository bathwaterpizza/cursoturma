import os, json, subprocess, atexit

# Exportando funções de acesso
__all__ = ["add_assunto", "del_assunto", "get_curso_by_turma", "get_turmas_by_curso"]

# Globais
_SCRIPT_DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))
_DATA_DIR_PATH: str = os.path.join(_SCRIPT_DIR_PATH, "data")
_JSON_FILE_PATH: str = os.path.join(_DATA_DIR_PATH, "assuntos.json")

# [
#     {
#         "id_turma": int,
#         "id_curso": int
#     },
#     ...
# ]
_assuntos: list[dict] = []

# Funções internas
def _read_assuntos() -> None:
    """
    Lê o arquivo _JSON_FILE_PATH e carrega a lista _assuntos com seu conteúdo.

    Se não existir, chama _write_assuntos parar criar um novo vazio.
    """
    global _assuntos

    if not os.path.exists(_JSON_FILE_PATH):
        _write_assuntos()
        return

    try:
        with open(_JSON_FILE_PATH, 'r') as file:
            _assuntos = json.load(file)
    except Exception as e:
        print(f"Erro de I/O em _read_assuntos: {e}")

def _write_assuntos() -> None:
    """
    Faz o dump da lista _assuntos no arquivo _JSON_FILE_PATH.

    Cria os arquivos necessários caso não existam, gerando uma lista vazia de assuntos
    """
    if not os.path.isdir(_DATA_DIR_PATH):
        os.makedirs(_DATA_DIR_PATH)

    try:
        with open(_JSON_FILE_PATH, 'w') as file:
            json.dump(_assuntos, file, indent=2)
    except Exception as e:
        print(f"Erro de I/O em _write_assuntos: {e}")

# Funções de acesso
def add_assunto(id_turma: int, id_curso: int) -> tuple[int, None]:
    # erro se ja existir
    # pcisa usar global pra acessar _assuntos
    raise NotImplementedError

def del_assunto(id_turma: int, id_curso: int) -> tuple[int, None]:
    # erro se nao existir
    raise NotImplementedError

def get_curso_by_turma(id_turma: int) -> tuple[int, int]:
    # retorna o curso relacionado a turma
    raise NotImplementedError

def get_turmas_by_curso(id_curso: int) -> tuple[int, list[int]]:
    # retorna as turmas sobre tal curso
    raise NotImplementedError

# Setup
# Popula lista
_read_assuntos()

# Salva lista ao final da execução
atexit.register(_write_assuntos)
