import os, json, atexit, sys

if 'unittest' in sys.modules:
    import mock_turma as turma, mock_curso as curso
else:
    from .. import turma, curso

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
    Lê o arquivo _JSON_FILE_PATH e carrega a lista _assuntos com seu conteúdo

    Se não existir, chama _write_assuntos parar criar um novo vazio
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
    Faz o dump da lista _assuntos no arquivo _JSON_FILE_PATH

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
    """
    Associa uma turma a um curso, que seria o assunto da turma, utilizando seus IDs

    Verifica se a turma e o curso existem em seus respectivos módulos
    """
    for assunto in _assuntos:
        if assunto["id_turma"] == id_turma:
            # Turma ja está associada a um curso
            return 4, None
    
    err, _ = turma.get_turma(id_turma)
    if err == 1:
        # Turma não existe
        return 1, None
    
    err, _ = curso.get_curso(id_curso)
    if err == 5:
        # Curso não existe
        return 5, None
    
    # Adiciona assunto
    _assuntos.append({"id_turma": id_turma, "id_curso": id_curso})

    return 0, None

def del_assunto(id_turma: int) -> tuple[int, None]:
    """
    Desassocia uma turma de um curso, removendo o par turma-curso da lista de assuntos

    Como toda turma identifica unicamente um par turma-curso, basta passar o id da turma
    """
    for assunto in _assuntos:
        if assunto["id_turma"] == id_turma:
            _assuntos.remove(assunto)
            return 0, None
    
    # Turma não está associada a um curso
    return 6, None

def get_curso_by_turma(id_turma: int) -> tuple[int, int]:
    """
    Retorna o ID do curso associado a turma
    """
    for assunto in _assuntos:
        if assunto["id_turma"] == id_turma:
            return 0, assunto["id_curso"]
    
    # Turma não está associada a um curso
    return 6, None # type: ignore

def get_turmas_by_curso(id_curso: int) -> tuple[int, list[int]]:
    """
    Retorna uma lista de IDs de turmas associadas a um curso
    """
    turmas_do_curso = []
    
    for assunto in _assuntos:
        if assunto["id_curso"] == id_curso:
            turmas_do_curso.append(assunto["id_turma"])
    
    if not turmas_do_curso:
        # Curso não tem nenhuma turma associada
        return 7, None # type: ignore
    
    return 0, turmas_do_curso

# Setup
# Popula lista
_read_assuntos()

# Salva lista ao final da execução
atexit.register(_write_assuntos)
