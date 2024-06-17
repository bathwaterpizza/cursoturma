# Mock implementation of turma.py

def get_turma(id_turma: int) -> tuple[int, dict]:
    """
    Simulates fetching a turma by its ID.
    
    Args:
    - id_turma (int): The ID of the turma to fetch.
    
    Returns:
    - tuple[int, dict]: A tuple containing an error code and the turma data.
    """
    # Simulate a successful lookup
    if id_turma == 200:
        return 0, {"id_turma": 200, "nome": "Turma A"}
    
    # Simulate an unsuccessful lookup
    return 1, {}