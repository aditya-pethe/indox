# Endpoints 


This document provides an overview of the Cat Facts API, which provides daily cat facts to users. It outlines the available endpoints and their associated parameters and responses.

# Authentication Endpoints

## Google Authentication

```
GET /google
```
Description: This endpoint is used to authenticate a user with Google.

Query Parameters: None

## Google Authentication Callback

```
GET /google/callback
```
Description: This endpoint is used to handle the callback from the Google authentication process.

Query Parameters: None

## Google Contacts

```
GET /google/contacts
```
Description: This endpoint is used to retrieve the user's contacts from Google.

Query Parameters: None

## Google Contacts Callback

```
GET /google/contacts/callback
```
Description: This endpoint is used to handle the callback from the Google contacts process.

Query Parameters: None

## Sign Out

```
GET /signout
```
Description: This endpoint is used to sign out the user.

Query Parameters: None

# (Daily) Endpoints

## Get Daily Recipients and Fact

```
GET /daily
```
Description: This endpoint is used to get all recipients and a fact to be sent out each day.

Query Parameters: 
- code: The code to recieve recipients

## Text Message

```
POST /message
```
Description: This endpoint is used to process text messages recieved from a recipient and respond.

Query Parameters: 
- query: The text query provided
- number: The phone number of the recipient

# Data Endpoints

## GET /data

Description: Retrieves data from the Recipient, UnsubscribeDate, User, and Fact models.

Query Parameters: None

# (Contacts) Endpoints

## Get Contacts

```
GET /contacts
```
Description: Retrieves a list of contacts from the user's Google account.

Query Parameters: 
- animal_type: The type of animal for which the user is subscribing.

# Facts Endpoints

## Get Facts

```
GET /
```
Description: Retrieves a list of facts.

Query Parameters: None

## Get Submitted Facts

```
GET /me
```
Description: Retrieves a list of facts submitted by the authenticated user.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter by.

## Get Random Fact

```
GET /random
```
Description: Retrieves a random fact.

Query Parameters: 
- animal_type: A comma-separated list of animal types to filter by.
- amount: The number of facts to retrieve. Limited to 500.

## Get Fact by ID

```
GET /:factID
```
Description: Retrieves a fact by its ID.

Query Parameters: None

## Submit a Fact

```
POST /
```
Description: Submits a new fact.

Query Parameters: 
- factText: The text of the fact.
- animalType: The type of animal the fact is about.

# Authentication Endpoints

## Auth Login

```
GET /auth/login
```
Description: This endpoint is used to authenticate a user and generate a JWT token.

Query Parameters: 

## Auth Logout

```
GET /auth/logout
```
Description: This endpoint is used to log out a user and invalidate their JWT token.

Query Parameters: 

# User Endpoints

## Get User

```
GET /users/:id
```
Description: This endpoint is used to retrieve a user's information.

Query Parameters: 

## Update User

```
PUT /users/:id
```
Description: This endpoint is used to update a user's information.

Query Parameters: 

# Catbot Endpoints

## Get Catbot

```
GET /catbot/:id
```
Description: This endpoint is used to retrieve a catbot's information.

Query Parameters: 

## Update Catbot

```
PUT /catbot/:id
```
Description: This endpoint is used to update a catbot's information.

Query Parameters: 

# Recipient Endpoints

## Get Recipient

```
GET /recipients/:id
```
Description: This endpoint is used to retrieve a recipient's information.

Query Parameters: 

## Update Recipient

```
PUT /recipients/:id
```
Description: This endpoint is used to update a recipient's information.

Query Parameters: 

# Fact Endpoints

## Get Fact

```
GET /facts/:id
```
Description: This endpoint is used to retrieve a fact's information.

Query Parameters: 

## Update Fact

```
PUT /facts/:id
```
Description: This endpoint is used to update a fact's information.

Query Parameters: 

# Console Endpoints

## Get Console

```
GET /console/:id
```
Description: This endpoint is used to retrieve a console's information.

Query Parameters: 

## Update Console

```
PUT /console/:id
```
Description: This endpoint is used to update a console's information.

Query Parameters: 

# Contact Endpoints

## Get Contact

```
GET /contacts/:id
```
Description: This endpoint is used to retrieve a contact's information.

Query Parameters: 

## Update Contact

```
PUT /contacts/:id
```
Description: This endpoint is used to update a contact's information.

Query Parameters: 

# Webhook Endpoints

## Get Webhook

```
GET /webhook/:id
```
Description: This endpoint is used to retrieve a webhook's information.

Query Parameters: 

## Update Webhook

```
PUT /webhook/:id
```
Description: This endpoint is used to update a webhook's information.

Query Parameters:

# Recipients Endpoints

## Get all recipients

```
GET /
```
Description: Get all recipients

Query Parameters: 
- animal_type: String

## Get user's recipients

```
GET /me
```
Description: Get all recipients associated with the authenticated user

Query Parameters: 
- animal_type: String

## Add new recipient(s)

```
POST /
```
Description: Add one or more recipients to the authenticated user's account

Query Parameters: 
- recipients: [{ name: String, number: String }]
- animalTypes: [String<Animal>]

## Restore recipient with new subscriptions

```
PATCH /:recipientId/restore
```
Description: Restore a deleted recipient with new subscriptions

Query Parameters: 
- resubscriptions: [String<Animal>]

## Edit recipient

```
PATCH /:recipientId
```
Description: Edit a recipient's name and/or number

Query Parameters: 
- name: String
- number: String

## Unsubscribe

```
DELETE /me
```
Description: Unsubscribe the authenticated user from the service

Query Parameters: 
- verificationCode: String

## Remove one or more recipients

```
DELETE /
```
Description: Remove one or more recipients from the authenticated user's account

Query Parameters: 
- recipients: [String<RecipientId>]
- soft: Boolean

# User Endpoints

## Get User

```
GET /me
```
Description: Retrieves the user object associated with the current session.

Query Parameters: None

## Delete User

```
DELETE /me
```
Description: Deletes the user object associated with the current session.

Query Parameters: 
- verificationEmail: Email address of the user to confirm intention to delete.

## Create Verification Code

```
POST /me/profile/phone/verification-code
```
Description: Creates a verification code for the user's phone number.

Query Parameters: 
- phone: Phone number to create verification code for.

## Update Phone Number

```
PUT /me/profile/phone
```
Description: Updates the user's phone number with the provided verification code.

Query Parameters: 
- verificationCode: Verification code to confirm the phone number.

# (Webhook) Endpoints

## processWebhook

```
POST /
```
Description: This endpoint is used to process webhooks from Dialogflow. It takes in a request body and returns a response.

Query Parameters: None