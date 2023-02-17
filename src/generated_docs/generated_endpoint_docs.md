#Endpoint Documentation 

});

## Google Contacts Endpoint

```
GET /google/contacts
```
Description: This endpoint is used to retrieve contacts from a user's Google account. 

Query Parameters: None

Example Response: 

```
{
    accessToken: <encrypted access token>,
    refreshToken: <refresh token>
}
```

## Google Contacts Callback Endpoint

```
GET /google/contacts/callback
```

Description: This endpoint is used to update the user's access token and refresh token after they have authenticated with Google Contacts.

Query Parameters: 
- `code`: The authorization code returned from the Google Contacts authentication process.
- `state`: The state of the application before the authentication process.

Example Response:
```
{
    "state": {
        "redirectUrl": "http://localhost:3000/dashboard"
    }
}
```

## Sign Out Endpoint

```
GET /signout
```

Description: This endpoint is used to sign out of the application.

Query Parameters: None

Example Response:

```
Status: 200
```

## Daily Endpoint

```
GET /daily
```
Description: This endpoint is used to retrieve a daily fact and the list of recipients for that fact. 

Query Parameters: 
- code: The code used to access the endpoint. 

Example Response: 
```
{
    cat: {
        recipients: [123456789, 987654321],
        fact: "Cats can make over 100 vocal sounds, while dogs can only make around 10."
    },
    dog: {
        recipients: [123456789, 987654321],
        fact: "Dogs can smell up to 100,000 times better than humans."
    }
}
```

## Message Endpoint

```
POST /message
```
Description: This endpoint is used to send a message to a recipient. It will check if the recipient exists and if not, it will create a new recipient. It will also check if the recipient has been deleted and if so, it will restore the recipient. 

Query Parameters: 
- query: text query
- number: phone number

Example Response: 
```
{
    response: message,
    delay: computeTypingDelay(message.text),
    number: req.query.number
}
```

## Get Data

```
GET /data
```

Description: This endpoint is used to retrieve data about recipients, unsubscribe dates, users, and override facts.

Query Parameters: None

Example Response: 

```
{
    recipients: {
        all: [
            {
                _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
                name: "John Doe",
                number: "+1234567890",
                addedBy: {
                    _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
                    name: "Jane Doe"
                },
                subscriptions: ["cat", "dog"]
            },
            ...
        ],
        total: 10
    },
    unsubscribeDates: [
        {
            _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
            date: "2020-08-01T00:00:00.000Z"
        },
        ...
    ],
    users: [
        {
            _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
            name: "Jane Doe",
            email: "jane@example.com"
        },
        ...
    ],
    overrideFacts: [
        {
            _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
            fact: "This is an override fact",
            sendDate: "2020-08-01T00:00:00.000Z"
        },
        ...
    ]
}
```
});

## Get Contacts

```
GET /path
```
Description: This endpoint is used to get a list of contacts from a user's Google account. It also checks if the contacts have been added to the user's list of recipients and if they have subscribed to a particular animal type. 

Query Parameters: 
- animal_type: The type of animal the user is interested in.

Example Response: 
```
[
    {
        name: 'John Doe',
        number: '1234567890',
        added: true
    },
    {
        name: 'Jane Doe',
        number: '0987654321',
        added: false
    }
]
```

## Get Random Facts

```
GET /path
```
Description: This endpoint returns a list of random facts from the database. 

Query Parameters: 
- amount: The number of facts to return (defaults to 1)
- filter: An object containing query parameters to filter the facts by
- animalType: The type of animal the facts should be about (defaults to 'cat')

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

## Get Animal Facts

```
GET /me
```

Description: This endpoint returns a list of animal facts based on the animal type specified in the query parameter.

Query Parameters: 
- animal_type: A comma-separated list of animal types.

Example Response:

```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Cats can jump up to six times their length.",
        "type": "cat",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "createdAt": "2020-08-12T15:00:00.000Z",
        "updatedAt": "2020-08-12T15:00:00.000Z",
        "__v": 0
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "text": "Dogs can smell up to 100,000 times better than humans.",
        "type": "dog",
        "user": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe"
        },
        "createdAt": "2020-08-12T15:00:00.000Z",
        "updatedAt": "2020-08-12T15:00:00.000Z",
        "__v": 0
    }
]
```

## Get Random Fact

```
GET /random
```

Description: This endpoint returns a random fact from the database.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter the facts by.
- amount: The number of facts to return. Limited to 500 facts at a time.

Example Response: 
```
{
    "user": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "text": "Cats can make over 100 vocal sounds, while dogs can make around 10.",
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
GET /:factID
```

Description: This endpoint is used to retrieve a single fact by its ID.

Query Parameters: None

Example Response: 

```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "name": "John Doe",
        "photo": "https://example.com/photo.jpg"
    },
    "text": "Did you know that cats can jump up to five times their own height?",
    "sendDate": "2020-08-12T15:00:00.000Z",
    "type": "cat",
    "status": {
        "verified": true,
        "feedback": "This fact is accurate",
        "sentCount": 5
    },
    "createdAt": "2020-08-12T15:00:00.000Z",
    "updatedAt": "2020-08-12T15:00:00.000Z",
    "__v": 0
}
```

## Create Fact Endpoint

```
POST /
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
    "sendDate": "2020-08-12T17:30:00.000Z",
    "status": {
        "verified": null,
        "feedback": null,
        "sentCount": 0
    },
    "createdAt": "2020-08-12T17:30:00.000Z",
    "updatedAt": "2020-08-12T17:30:00.000Z",
    "__v": 0
}
```

## Get Recipients

```
GET /path
```

Description: This endpoint is used to get a list of recipients.

Query Parameters: 
- animal_type: A comma-separated list of animal types.

Example Response: 

```
{
    "recipients": [
        {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe",
            "number": "+123456789",
            "addedBy": {
                "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
                "name": "Jane Doe"
            },
            "subscriptions": ["dog", "cat"]
        }
    ]
}
```

## Get Recipients

```
GET /me
```

Description: This endpoint is used to get a list of recipients based on the user's query parameters.

Query Parameters: 
- animal_type: A comma-separated list of animal types.

Example Response: 
```
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe",
        "subscriptions": ["dog", "cat"]
    },
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "Jane Doe",
        "subscriptions": ["cat"]
    }
]
```

## Add Recipients

```
POST /
```

Description: This endpoint adds recipients to the user's account.

Query Parameters: 
- `recipients`: An array of objects containing the recipient's name and number.
- `animalTypes`: An array of strings representing the types of animals the recipient is subscribed to.

Example Response: 

```
{
    "message": "Recipients added successfully",
    "recipients": [
        {
            "name": "John Doe",
            "number": "1234567890"
        },
        {
            "name": "Jane Doe",
            "number": "0987654321"
        }
    ],
    "subscriptions": [
        "dog",
        "cat"
    ]
}
```

## Delete Recipient Endpoint

```
DELETE /me
```

Description: This endpoint deletes a recipient from the database.

Query Parameters: 
- `verificationCode`: A unique code used to verify the recipient.

Example Response: 
```
{
    message: "Successfully unsubscribed (123) 456-7890"
}
```

## Delete Recipient

```
DELETE /
```

Description: This endpoint deletes a recipient from the database. 

Query Parameters: 
- recipients: An array of recipient IDs to delete
- soft: A boolean value indicating whether to soft delete or hard delete the recipient

Example Response: 
```
{
    "message": "Recipient deleted successfully"
}
```

## Get Conversation

```
GET /:number/conversation
```

Description: This endpoint is used to get a conversation between a user and a recipient.

Query Parameters: None

Example Response: 

```
{
    "message": "You aren't facting this person"
}
```
    });

    data model: 
    {
        id: String,
        name: String,
        email: String
    }

## /me

```
GET /me
```

Description: This endpoint returns the user's information.

Query Parameters: None

Example Response: 

```
{
    id: "12345",
    name: "John Doe",
    email: "johndoe@example.com"
}
```
    });

## Delete User Account

```
DELETE /me
```

Description: This endpoint allows a user to delete their account.

Query Parameters: 
- `verificationEmail`: The email address associated with the user's account.

Example Response:

```
{
    "message": "Account deleted"
}
```
});

## Create Verification Code

```
POST /me/profile/phone/verification-code
```

Description: This endpoint creates a verification code for a user's phone number.

Query Parameters: 
- user: The user's ID
- type: The type of verification code (in this case, 'phone')
- data: The user's phone number

Example Response: 
```
{
    message: "Created verification code",
    user: <user_id>,
    type: "phone",
    data: <phone_number>
}
```
});

## Update Phone Number Endpoint

```
PUT /me/profile/phone
```

Description: This endpoint updates the phone number associated with the user's profile.

Query Parameters: 
- `verificationCode`: The verification code associated with the user's phone number.

Example Response:

```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+11234567890"
}
```

## processWebhook

```
POST /
```
Description: This endpoint processes a webhook and returns a response.

Query Parameters: None

Example Response: 
```
{
    speech: response.message,
    displayText: response.message,
    data: {},
    contextOut: [],
    source: "Cat Facts"
}
```