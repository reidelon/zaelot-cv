# Project to manage cv in zaelot

### Getting Started
```bash
git clone https://github.com/reidelon/zaelot-cv.git

cd zaelot-cv

docker-compose up --build
```
### graphql server(Hasura)
 http://localhost:8080/v1/graphql

### Django server
 http://localhost:8009/
 

## Important Mutations

### get auth token
```
mutation tokenAuth {
  tokenAuth(password: "", username: "") {
    payload
    refreshExpiresIn
    token
  }
}
```

### verify token
```
mutation verifyToken {
  verifyToken(token: "") {
    payload
  }
}
```

### refresh token
```
mutation refreshToken {
  refreshToken(token: "") {
    payload
    refreshExpiresIn
    token
  }
}
```

### Every time you make any change in hasura, you need to export the metadata`(need to have Hasura CLI installed, see Technology section)` and commit it, like this:
```bash
cd app/hasura
```
```bash
hasura md export
```
# -Every table change need to be done using django migrations and track the table from hasura console.

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
 [Hasura CLI](https://hasura.io/docs/latest/graphql/core/hasura-cli/index.html)- Command line tool which is the primary mode of managing Hasura projects.<br />
 [PostgreSQL](https://www.postgresql.org/) - Database Engine used.<br />
 [Docker](https://www.docker.com/) - Container technology used.<br />
 [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/) - Tool to implement a GraphQL API in Python


