# omnissa
Test suite to perform and verify CRUD (Create, Read, Update, Delete) operations on a resource

# omnissa
Test suite to perform and verify CRUD (Create, Read, Update, Delete) operations on a resource

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
- **page_objects/**: This folder can be used to create page classes and abstractions.
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
