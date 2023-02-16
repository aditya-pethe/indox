

## Get Random Facts

```
GET /endpoint/path
```
Description: This endpoint returns a list of random facts from the database. 

Query Parameters: 
- amount: The number of facts to return (defaults to 1)
- filter: An object containing filter parameters for the query
- animalType: The type of animal to return facts about (defaults to 'cat')

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Cats can jump up to six times their length.",
        "sendDate": "2020-08-12T00:00:00.000Z",
        "type": "cat",
        "status": {
            "verified": true,
            "feedback": "",
            "sentCount": 0
        },
        "createdAt": "2020-08-12T00:00:00.000Z",
        "updatedAt": "2020-08-12T00:00:00.000Z",
        "__v": 0
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "user": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Cats have over 20 muscles that control their ears.",
        "sendDate": "2020-08-12T00:00:00.000Z",
        "type": "cat",
        "status": {
            "verified": true,
            "feedback": "",
            "sentCount": 0
        },
        "createdAt": "2020-08-12T00:00:00.000Z",
        "updatedAt": "2020-08-12T00:00:00.000Z",
        "__v": 0
    }
]
```

## Get User Facts

```
GET /endpoint/me
```

Description: This endpoint returns a list of facts associated with a user.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter the facts by.

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Cats can be right-pawed or left-pawed.",
        "type": "cat",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        }
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Dogs can learn up to 250 words.",
        "type": "dog",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        }
    }
]
```

## Get Random Animal Fact

```
GET /endpoint/random
```

Description: This endpoint returns a random animal fact.

Query Parameters: 
- animal_type: A comma-separated list of animal types. Defaults to 'cat'.
- amount: The number of facts to return. Limited to 500 at a time.

Example Response: 
```
{
    "user": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "text": "Cats can make over 100 vocal sounds, while dogs can only make around 10.",
    "sendDate": "2020-08-20T17:00:00.000Z",
    "type": "cat",
    "status": {
        "verified": true,
        "feedback": "",
        "sentCount": 0
    },
    "createdAt": "2020-08-20T17:00:00.000Z",
    "updatedAt": "2020-08-20T17:00:00.000Z",
    "__v": 0
}
```

## Get Fact by ID

```
GET /endpoint/path
```
Description: This endpoint retrieves a fact from the database by its ID.

Query Parameters: None

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "name": "John Doe",
        "photo": "https://example.com/photo.jpg"
    },
    "text": "Cats can sleep for up to 16 hours a day.",
    "sendDate": "2020-08-01T00:00:00.000Z",
    "type": "cat",
    "status": {
        "verified": true,
        "feedback": "Approved",
        "sentCount": 0
    },
    "createdAt": "2020-08-01T00:00:00.000Z",
    "updatedAt": "2020-08-01T00:00:00.000Z",
    "__v": 0
}
```

## Create Fact Endpoint

```
POST /endpoint/path
```
Description: This endpoint allows a user to create a fact about an animal. 

Query Parameters: 
- factText: The text of the fact
- animalType: The type of animal the fact is about

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    },
    "text": "This is a fact about an animal.",
    "type": "cat",
    "sendDate": "2020-08-12T15:00:00.000Z",
    "status": {
        "verified": null,
        "feedback": null,
        "sentCount": 0
    },
    "createdAt": "2020-08-12T15:00:00.000Z",
    "updatedAt": "2020-08-12T15:00:00.000Z",
    "__v": 0
}
```