import boto3

session = boto3.Session()


ec2_client = session.client('ec2')
s3_client = session.client('s3')


def list_ec2_instance():
    response = ec2_client.describe_instances()
    for reser in response['Reservations']:
        for ins in reser['Instances']:
            print(f"ID: {ins['InstanceId']} | Type: {ins['InstanceType']} | Private IP: {ins['PrivateIpAddress']} | Public IP: {ins['PublicIpAddress']} | Status: {(ins['State'])['Name']}")
            
            
def tag_ec2_ins(ins_id, tags):
    try:
        ec2_client.create_tags(
            Resources=[ins_id], Tags = tags
        )  
        print(f"Instance {ins_id} successfully tagges with {tags}")
    except Exception as e:
        print(f"Error tagging instance {ins_id}: {e}")
        

if __name__ == '__main__':
    print("EC2 list: ")
    list_ec2_instance()
    ins_id = input("Enter EC2 Instance Id: ")
    
    tags = []
    while True:
        tag_key = input("Enter tag key (leave empty to stop): ").strip()
        if not tag_key:
            break
        tag_value = input(f"Enter value for {tag_key}: ").strip()
        tags.append({'Key': tag_key, 'Value': tag_value})

if ins_id and tags:
    tag_ec2_ins(ins_id, tags)
else:
    print("Instance ID and tags cannot be empty. Please provide valid inputs.")

