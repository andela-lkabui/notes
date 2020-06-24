[![Build Status](https://travis-ci.org/lewisemm/notes.svg?branch=master)](https://travis-ci.org/lewisemm/notes)

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

The app can be stopped in one of two ways;
  * Pressing `Ctrl + C` keys on the terminal that is running `docker-compose up`.
  * Opening a new terminal window and running the following command.

    ```sh
    docker-compose down
    ```


## Documentation
Documentation for this API can be accessed through [http://localhost:8080/api/docs](http://localhost:8080/api/docs)  on the browser once the app is running.


## Running the tests
To run the tests, first make sure that the `test.sh` script has sufficient executable permissions.

```sh
sudo chmod 500 test.sh
```

Once that is done, the tests can be run by running the `test.sh` script.

```sh
./test.sh
```
