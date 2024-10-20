# DynamoDB Visit Counter Lambda Function

This project is an AWS Lambda function that tracks how many times a specific user has visited a page. It uses **AWS DynamoDB** to store and retrieve the visit count for each user. The function increments the visit count every time it is invoked and returns a personalized message to the user with the updated visit count.

## How it Works

1. The function receives an event that contains the `user` attribute (username).
2. It retrieves the current visit count for the user from a DynamoDB table.
3. If the user exists in the table, it increments their visit count. If the user is new, the count starts at 1.
4. The updated visit count is saved back to DynamoDB.
5. A message is returned, informing the user of how many times they have visited the page.

## Setup Instructions

### Prerequisites

- Python 3.x
- AWS account with DynamoDB access
- AWS credentials configured locally (e.g., using `aws configure`)
- DynamoDB table created with `user` as the primary key

### Environment Variables

Make sure to set the environment variable `TABLE_NAME` in your AWS Lambda environment or locally:

### Running Locally

1. Install the required dependencies:

   ```bash
   pip install boto3
   ```
Set the TABLE_NAME environment variable in your terminal or directly in the code.

To test the function locally:
```bash
python lambda_function.py
```
