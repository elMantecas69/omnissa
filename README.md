# CRUD Framework Documentation

## Overview

This repository contains a framework for automating CRUD (Create, Read, Update, Delete) operations using Python, Selenium, Poetry, and pytest. The framework is designed to interact with a REST API, using [crudcrud.com](https://crudcrud.com) as the example endpoint.

## Project Structure

```
selenium_crud_framework/
  |-- tests/
      |-- conftest.py
      |-- test_crud_operations.py
  |-- page_objects/
  |-- pyproject.toml
  |-- pytest.ini
  |-- README.md
```

- **tests/**: Contains all the test cases and configurations.
  - **conftest.py**: Contains reusable fixtures for Selenium WebDriver setup.
  - **test_crud_operations.py**: Contains the CRUD operation test cases.
- **page_objects/**: This folder can be used to create page classes and abstractions (this time there was not enoght time to implement POM however it could be a good improvment)
- **pyproject.toml**: Poetry project configuration.
- **pytest.ini**: Pytest configuration file.
- **README.md**: Project documentation.

## Step 1: Install Dependencies

To set up the project dependencies, use Poetry, a dependency manager for Python.

1. Install Poetry:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. Initialize a new project:
    ```sh
    mkdir selenium_crud_framework
    cd selenium_crud_framework
    poetry init --no-interaction
    ```

3. Add necessary dependencies to the project:
    ```sh
    poetry add selenium requests pytest webdriver-manager pytest-html
    ```

4. Install Selenium WebDriver (e.g., ChromeDriver):
   - Make sure you have Chrome installed, and download the corresponding ChromeDriver from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).
   - Add the executable to your system path:
     - Move `chromedriver` to a permanent location such as `/usr/local/bin/`:
       ```sh
       mv ~/Downloads/chromedriver /usr/local/bin/
       ```
     - Alternatively, add the directory containing `chromedriver` to your PATH by editing your shell configuration file (e.g., `~/.zshrc` or `~/.bashrc`):
       ```sh
       export PATH="$PATH:/path/to/chromedriver"
       ```
     - Reload your shell configuration:
       ```sh
       source ~/.zshrc  # or source ~/.bashrc
       ```

## Step 2: Setup Visual Studio Code

1. Open Visual Studio Code and open the folder containing your project (`selenium_crud_framework`).
2. Install the Python extension for VS Code to support linting and debugging.
3. Install the Poetry extension if needed (for easy management of dependencies).
4. Enable the Poetry virtual environment for VS Code using the command palette (`Ctrl+Shift+P`), by typing "Python: Select Interpreter" and choosing the Poetry environment.

## Step 3: Set Up Selenium Framework Structure

1. Inside the `selenium_crud_framework` folder, create a directory called `tests` and a Python file named `test_crud_operations.py`.

2. Create a `conftest.py` file inside the `tests` folder to contain reusable fixtures for Selenium.

3. Create a `page_objects` folder for page classes and abstractions.

## Step 4: Write Tests for CRUD Operations

The test suite covers the CRUD operations for a `book` resource. It uses the REST API endpoint from [crudcrud.com](https://crudcrud.com).

- `tests/conftest.py`: Set up Selenium WebDriver.
- `tests/test_crud_operations.py`: Perform CRUD operations using requests for API calls.

### Example CRUD Tests
The tests use `pytest` to verify CRUD functionality:

1. **Create a Book**: Use `requests.post` to create a new book.
2. **Read Books**: Use `requests.get` to retrieve the books.
3. **Update a Book**: Use `requests.put` to update an existing book.
4. **Delete a Book**: Use `requests.delete` to remove a book.

## Step 5: Run the Tests

Run the following command to execute the tests:

```sh
poetry run pytest tests/
```

This will run the CRUD operation tests using pytest.

To generate an HTML report, run:

```sh
poetry run pytest tests/ --html=report.html --self-contained-html -s
```

The `report.html` will provide a detailed report of the test results.

## Step 6: Cleanup Operations

### Pre-Execution Cleanup

To delete any generated files and directories (e.g., `.pytest_cache`, `assets`, `__pycache__`, `report.html`) before running tests, you can use a pre-execution cleanup script.

./pre_cleanup.sh
poetry run pytest tests/ --html=report.html

# Step 7: Troubleshooting, Insights, and Recommendations

### Issues Encountered During Implementation
1. **Request Timeouts**
   - *Problem*: Requests may occasionally fail due to network issues or high latency.
   - *Solution*: Implement retry logic using a loop to handle transient errors gracefully.

2. **Data Cleanup**
   - *Problem*: Data created during testing may be left behind, causing tests to fail on subsequent runs.
   - *Solution*: Ensure to include teardown steps in your tests to delete any data created during the test process.

3. **Driver Path Issues with Selenium**
   - *Problem*: Selenium tests may fail due to incorrect driver paths or outdated ChromeDriver.
   - *Solution*: Keep the ChromeDriver version aligned with your browser version and specify the correct driver path.

### Edge Cases Considered but Not Implemented
1. **Handling Duplicate Records**
   - *Reason*: Handling duplicate records, such as attempting to create books with identical titles and authors, was considered but omitted due to complexity in defining unique constraints for each resource.

2. **Concurrency Tests**
   - *Reason*: Concurrent requests, such as multiple clients trying to update the same record simultaneously, could lead to race conditions. This was not implemented due to time constraints and the need for more advanced tools like threading.

3. **Validation for Missing Fields**
   - *Reason*: Testing for API validation errors, such as missing fields or invalid data types, was not implemented as it required detailed knowledge of all resource fields and their expected behaviors.

### Additional Insights and Recommendations
1. **Use Fixtures for Reusable Data**
   - Utilize pytest fixtures for setting up reusable test data. This approach simplifies test setup and ensures consistent data across tests.

2. **Automate Test Environment Setup**
   - Consider using Docker to create a reproducible test environment, which includes both the Selenium WebDriver and dependencies. This can minimize the "it works on my machine" issues.

3. **Logging**
   - Implement proper logging in both API interactions and Selenium tests to help in debugging failed tests. Logs can provide more insight into the state of the application during test failures.

4. **Error Handling**
   - Implement better error handling when making requests. For instance, using `try...except` blocks can help capture and handle exceptions like `ConnectionError` more effectively, leading to less flakiness in the test suite.

### Common issues
For any reason, if test_01_get_address fails. The reason might be that address_id has been expired. In order to fix this issue, and continue with the next tests execution, follow the next steps:

Navigate to CrudCrud page.
Copy the 30 character address_id value ( I.e. 8cd8eac03cb948a8bc207075622b700d) from generated URL into data/addressId.json
Run the test again
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

