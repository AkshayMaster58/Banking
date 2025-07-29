output "raw_bucket" {
  value = aws_s3_bucket.raw_data.bucket
}

output "processed_bucket" {
  value = aws_s3_bucket.processed_data.bucket
}