## Setup

### Set up the DB
* Run the [create_db.sql](sql/create_db.sql) script on a MySQL instance
* Update the config files if needed:
  * [sis-api/config.yml](sis-api/config.yml)
  * [sis-api/test/config.yml](sis-api/test/config.yml)

### Start the API Server
```shell
python3 -m sis-api
```

### Build the web app
```shell
cd sis-ng
npm install
npm run build
```

### Start the Web Server
```shell
python3 -m sis-web
```

## Testing
* Install all test requirements, including `behave`
* Using the ID, right click on [sis-api/test/bdd](sis-api/test/bdd) and select `Run BDD Tests`
