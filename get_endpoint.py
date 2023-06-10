import boto3


client = boto3.client('sqs')
queues = ['TRACK_QUEUE', 'VIDEO_QUEUE', 'DEAD_QUEUE']
processor = resources['PROCESSOR']


# Specify the task ARN for which you want to retrieve container information
task_arn = 'arn:aws:ecs:region:account-id:task/task-id'

# Retrieve the container information
response = ecs_client.describe_tasks(cluster='cluster-name', tasks=[task_arn])

# Get the container instance ID
container_instance_id = response['tasks'][0]['containerInstanceArn'].split('/')[-1]

print(container_instance_id)
