# Configure the AWS provider
provider "aws" {
  region = "us-west-2" 
}

# Create a DynamoDB table (Not for state locking)
resource "aws_dynamodb_table" "demo_table" {
  name         = "demo-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

# Create a DynamoDB table for state locking
resource "aws_dynamodb_table" "lock_table" {
  name           = "lock-table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}

# Configure the S3 backend
terraform {
  backend "s3" {
    bucket         = "statefile-b" 
    key            = "terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = aws_dynamodb_table.lock_table.name
  }
}

