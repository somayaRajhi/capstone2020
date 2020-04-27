##get\_user\_id

A GET request is invoked by the client to the server. This will return a JSON object with information containing a `user_id` number that the client will use to identify itself for every job it completes.

##JSON definition
A simple JSON object will be returned with only one field:

* `user_id`: A unique identifier of the client returning the result.

##Example return value:
```
{'user_id' = user123}
```
