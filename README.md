# EC2_EBS_Volume_Check
**Python lambda function that verifies that an EBS volume complies with regulations.**

We use AWS Cloud Watch and AWS Lambda Function together to manage resources in accordance with corporate policies or requirements.

When an Amazon Elastic Block Store (EBS) volume gets created, for instance, we use Amazon Cloud Watch Events to trigger a Lambda function that responds to the GP2 EBS volume and converts it to GP3.

![volume](https://github.com/ghulekomal/EC2_EBS_Volume_Check/assets/54700625/bf010d04-b3fa-4591-a393-6964ea9d0aed)

![logs](https://github.com/ghulekomal/EC2_EBS_Volume_Check/assets/54700625/6f70ae00-f162-4d2d-ae97-a7c38596dbd6)
