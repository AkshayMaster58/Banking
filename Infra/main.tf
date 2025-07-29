provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw_data" {
  bucket = "banking-raw-data"
  force_destroy = true
}

resource "aws_s3_bucket" "processed_data" {
  bucket = "banking-processed-data"
  force_destroy = true
}