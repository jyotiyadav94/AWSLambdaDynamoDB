import boto3
import urllib3
import warnings
import os

# Disable specific SSL warnings
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

def lambda_handler(event, context):
    user = event["user"]
    visit_count = 0  # Initialize visit count

    # DynamoDB Client
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1',verify=False)
    table_name = os.environ["TABLE_NAME"]
    table = dynamodb.Table(table_name)

    # Get the current visit count (if exists)
    response = table.get_item(Key={"user": user})
    
    # Check if the user exists in the table
    if "Item" in response:
        visit_count = response["Item"]["visit_count"]  # Retrieve visit count from the item

    # Increment the number of visits
    visit_count += 1 

    # Put the new visit count back to DynamoDB
    table.put_item(Item={"user": user, "visit_count": visit_count})

    message = f"Hello {user}! You have visited this page {visit_count} times."
    return {"message": message}

# Testing locally
if __name__ == "__main__":
    os.environ["TABLE_NAME"] ="mytable"
    event = {"user": "pixagami"}
    print(lambda_handler(event, None))
