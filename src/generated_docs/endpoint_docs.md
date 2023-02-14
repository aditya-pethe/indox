

# Fact Endpoints

## Get Facts

```
GET /
```
Description: Retrieves a list of facts from the database.

Query Parameters: None

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "text": "Cats can be right-pawed or left-pawed.",
        "type": "cat",
        "createdAt": "2020-08-14T17:00:00.000Z",
        "updatedAt": "2020-08-14T17:00:00.000Z"
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "text": "Cats have a longer-than-normal intestine which helps them digest their food better.",
        "type": "cat",
        "createdAt": "2020-08-14T17:00:00.000Z",
        "updatedAt": "2020-08-14T17:00:00.000Z"
    }
]
```

## Get Submitted Facts

```
GET /me
```
Description: Retrieves a list of facts submitted by the current user.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter by.

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "text": "Cats can be right-pawed or left-pawed.",
        "type": "cat",
        "createdAt": "2020-08-14T17:00:00.000Z",
        "updatedAt": "2020-08-14T17:00:00.000Z"
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "text": "Cats have a longer-than-normal intestine which helps them digest their food better.",
        "type": "cat",
        "createdAt": "2020-08-14T17:00:00.000Z",
        "updatedAt": "2020-08-14T17:00:00.000Z"
    }
]
```

## Get Random Fact

```
GET /random
```
Description: Retrieves a random fact from the database.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter by.
- amount: The number of facts to retrieve. Limited to 500.

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "text": "Cats can be right-pawed or left-pawed.",
        "type": "cat",
        "createdAt": "2020-08-14T17:00:00.000Z",
        "updatedAt": "2020-08-14T17:00:00.000Z"
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "text": "Cats have a longer-than-normal intestine which helps them digest their food better.",
        "type": "cat",
        "createdAt": "2020-08-14T17:00:00.000Z",
        "updatedAt": "2020-08-14T17:00:00.000Z"
    }
]
```

## Get Fact by ID

```
GET /:factID
```
Description: Retrieves a fact from the database by its ID.

Query Parameters: None

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    },
    "text": "Cats can be right-pawed or left-pawed.",
    "type": "cat",
    "createdAt": "2020-08-14T17:00:00.000Z",
    "updatedAt": "2020-08-14T17:00:00.000Z"
}
```

## Submit a Fact

```
POST /
```
Description: Submits a new fact to the database.

Query Parameters: None

Example Request Body: 
```
{
    "factText": "Cats can be right-pawed or left-pawed.",
    "animalType": "cat"
}
```

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    },
    "text": "Cats can be right-pawed or left-pawed.",
    "type": "cat",
    "createdAt": "2020-08-14T17:00:00.000Z",
    "updatedAt": "2020-08-14T17:00:00.000Z"
}
```