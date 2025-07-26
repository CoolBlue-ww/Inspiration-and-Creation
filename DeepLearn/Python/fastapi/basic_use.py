from fastapi import FastAPI, Header, Response
from fastapi.testclient import TestClient
import uvicorn
from PIL import Image
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
import jieba

app = FastAPI()
image = Image.open(r"L:\DeepLearn\Python\fastapi\cat.jpg")
model = SentenceTransformer(r"L:\DeepLearn\KeyBert\models\sentence-transformers\shibing624-text2vec-base-chinese")
keybert_model = KeyBERT(model=model)


@app.get("/main/")
async def root(key1: str = "key1", key2: str = "key2"):
    return {"key1": key1, "key2": key2}


@app.get("/image")
async def get_image(image_info: str = None):
    if image_info == "size":
        return {"size": image.size}
    if image_info == "width":
        return {"width": image.width}
    if image_info == "height":
        return {"height": image.height}
    if image_info == "show":
        return image.show()
    if image_info == "save":
        return image.save("cat-RGB.jpg")
    if image_info == "image":
        return image


@app.get("/headers")
async def get_headers(
        user_agent: str | None = Header(default=None),
        x_token: list[str] = Header(default=[]),
        content_type: str | None = Header(default=None, alias="content-type"),
        accept_encoding: str | None = Header(default=None, alias="accept-encoding")
) -> dict:
    return {
        "user-agent": user_agent,
        "x_token": x_token,
        "content_type": content_type,
        "accept_encoding": accept_encoding
    }


@app.get("/extract_keywords")
async def extract_keywords(text: str):
    text_cut = jieba.cut(text)
    text = " ".join(text_cut)
    keywords = keybert_model.extract_keywords(text)
    return keywords

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)  # 启动服务，也可以使用命令行启动 uvicorn main:app --reload
