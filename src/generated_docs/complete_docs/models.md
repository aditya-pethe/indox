# Model Documentation 

## Api Log Model

Description: This data model is used to store information about API requests.

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| host              | String        | The host of the API request. |
| body              | String        | The body of the API request. |
| clientIp          | String        | The IP address of the client making the API request. |
| originalUrl       | String        | The original URL of the API request. |
| timestamps        | Boolean       | A boolean value indicating whether or not timestamps are enabled. |
## Fact Model

Description: This data model is used to store facts about animals, such as cats and dogs. It contains information about the user, the text of the fact, the date it was sent, the type of animal, and the status of the fact.

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| user              | ObjectId      | The user associated with the fact. |
| text              | String        | The text of the fact. |
| sendDate          | Date          | The date the fact was sent. |
| type              | String        | The type of animal the fact is about. |
| status.verified   | Boolean       | Whether the fact has been verified. |
| status.feedback   | String        | Feedback about the fact. |
| status.sentCount  | Number        | The number of times the fact has been sent. |
## Message Model

Description: This data model is used to store messages sent and received by a user.

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| text              | String        | The text of the message |
| number            | String        | The phone number associated with the message |
| type              | String        | The type of message (incoming or outgoing) |
| createdAt         | Date          | The date and time the message was created |
## Recipient Model

Description: This data model is used to store information about recipients of SMS messages. It contains information such as the recipient's name, phone number, and subscriptions. 

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| name              | String        | The name of the recipient. |
| notes             | String        | Notes about the recipient. |
| number            | String        | The phone number of the recipient. |
| addedBy           | ObjectId      | The ID of the user who added the recipient. |
| subscriptions     | Array         | An array of strings containing the recipient's subscriptions. |
## UnsubscribeDate Model

Description: This data model is used to determine if a user is allowed to unsubscribe from a service. It contains two keys, start and end, which are used to define a date range. The allowUnsubscribe() method is used to determine if the current date is within the date range.

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| start             | Date          | The start date of the date range. |
| end               | Date          | The end date of the date range. |
## User Model

Description: This data model is used to store user information for an API.

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| name.first        | String        | The first name of the user. |
| name.last         | String        | The last name of the user. |
| email             | String        | The email address of the user. |
| phone             | String        | The phone number of the user. |
| photo             | String        | The URL of the user's profile photo. |
| google.id         | String        | The Google ID of the user. |
| google.accessToken| String        | The Google access token of the user. |
| google.refreshToken| String       | The Google refresh token of the user. |
| isAdmin           | Boolean       | Whether or not the user is an admin. |
| ip                | String        | The IP address of the user. |
## Verification Code Model

Description: This data model is used to store verification codes for users.

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
| code              | String        | Unique code generated for the user |
| user              | ObjectId      | Reference to the user |
| type              | String        | Type of verification code |
| data              | String        | Data associated with the verification code |
| createdAt         | Date          | Date the verification code was created |