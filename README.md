# Notes REST API
A simple REST API which allows authenticated users to create and edit notes.

## Installation
1. Clone this repository.

    ```sh
    git clone git@github.com:lewisemm/notes.git
    ```
2. Install [the Docker Engine for your platform](https://docs.docker.com/install/). When finished, check that it has installed correctly by checking the Docker Engine's version.

    ```sh
    docker --version
    ```
3. If you're running this app on Linux, [install docker-compose by following these instructions](https://docs.docker.com/compose/install/#install-compose).
    > The Docker Engine on Mac and Windows already include docker-compose, so you may skip this step if you are running on those platforms.

    After successful installation, confirm everything is in working order by checking the docker-compose version.

    ```sh
    docker-compose --version
    ```

## Setting up the development environment
Before the app can be started, two environment variables must be configured with the following values on your system.

```sh
export SETTINGS_MODULE=notes.settings.dev_settings
export DATABASE_URL="postgresql://postgres:password@db:5432/notes"
```

These environment variables are used in the `docker-compose.yml` file to configure the settings file and database service to be used by the containerized `notes_api` REST API.

## Running the app
Using docker-compose, running the app is quite straightforward.

`cd` into the root directory and issue the following command.

```sh
docker-compose up
```

To stop the app, use `Ctrl + C` to stop the `docker-compose up` command.


## Running the tests

