# BoojPressDocker

## Example using docker
```
docker build -t simpe-callback-server .
docker run \
    --name=simple-callback-server \
    -e SCS_MYSQL_HOST="HOST" \
    -e SCS_MYSQL_USER="USER" \
    -e SCS_MYSQL_PASS="PASS" \
    -e SCS_MYSQL_NAME="simple_callback_server" \
    -e VIRTUAL_HOST='simpe-callback-server.example.com' \
    -td \
    --restart=always \
    simple-callback-server:latest
```


## Environmental Vars
ENV Var | Default | Description
--- | --- | ---
`SCS_MYSQL_USER` | *None* | Database user name
`SCS_MYSQL_PASS`  | *None* |  Database user password
`SCS_MYSQL_HOST` | *None* | Database host
`SCS_MYSQL_NAME`  | *None* | Database name
`VIRTUAL_HOST`  |  *None*  | URL the Nginx proxy will route to this container
`SCS_ADMIN_URL` | 'the-admin' | URI for admin