import boto3


def extractVolumeId(volume_arm):
    arm_parts = volume_arm.split(":")
    volume_id = arm_parts[-1].split("/")[-1]
    return volume_id
    

def lambda_handler(event, context):
    # TODO implement
    
    print(event)
    
    volume_arm = event['resources'][0]
    volume_id = extractVolumeId(volume_arm)
    
    client = boto3.client('ec2')
    
    response = client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3'
    )
    
    
