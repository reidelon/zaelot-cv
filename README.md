# Project to manage cv in zaelot

This is a `todo` REST-FULL API made following TDD

### Getting Started
```bash
git clone https://github.com/reidelon/todo_app-flask-tdd-docker.git

cd todo_app-flask-tdd-docker

docker-compose up --build
```

### Useful commands

## To execute django commands

```bash
sudo docker-compose run cv-web python manage.py showmigrations
sudo docker-compose run cv-web python manage.py migrate
```

## To debug with pdb
     `first the services must be stopped like this:`
    ```bash
    docker stop <container id>
    ```

    `afterward`
    ```bash
    sudo docker-compose run --service-ports cv-web
    ```

## Technology
    * [Django](https://www.djangoproject.com/) - The web framework used.
    * [Hasura](https://hasura.io/) - The graphql server used.
    * [PostgreSQL](https://www.postgresql.org/) - Database Engine used.
    * [Docker](https://www.docker.com/) - Container technology used.


