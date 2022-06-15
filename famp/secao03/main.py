from distutils.log import debug
from imp import reload
from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": 'titulo 1',
        "aulas": 112,
        "horas": 200
    },
    2: {
        "titulo": 'titulo 2',
        "aulas": 224,
        "horas": 400
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)