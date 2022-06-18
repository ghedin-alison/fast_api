from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/cursos')
async def get_cursos():
    return {'info': 'Todos os cursos via router'}

@router.post('/api/v1/cursos')
async def post_curso():
    return {'info': 'Post com as informações'}