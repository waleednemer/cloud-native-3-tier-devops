
import uuid


def create_test_employee(client):
    employee = {
        "first_name": "CI",
        "last_name": "Test",
        "email": f"ci-{uuid.uuid4().hex[:10]}@example.com",
        "department": "DevOps",
        "salary": 7500
    }

    response = client.post("/employees/", json=employee)

    assert response.status_code == 201
    return response.json()


def test_get_employees(client):
    response = client.get("/employees/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_employee(client):
    employee = create_test_employee(client)

    assert employee["id"] is not None
    assert employee["first_name"] == "CI"
    assert employee["department"] == "DevOps"

    response = client.delete(f"/employees/{employee['id']}")
    assert response.status_code == 200


def test_put_employee(client):
    employee = create_test_employee(client)

    updated_data = {
        "department": "Cloud Engineering",
        "salary": 9000
    }

    response = client.put(
        f"/employees/{employee['id']}",
        json=updated_data
    )

    assert response.status_code == 200
    assert response.json()["department"] == "Cloud Engineering"

    client.delete(f"/employees/{employee['id']}")


def test_delete_employee(client):
    employee = create_test_employee(client)
    employee_id = employee["id"]

    response = client.delete(f"/employees/{employee_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"

    response = client.get(f"/employees/{employee_id}")

    assert response.status_code == 404


def test_database_integration(client):
    employee = create_test_employee(client)

    response = client.get(f"/employees/{employee['id']}")

    assert response.status_code == 200
    assert response.json()["email"] == employee["email"]

    client.delete(f"/employees/{employee['id']}")
