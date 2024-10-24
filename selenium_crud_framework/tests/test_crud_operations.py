import requests
import pytest # type: ignore
import json

# Set your unique API endpoint from CrudCrud
BASE_URL = "https://crudcrud.com/api/c1eca691026a4713b242906ec2a3ce76/books"

@pytest.fixture(scope="module")
def book_data():
    return {
        "title": "Test Book",
        "author": "Emmanuel Hop",
        "year": 2024
    }


# Test to create a book
@pytest.mark.dependency()
def test_01_create_book(book_data):
    print("\nCreating Book...")

    # Act
    response = requests.post(BASE_URL, data=json.dumps(book_data), headers={"Content-Type": "application/json"})

    # Assertions
    response_data = response.json()
    book_data["_id"] = response_data["_id"]
    assert response.status_code == 201
    assert "_id" in response_data, f"Book creation failed: {response_data}"

    # Statements to display
    print("Request: POST", BASE_URL)
    print("Payload:", book_data)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)
    print("Book created successfully with ID:", response_data["_id"])


# Test to read all books
@pytest.mark.dependency(depends=["test_create_book"])
def test_02_get_books():
    print("\nReading Book...")

    # Act
    response = requests.get(BASE_URL)

    # Assertions
    books = response.json()
    assert response.status_code == 200
    assert len(books) > 0

    # Statements to display
    print("Request: GET", BASE_URL)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)
    print("List of Books:", books)


# Test to update a book
@pytest.mark.dependency(depends=["test_create_book"])
def test_03_update_book(book_data):
    print("\nUpdating Book...")
    updated_data = {
        "title": "Updated Test Book",
        "author": "New Author",
        "year": 2025
    }

    # Act
    response = requests.put(f"{BASE_URL}/{book_data['_id']}", data=json.dumps(updated_data), headers={"Content-Type": "application/json"})

    # Assertions
    response = requests.get(f"{BASE_URL}/{book_data['_id']}")
    book = response.json()
    assert response.status_code == 200 or response.status_code == 204  # Allow both 200 and 204 as valid responses
    assert book["title"] == "Updated Test Book"
    assert book["author"] == "New Author"
    assert book["year"] == 2025

    # Statements to display
    print("Request: PUT", BASE_URL)
    print("Payload:", updated_data)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)
    print("Updated Book:", book)


# Test to delete a book
@pytest.mark.dependency(depends=["test_create_book"])
def test_04_delete_book(book_data):
    print("\nDeleting Book...")

    # Act 1
    response = requests.delete(f"{BASE_URL}/{book_data['_id']}")
    
    # Assertions
    assert response.status_code == 200 or response.status_code == 204  # Allow both 200 and 204 as valid responses

    # Act 2
    response = requests.get(f"{BASE_URL}/{book_data['_id']}")
    assert response.status_code == 404

    # Statements to display
    print("Request: DELETE", BASE_URL)
    print("Response Status Code:", response.status_code)
    print("Book Deleted:", book_data)
