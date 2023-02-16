#Endpoint Documentation 


## Google Contacts Endpoint

```
GET /google/contacts
```

Description: This endpoint is used to authenticate a user's Google contacts.

Query Parameters: None

Example Response: A redirect to the Google authentication page.

## Google Contacts Callback Endpoint

```
GET /google/contacts/callback
```

Description: This endpoint is used to handle the callback from the Google Contacts API. It is used to update the user's access token and refresh token in the database.

Query Parameters: 
- `code`: The authorization code returned from the Google Contacts API.
- `state`: The state of the request.

Example Response:
```
{
    "state": {
        "redirectUrl": "http://localhost:3000/contacts"
    }
}
```

Data Model:
```
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const crypto = require('crypto');
const mongooseDelete = require('mongoose-delete');

const keys = require.main.require('./app/config/keys');
const strings = require.main.require('./app/config/strings');

// Make email and phone docs unique except for those that are flagged as deleted
const uniquePartialIndex = {
    unique: true,
    partialFilterExpression: {
        deleted: false
    }
};

const UserSchema = new Schema({
    name: {
        first:  {type: String, required: true},
        last:   {type: String, required: true}
    },
    email:      {type: String},
    phone:      {type: String},
    photo:      {type: String, default: strings.userPhotoUrl},
    google: {
        id:           {type: String},
        accessToken:  {type: String},
        refreshToken: {type: String}
    },
    isAdmin: {type: Boolean, default: false},
    ip: String
}, {
    timestamps: true
});

UserSchema.statics.encryptAccessToken = function(plainText) {
    return crypto
        .createCipher(keys.encryption.algorithm, keys.encryption.key)
        .update(plainText, 'utf-8', 'hex');
};

UserSchema.statics.decryptAccessToken = function(cipher) {
    return crypto
        .createDecipher(keys.encryption.algorithm, keys.encryption.key)
        .update(cipher, 'hex', 'utf-8');
};

UserSchema.plugin(mongooseDelete, {overrideMethods: true});

UserSchema.index({email: 1, phone: 1}, uniquePartialIndex);

var User = mongoose.model('User', UserSchema);

module.exports = User;
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
GET /endpoint/path
```
Description: This endpoint is used to send facts to recipients who have subscribed to a certain animal type. 

Query Parameters: 
- code: The code used to access the endpoint

Example Response: 
```
{
    cat: {
        recipients: [123456789],
        fact: "Cats can sleep up to 20 hours a day!"
    },
    dog: {
        recipients: [987654321],
        fact: "Dogs can hear sounds four times farther away than humans!"
    }
}
```

## Send Message Endpoint

```
POST /message
```
Description: This endpoint is used to send a message to a recipient. It will check if the recipient exists, and if not, create a new recipient. It will also check if the recipient has been deleted, and if so, restore them. 

Query Parameters: 
- query: Text query provided
- number: Phone number provided

Example Response: 
```
{
    response: {
        text: "Welcome back!",
        number: "1234567890",
        type: "outgoing"
    },
    delay: 2,
    number: "1234567890"
}
```

## Get Data

```
GET /endpoint/data
```

Description: This endpoint is used to retrieve data from the Recipient, UnsubscribeDate, User, and Fact models.

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
            sendDate: "2020-08-01T00:00:00.000Z"
        },
        ...
    ]
}
```

## Get Contacts

```
GET /endpoint/path
```
Description: This endpoint is used to get a list of contacts from a user's Google account.

Query Parameters: 
- `animal_type`: The type of animal the user is subscribed to.

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
Description: This endpoint is used to create a new fact. 

Query Parameters: 
- factText: The text of the fact
- animalType: The type of animal associated with the fact

Example Response: 
```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "user": {
        "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
        "name": "John Doe"
    },
    "text": "This is a fact about cats.",
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

## Get Recipients

```
GET /endpoint/path
```

Description: This endpoint is used to get a list of recipients.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter the recipients by.

Example Response: 

```
{
    "recipients": [
        {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "name": "John Doe",
            "number": "+15555555555",
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
GET /endpoint/me
```

Description: This endpoint returns a list of recipients based on the user's query parameters.

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
POST /endpoint/path
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
DELETE /endpoint/path
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
GET /endpoint/path
```

Description: This endpoint is used to get a conversation between a user and a recipient.

Query Parameters: None

Example Response: 

```
{
    "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
    "number": "1234567890",
    "messages": [
        {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "sender": "user",
            "recipient": "recipient",
            "message": "Hello, how are you?"
        },
        {
            "_id": "5f3f3f3f3f3f3f3f3f3f3f3f",
            "sender": "recipient",
            "recipient": "user",
            "message": "I'm doing well, thank you!"
        }
    ]
}
```

## Get User Information

```
GET /me
```

Description: This endpoint is used to retrieve the user information of the currently authenticated user.

Query Parameters: None

Example Response:

```
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

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

## Generate Verification Code

```
POST /me/profile/phone/verification-code
```

Description: This endpoint is used to generate a verification code for a user's phone number.

Query Parameters: None

Example Response:

```
{
    message: "Created verification code",
    user: <user_id>,
    type: "phone",
    data: <phone_number>
}
```

## Update User Phone Endpoint

```
PUT /me/profile/phone
```

Description: This endpoint updates the phone number of the user in the database.

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
POST /endpoint/path
```
Description: This endpoint is used to process webhooks.

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