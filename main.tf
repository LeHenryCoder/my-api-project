
# This part is the EC2

provider "aws" {
  region = "us-east-2"  # Replace with the appropriate region
}



resource "aws_instance" "api_server" {
  ami           = "ami-048e636f368eb3006"  # Your selected AMI ID
  instance_type = "t2.micro"  # Choose an instance type that suits your needs



  tags = {
    Name = "API Server"
  }
}
