# Project to manage cv in zaelot

### Getting Started
```bash
git clone https://github.com/reidelon/zaelot-cv.git

cd zaelot-cv

docker-compose up --build
```

## Useful commands

### To execute django commands

```bash
docker-compose run cv-web python manage.py showmigrations
docker-compose run cv-web python manage.py migrate
```

### To debug with pdb
first the services must be stopped like this:
    
```bash
docker stop <container id>
```
afterward

```bash
docker-compose run --service-ports cv-web
```

## Prerequisites
 [Docker](https://www.docker.com/)<br />
 [Docker Compose](https://docs.docker.com/compose/)

## Technology
 [Django](https://www.djangoproject.com/) - The web framework used.<br />
 [Hasura](https://hasura.io/) - The graphql server used.<br />
 [PostgreSQL](https://www.postgresql.org/) - Database Engine used.<br />
 [Docker](https://www.docker.com/) - Container technology used.


