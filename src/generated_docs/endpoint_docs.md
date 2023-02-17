
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

Description: This endpoint is used to update the user's Google access token and refresh token after they have authenticated with Google.

Query Parameters: 
- `code`: The authorization code returned from Google after authentication.
- `state`: The state of the application before authentication.

Example Response:

```json
{
    "state": {
        "key": "value"
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