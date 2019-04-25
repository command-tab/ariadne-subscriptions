# ariadne-subscriptions

Demonstrates a possible issue with [ariadne subscriptions](https://github.com/mirumee/ariadne/blob/master/docs/subscriptions.rst).

## Setup

This example uses [pipenv](https://pipenv.readthedocs.io/en/latest) for dependency management:

    pip3 install pipenv
    pipenv --three
    pipenv install
    pipenv run uvicorn --reload --port=5000 --http=h11 --ws=websockets app:app

Visit [http://localhost:5000](http://localhost:5000) to load the GraphQL Playground.

## Run Queries & Subscriptions

Execute the following query to see that the query type returns a String, as defined in `app/__init__.py`:

    query {
      ping
    }

Execute the following subscription:

    subscription {
      counter
    }

And observe this in the logs:

    INFO: ('127.0.0.1', 51738) - "WebSocket /graphql" [accepted]
    ERROR: Exception in ASGI application
    Traceback (most recent call last):
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 146, in run_asgi
        result = await self.app(self.scope, self.asgi_receive, self.asgi_send)
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/uvicorn/middleware/asgi2.py", line 7, in __call__
        await instance(receive, send)
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/ariadne/asgi.py", line 75, in handle_websocket
        await self.websocket_server(websocket)
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/ariadne/asgi.py", line 119, in websocket_server
        await self.handle_websocket_message(message, websocket, subscriptions)
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/ariadne/asgi.py", line 142, in handle_websocket_message
        message.get("payload"), operation_id, websocket, subscriptions
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/ariadne/asgi.py", line 174, in start_websocket_subscription
        error_formatter=self.error_formatter,
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/ariadne/graphql.py", line 134, in subscribe
        **kwargs,
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/graphql/subscription/subscribe.py", line 59, in subscribe
        subscribe_field_resolver,
      File "/Users/redacted/.local/share/virtualenvs/ariadne-subscriptions-MGCD41D_/lib/python3.7/site-packages/graphql/subscription/subscribe.py", line 177, in create_source_event_stream
        f"Subscription field must return AsyncIterable. Received: {event_stream!r}"
    TypeError: Subscription field must return AsyncIterable. Received: None
