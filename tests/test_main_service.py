from ..main_service import create_app
from models import User
from ..repoimple import MockUserRepository
from fastapi.testclient import TestClient


def test_create_user():
    # Given
    repo_user_test = MockUserRepository(store={"Test_user":User(id=1, name="Test_user")})
    test_app = create_app(repo=repo_user_test)
    client = TestClient(test_app)
    # When
    response = client.post(url="/app/v1/users", json={"user_name": "Test_user"})
    # Then
    assert response.status_code == 200
    assert response.json() == {"user_id": 1,
                               "user_name": "Test_user" }

def test_get_user():
    # Given
    repo_user_test = MockUserRepository(store={1:User(id=1, name="Test_user")})
    test_app = create_app(repo=repo_user_test)
    client = TestClient(test_app)
    # When
    response = client.get("/app/v1/users/1")
    # Then
    assert response.status_code == 200
    assert response.json() == {"user_id": 1,
                               "user_name": "Test_user" }


