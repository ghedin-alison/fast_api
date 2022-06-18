from typing import Any, List, Optional
from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
# from fastapi.responses import JSONResponse
from models import Curso

from time import sleep
from fastapi import Depends

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

def fake_db():
    try:
        print('Abrindo conexao com banco de dados..')    
        sleep(2)
    finally:
        print('Fechando conexão com banco de dados')
        sleep(1)


# Injeção de dependencia
@app.get('/cursos')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None,
                                        title='ID do curso', 
                                        description='Deve ser valor entre 1 e 5',
                                        ge=1, lt=6),
                                        db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso,
                    db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso

@app.put('/cursos/{curso_id}')
async def update_curso(curso_id: int, 
                       curso: Curso,
                       db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=not_found(curso_id))

@app.delete('/cursos/{curso_id}')
async def destroy(curso_id: int, 
                  db: Any = Depends(fake_db)):
    try:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=not_found(curso_id))

# query parameters
# http://localhost:8000/calculadora?a=1&b=2&c=3
#header parameters
@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=0, lt=1000), 
                   b: int = Query(default=None, gt=0, lt=10000), 
                   c: Optional[int] = Query(default=0, ge=0, lt=10),
                   x_geek: str = Header(default=None),
                   db: Any = Depends(fake_db)):
    soma = a + b + c
    print(f'X-GEEK: {x_geek}')
    return {'Resultado': soma}


def not_found(id):
    return 'Curso de id: {id} não encontrado'




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)