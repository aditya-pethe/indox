# Endpoint_Category Endpoints

## Get Facts

```
GET /
```
Description: Retrieves a list of facts.

Query Parameters: None

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Fact text",
        "type": "cat"
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Fact text",
        "type": "dog"
    }
]
```

## Get Submitted Facts

```
GET /me
```
Description: Retrieves a list of facts submitted by the authenticated user.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter by.

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Fact text",
        "type": "cat"
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Fact text",
        "type": "dog"
    }
]
```

## Get Random Fact

```
GET /random
```
Description: Retrieves a random fact.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter by.
- amount: The number of facts to return.

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Fact text",
        "type": "cat"
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Fact text",
        "type": "dog"
    }
]
```

## Get Fact by ID

```
GET /:factID
```
Description: Retrieves a fact by its ID.

Query Parameters: None

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "text": "Fact text",
    "type": "cat",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe",
        "photo": "http://example.com/photo.jpg"
    }
}
```

## Submit a Fact

```
POST /
```
Description: Submits a fact.

Query Parameters: None

Example Request: 
```
{
    "factText": "Fact text",
    "animalType": "cat"
}
```

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "text": "Fact text",
    "type": "cat",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    }
}
```