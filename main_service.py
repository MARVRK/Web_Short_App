import uvicorn
from fastapi import FastAPI, APIRouter
from repoimple import UserRepository
from schemas import CreateUser

user_repo_prod = UserRepository()


def create_router(app : FastAPI) -> APIRouter:
    router = APIRouter(prefix="/app/v1")

    @router.post("/users")
    def create_user(data: CreateUser):
        new_user = app.state.repo.save_user(name=data.user_name)
        return {"user_id": new_user.id,
                "user_name": new_user.name}

    @router.get("/users/{user_id}")
    def get_user(user_id: int):
        user = app.state.repo.download_user(user_id=user_id)
        if user:
            return {"user_id": user.id,
                    "user_name": user.name}
        return None
    return router

def create_app(repo: UserRepository) -> FastAPI:
    application = FastAPI()
    application.state.repo = repo
    router = create_router(application)
    application.include_router(router)

    return application

app = create_app(repo=user_repo_prod)


if __name__ == "__main__":
    uvicorn.run("main_service:app")
