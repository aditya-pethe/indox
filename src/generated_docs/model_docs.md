
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