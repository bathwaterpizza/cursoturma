import unittest
from unittest.mock import patch, MagicMock
import cursoturma

class TestCursoTurma(unittest.TestCase):
    @patch('cursoturma.curso.get_curso')
    @patch('cursoturma.turma.get_turma')
    def test_add_assunto(self, mock_get_turma, mock_get_curso):
        mock_get_turma.return_value = (0, None)  # Simulating turma exists
        mock_get_curso.return_value = (0, None)  # Simulating curso exists
        cursoturma._assuntos = []  # Resetting _assuntos to empty
        result = cursoturma.add_assunto(1, 1)
        self.assertEqual(result, (0, None))
        self.assertIn({"id_turma": 1, "id_curso": 1}, cursoturma._assuntos)

    def test_del_assunto(self):
        cursoturma._assuntos = [{"id_turma": 1, "id_curso": 1}]  # Pre-populate _assuntos
        result = cursoturma.del_assunto(1)
        self.assertEqual(result, (0, None))
        self.assertNotIn({"id_turma": 1, "id_curso": 1}, cursoturma._assuntos)

    def test_get_curso_by_turma(self):
        cursoturma._assuntos = [{"id_turma": 1, "id_curso": 2}]  # Pre-populate _assuntos
        result = cursoturma.get_curso_by_turma(1)
        self.assertEqual(result, (0, 2))

    def test_get_curso_by_turma_not_associated(self):
        cursoturma._assuntos = []  # No associations
        result = cursoturma.get_curso_by_turma(1)
        self.assertEqual(result, (6, None))

    def test_get_turmas_by_curso(self):
        cursoturma._assuntos = [{"id_turma": 1, "id_curso": 2}, {"id_turma": 3, "id_curso": 2}]  # Pre-populate _assuntos
        result = cursoturma.get_turmas_by_curso(2)
        self.assertEqual(result, (0, [1, 3]))

    def test_get_turmas_by_curso_no_associations(self):
        cursoturma._assuntos = []  # No associations
        result = cursoturma.get_turmas_by_curso(2)
        self.assertEqual(result, (7, None))

if __name__ == '__main__':
    unittest.main()