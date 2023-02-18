# Endpoint Documentation 

});

## Google Contacts Endpoint

```
GET /google/contacts
```

Description: This endpoint is used to authenticate a user's Google contacts.

Query Parameters: 
- `accessToken`: A token used to access the user's Google contacts.
- `refreshToken`: A token used to refresh the user's access token.

Example Response:

```
{
    url: 'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcontacts.readonly&state=%7B%22action%22%3A%22contacts%3Aimport%22%7D&include_granted_scopes=true&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fauth%2Fgoogle%2Fcallback&response_type=code&client_id=123456789.apps.googleusercontent.com'
}
```

## Google Contacts Callback Endpoint

```
GET /google/contacts/callback
```

Description: This endpoint is used to update the user's access token and refresh token after authenticating with Google Contacts.

Query Parameters: 
- `code`: The authorization code returned from the Google Contacts authentication process.
- `state`: The state of the application before the authentication process.

Example Response:

```
{
    "state": {
        "redirect": "/dashboard"
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
- `code`: The code used to access the endpoint.

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
Description: This endpoint is used to send a message to a recipient. It will check if the recipient exists, and if not, create a new recipient. It will also check if the recipient has been deleted, and if so, restore them. 

Query Parameters: 
- `query`: The text of the message to be sent
- `number`: The phone number of the recipient

Example Response: 
```
{
    response: {
        text: "Welcome back!",
        number: "1234567890",
        type: "outgoing"
    },
    delay: 4,
    number: "1234567890"
}
```

## Get Data

```
GET /data
```

Description: This endpoint is used to retrieve data from the Recipient, UnsubscribeDate, User, and Fact models.

Query Parameters: 
- None

Example Response: 

```
{
    recipients: {
        all: [
            {
                _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
                name: "John Doe",
                number: "+15555555555",
                addedBy: {
                    _id: "5f3f3f3f3f3f3f3f3f3f3f3f",
                    name: "Jane Doe"
                },
                subscriptions: ["dog", "cat"]
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
            sendDate: "2020-08-01T00:00:00.000Z"
        },
        ...
    ]
}
```
});

## Get Contacts

```
GET /
```
Description: This endpoint retrieves a list of contacts from a user's Google account. It also checks if the contacts have been added to the user's list of recipients for a given animal type.

Query Parameters: 
- `animal_type`: The type of animal for which the user is checking if the contacts have been added as recipients.

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
GET /
```
Description: This endpoint returns a list of random facts from the database.

Query Parameters: 
- `amount`: The number of facts to return (defaults to 1)
- `filter`: An object containing filter parameters
- `animalType`: The type of animal to return facts about (defaults to 'cat')

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

## Get Facts

```
GET /me
```
Description: This endpoint returns a list of facts based on the user's query parameters.

Query Parameters: 
- `animal_type`: A comma-separated list of animal types to filter the facts by.

Example Response:

```
{
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    },
    "text": "Cats can be right-pawed or left-pawed.",
    "type": "cat"
}
```

## Get Random Animal Facts

```
GET /random
```
Description: This endpoint returns a random animal fact from the database.

Query Parameters: 
- `animal_type`: A comma-separated list of animal types to filter the facts by.
- `amount`: The number of facts to return. Limited to 500 facts at a time.

Example Response:

```
{
    "user": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "text": "Cats can make over 100 vocal sounds.",
    "sendDate": "2020-08-20T15:00:00.000Z",
    "type": "cat",
    "status": {
        "verified": true,
        "feedback": "",
        "sentCount": 0
    },
    "createdAt": "2020-08-20T15:00:00.000Z",
    "updatedAt": "2020-08-20T15:00:00.000Z",
    "__v": 0
}
```

## Get Fact by ID

```
GET /:factID
```

Description: This endpoint retrieves a fact by its ID.

Query Parameters: 
- `factID`: The ID of the fact to be retrieved.

Example Response:

```
{
    "_id": "5f3f9f9f9f9f9f9f9f9f9f9f",
    "user": {
        "name": "John Doe",
        "photo": "https://example.com/photo.jpg"
    },
    "text": "Fact text here",
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
POST /
```
Description: This endpoint allows a user to create a fact about an animal.

Query Parameters: 
- `factText`: The text of the fact
- `animalType`: The type of animal the fact is about

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    },
    "text": "Fact about an animal.",
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
GET /
```
Description: This endpoint is used to get a list of recipients.

Query Parameters: 
- `animal_type`: A comma-separated list of animal types to filter the recipients by.

Example Response:

```json
[
    {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe",
        "number": "+15555555555",
        "addedBy": {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "Jane Doe"
        },
        "subscriptions": ["cat", "dog"]
    }
]
```

## Get Recipients

```
GET /me
```

Description: This endpoint returns a list of recipients based on the user's query parameters.

Query Parameters: 
- `animal_type`: A comma-separated list of animal types to filter the recipients by.

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
- `recipients`: An array of objects containing the recipient's name and phone number.
- `animalTypes`: An array of strings containing the types of animals the recipient is subscribed to.

Example Response:

```
{
    "success": true,
    "recipients": [
        {
            "name": "John Doe",
            "number": "1234567890",
            "subscriptions": [
                "dog",
                "cat"
            ]
        }
    ]
}
```

## Unsubscribe Endpoint

```
DELETE /me
```
Description: This endpoint is used to unsubscribe a user's phone number from the service.

Query Parameters: 
- `verificationCode`: The verification code associated with the user's phone number.

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
- `recipients`: An array of recipient IDs to delete
- `soft`: A boolean value indicating whether to soft delete or hard delete the recipient

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

Query Parameters: 
- `number`: The phone number of the recipient.

Example Response:

```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "number": "1234567890",
    "message": "Hello, how are you?"
}
```
    });

## /me

```
GET /me
```
Description: This endpoint returns the user object associated with the authenticated user.

Query Parameters: None

Example Response:

```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "name": "John Doe",
    "email": "johndoe@example.com"
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
    message: 'Account deleted'
}
```
    });

## Generate Verification Code

```
POST /me/profile/phone/verification-code
```

Description: This endpoint generates a verification code for a user's phone number.

Query Parameters: 
- `phone`: The phone number to generate a verification code for.

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

## Update User Phone Number

```
PUT /me/profile/phone
```

Description: This endpoint updates the user's phone number in the database.

Query Parameters: 
- `verificationCode`: The verification code sent to the user's phone number.

Example Response:

```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+11234567890"
}
```

## Process Webhook

```
POST /[insert path here]
```
Description: This endpoint processes a webhook and returns a response.

Query Parameters: 
- `req`: The webhook request

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
Data Model: 
```
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const mongooseDelete = require('mongoose-delete');
const random = require('mongoose-simple-random');
const { animalTypes } = require('../config/strings.js');

const FactSchema = new Schema({
    user: { type: Schema.Types.ObjectId, ref: 'User' },
    text: { type: String, required: true, unique: true },
    sendDate: { type: Date },
    type: { type: String, enum: animalTypes, default: 'cat' },
    status: {
        verified: { type: Boolean, default: null },
        feedback: { type: String },
        sentCount: { type: Number, default: 0 }
    }
}, {
    timestamps: true
});

/**
 * Soft delete implementation
 * https://github.com/dsanel/mongoose-delete
 */
FactSchema.plugin(mongooseDelete, { overrideMethods: true });
FactSchema.plugin(random);

FactSchema.statics.getFact = function({ amount = 1, filter = {}, animalType = 'cat' }) {

    if (typeof animalType === 'string') {
        animalType = [animalType];
    }

    const query = {
        ...filter,
        type: { $in: animalType }
    };

    return new Promise((resolve, reject) => {
        this.findRandom(query, {}, { limit: amount }, (err, facts) => {
            if (err) return reject(err);
            facts = facts || [];

            resolve(amount == 1 ? facts[0] : facts);
        });
    });
};

const Fact = mongoose.model('Fact', FactSchema);

module.exports = Fact;
```