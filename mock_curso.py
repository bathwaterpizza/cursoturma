# Mock implementation of curso.py

def get_curso(id_curso: int) -> tuple[int, dict]:
    """
    Simulates fetching a curso by its ID.
    
    Args:
    - id_curso (int): The ID of the curso to fetch.
    
    Returns:
    - tuple[int, dict]: A tuple containing an error code and the curso data.
    """
    # Simulate a successful lookup
    if id_curso == 100:
        return 0, {"id_curso": 100, "nome": "Curso de Python"}
    
    # Simulate an unsuccessful lookup
    return 5, {}