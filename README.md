# Como utilizar

No diretório imediatamente acima do seu módulo, execute:

`git clone https://github.com/bathwaterpizza/cursoturma`

Depois você pode utilizar as funções de turma com o import:

```Python
from .. import cursoturma

turma.get_curso_by_turma(3)
```

**OBS:** Para utilizar imports relativos, seu módulo também precisa fazer parte de um package, ou seja, o diretório do módulo deve possuir um arquivo `__init__.py` assim como o nosso.

Alternativamente, se o diretório acima do seu módulo também for um repositório, como o principal, você pode adicionar turma como submódulo:

`git submodule add https://github.com/bathwaterpizza/cursoturma`

## Dependências

Python 3.9+

# Documentação adicional

## add_assunto

Função associa uma turma a um curso (assunto), a função verifica se os dois existem no sistema.

Utiliza `id_turma` do módulo alunoturma e `id_curso` do módulo curso.

### Requisitos
- Uma turma tem que possuir apenas um curso.
- Um curso pode ser assunto de mais de uma turma.

### Acoplamento

- id_turma: int
  Usado para captar uma turma através da função `get_turma()`.
  
- id_curso: int
  Usado para captar um curso que será associado a uma turma, através da função `get_curso`.

### Condições de acoplamento

- Se `id_turma` existir dentro da lista de assunto, turma já possui um curso.
- Se `get_curso()` não achar o id do curso específico, ele não existe.
- Se `get_turma()` não achar o id da turma específica, ela não existe.

## del_assunto

Função desassocia uma turma de um curso, retirando o par turma-curso da lista de assuntos.

Como toda turma identifica exclusivamente um par turma-curso, basta passar o id da turma.

### Acoplamento

- id_turma: int
  Usa o id da turma, que possui apenas um curso, para fazer a busca e deletar a lista de assuntos associada a essa turma.

### Condições de acoplamento

- `id_turma` necessita estar associado a um assunto, caso contrário nada acontecerá.

## get_curso_by_turma

Função utiliza o id de uma turma específica para retornar o curso associado a ela.

### Acoplamento

id_turma: int
- Usado na busca pela lista de assuntos, que possui o curso associado a essa turma.

### Condições de acoplamento

- `id_turma` deve estar associada a algum curso, a um assunto nesse caso.

## get_turmas_by_curso

Função retorna uma lista de IDs de turma que estão associados ao id do curso passado como parâmetro.

### Acoplamento

id_curso: int
- Usado na busca de assuntos para agrupar todos IDs de turma associados com o `id_curso` recebido.

### Condições de acoplamento
- `id_curso` deve estar associado a alguma turma para existir em uma lista `assunto`.
