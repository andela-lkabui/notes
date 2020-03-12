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

## Running the app
Using docker-compose, running the app is quite straightforward.

`cd` into the root directory and issue the following command.

```sh
docker-compose up
```

To stop the app, use `Ctrl + C` to stop the `docker-compose up` command.


## Running the tests

