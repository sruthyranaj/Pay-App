# PayApp

## Setup
  - Setup virtual environment
  ```sh
  virtualenv -p python3.8 venv
  ```

   ```sh
  source venv/bin/activate
  ```

  - start application
    ```sh
  pip install -r requirements.txt
  ```
  - create env file .env in payapp folder

  - migrate db
    ```sh
    python manage.py migrate
    ```
   - run application
```sh
    python manage.py runserver
    ```
   - run testcase
```sh
    python manage.py test
    ```




