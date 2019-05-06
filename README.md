# ariadne-subscriptions

Demonstrates how to use [ariadne subscriptions](https://github.com/mirumee/ariadne/blob/master/docs/subscriptions.rst).

## Setup

This example uses [pipenv](https://pipenv.readthedocs.io/en/latest) for dependency management:

    pip3 install pipenv
    pipenv --three
    pipenv install
    pipenv run uvicorn --reload --port=5000 --http=h11 --ws=websockets app:app

Visit [http://localhost:5000](http://localhost:5000) to load the GraphQL Playground.

## Run Queries & Subscriptions

Execute the following query to see that the `ping` query type returns a String, as defined in `app/__init__.py`:

    query {
      ping
    }

Execute the following subscription to see the subscription return multiple responses over time:

    subscription {
      counter
    }
