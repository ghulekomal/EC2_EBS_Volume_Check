import boto3

def EBC_Volume_Check(volume_arn):
    splittingArn = volume_arn.split(':')
    volume_id = splittingArn[-1].split('/')[-1]
    return volume_id
    
def lambda_handler(event, context):
    volume_arn = event['resources'][0]
    volume_id = EBC_Volume_Check(volume_arn)
    
    
    ec2_client= boto3.client('ec2')
    
    response = ec2_client.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3',

)
    