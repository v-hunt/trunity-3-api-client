# API Client for Trunity 3 Learning Platform

## Installation

```
pip install <url-to-repo>
```

**Note:** PyPi package will be added soon.


## Usage

First of all, you need to authenticate withing the API
and create a session to interact with client classes:
```python
from trunity_3_client import initialize_session_from_creds

session = initialize_session_from_creds('your-login', 'your-password')
```
You need to include the `session` in all clients you want to use.


Each resource can be on of two types: `list` or `detail`.
For example, `/topics` is a 'list' type of a resource and
`/topics/{id}` is a 'detail' type of a resource. You need that
knowledge to understand how the API Clients works.

Let assume you need to make GET request to `/topics/{id}` endpoint.
How it should be done:
```python
from trunity_3_client import TopicsClient
client = TopicsClient(session)

client.detail.get(topic_id)
```


If you need to create a topic, you need to make POST request
to `list` type of url:

```python
client.list.post(site_id, name, topic_id, short_name, description)
```

Also you may use general client that has each of the client built-in:
```python
from trunity_3_client import Client
client = Client('login', 'password')

client.topics.detail.get(topic_id)
```

### Available Clients Classes:
- TopicsClient
- ContentsClient