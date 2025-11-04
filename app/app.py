from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends  # pyright: ignore[reportMissingImports]
from app.schemas import PostSchema 
from app.schemas import PostResponse 
from app.db import Post, create_db_and_tables, get_async_session 
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession  # pyright: ignore[reportMissingImports]
from sqlalchemy.future import select  # pyright: ignore[reportMissingImports]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    # Shutdown code can be added here if needed

app = FastAPI(lifespan=lifespan) 

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption=caption,
        url="dummy-url",
        file_type="photo",
        file_name="dummy-name" 
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]
    
    posts_data = []

    for post in posts:
        posts_data.append({
            "id": post.id,
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })

    return {"posts": posts_data}