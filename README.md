# Set up

1. Create and activate virtual environment

   ```bash
   pipenv --python 3.10
   
   pipenv shell
   ```
3. Install django

   ```bash
   
   pipenv install django
   ```
5. Start project using this template, ensuring to replace `ian_test_proj` with the appropriate project name on the command below:

    ```bash
    django-admin startproject --template https://github.com/Impact-Africa-Network/ian-django-template/archive/main.zip ian_test_proj .
    ```
4. Rename all the `.template` files by removing the `.template` extensions

5. Copy the contents of `example.env` to `.env`

    ```bash
    
       cp example.env .env
     ```

6. Populate the `.env` with real values.

7. Setup your database, and run migrations.
