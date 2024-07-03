import requests
import json
from test_runner import test_functions

BASE_URL = "http://localhost:5000"


def test_basic_auth_no_credentials():
    """Test that the endpoint returns 401 when no credentials are provided."""
    response = requests.get(f"{BASE_URL}/basic-protected")
    assert response.status_code == 401


def test_basic_auth_valid_credentials():
    """Test that the endpoint returns 200 when valid credentials are provided."""
    response = requests.get(f"{BASE_URL}/basic-protected", auth=("user1", "password"))
    assert response.status_code == 200
    assert response.text == "Basic Auth: Access Granted"


def test_basic_auth_invalid_credentials():
    """Test that the endpoint returns 401 when invalid credentials are provided."""
    response = requests.get(
        f"{BASE_URL}/basic-protected", auth=("user1", "wrongpassword")
    )
    assert response.status_code == 401


def test_jwt_login_valid_credentials():
    """Test that the login endpoint returns a valid JWT token when valid credentials are provided."""
    login_data = {"username": "user1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_jwt_login_invalid_credentials():
    """Test that the login endpoint returns 401 when invalid credentials are provided."""
    login_data = {"username": "user1", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 401


def test_jwt_protected_no_token():
    """Test that the jwt-protected endpoint returns 401 when no token is provided."""
    response = requests.get(f"{BASE_URL}/jwt-protected")
    assert response.status_code == 401


def test_jwt_protected_valid_token():
    """Test that the jwt-protected endpoint returns 200 when a valid token is provided."""
    login_data = {"username": "user1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    assert response.status_code == 200
    assert response.text == "JWT Auth: Access Granted"


def test_jwt_protected_invalid_token():
    """Test that the jwt-protected endpoint returns 401 when an invalid token is provided."""
    headers = {"Authorization": "Bearer invalidtoken"}
    response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    assert response.status_code == 401


def test_admin_only_no_token():
    """Test that the admin-only endpoint returns 401 when no token is provided."""
    response = requests.get(f"{BASE_URL}/admin-only")
    assert response.status_code == 401


def test_admin_only_user_token():
    """Test that the admin-only endpoint returns 403 when a user token is provided."""
    login_data = {"username": "user1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
    assert response.status_code == 403
    assert response.json() == {"error": "Admin access required"}


def test_admin_only_admin_token():
    """Test that the admin-only endpoint returns 200 when an admin token is provided."""
    login_data = {"username": "admin1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
    assert response.status_code == 200
    assert response.text == "Admin Access: Granted"


if __name__ == "__main__":
    test_functions(
        [
            test_basic_auth_no_credentials,
            test_basic_auth_valid_credentials,
            test_basic_auth_invalid_credentials,
            test_jwt_login_valid_credentials,
            test_jwt_login_invalid_credentials,
            test_jwt_protected_no_token,
            test_jwt_protected_valid_token,
            test_jwt_protected_invalid_token,
            test_admin_only_no_token,
            test_admin_only_user_token,
            test_admin_only_admin_token,
        ]
    )
