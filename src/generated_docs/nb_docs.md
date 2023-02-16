
## Get a Random Fact

```
GET /random
```
Description: This endpoint returns a random fact about an animal. 

Query Parameters: 
- animal_type: A comma separated list of animal types to get facts about. Defaults to 'cat'.
- amount: The number of facts to return. Limited to 500 facts at a time.

Example Response: 
```
{
    "user": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "text": "Cats have over 20 muscles that control their ears.",
    "sendDate": "2020-09-09T00:00:00.000Z",
    "type": "cat",
    "status": {
        "verified": true,
        "feedback": "",
        "sentCount": 0
    }
}
```