from typing import List, Optional
from fastapi import FastAPI
from fastapi import HTTPException, status

from models import Curso

app = FastAPI()

cursos = {
    1: {
        "id": 1,
        "titulo": 'titulo 1',
        "aulas": 112,
        "horas": 200
    },
    2: {
        "id": 2,
        "titulo": 'titulo 2',
        "aulas": 224,
        "horas": 400
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso

@app.put('/cursos/{curso_id}', status_code=status.HTTP_200_OK)
async def update_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Curso de id:{curso_id} não encontrado')



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)