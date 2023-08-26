
import boto3

def get_available_regions_for_instance_type(instance_type):
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions(AllRegions=True)['Regions']]
    available_regions = []

    for region in regions:
        print(f'Checking {instance_type} instance type in region: {region} {region_list.get(region, "*")}...', end='')
        client = boto3.client('ec2', region_name=region)
        try: 
            response = client.describe_instance_type_offerings(
                LocationType='region',
                Filters=[
                    {
                        'Name': 'instance-type',
                        'Values': [
                            instance_type,
                        ]
                    },
                ]
            )

            # If the instance type is available in the region, add the region to the list
            if response['InstanceTypeOfferings']:
                available_regions.append(region)
                print('Available')
            else:
                print('Not available')
        except Exception as e:
            print(f'AuthFailure, cannot access {region}')
            continue
    
    return available_regions

region_list={"us-east-2": "US East (Ohio)",
             "us-east-1": "US East (N. Virginia)",
             "us-west-1": "US West (N. California)",
             "us-west-2": "US West (Oregon)",
             "af-south-1": "Africa (Cape Town)",
             "ap-east-1": "Asia Pacific (Hong Kong)",
             "ap-south-2": "Asia Pacific (Hyderabad)",
             "ap-southeast-3": "Asia Pacific (Jakarta)",
             "ap-southeast-4": "Asia Pacific (Melbourne)",
             "ap-south-1": "Asia Pacific (Mumbai)",
             "ap-northeast-3": "Asia Pacific (Osaka-Local)",
             "ap-northeast-2": "Asia Pacific (Seoul)",
             "ap-southeast-1": "Asia Pacific (Singapore)",
             "ap-southeast-2": "Asia Pacific (Sydney)",
             "ap-northeast-1": "Asia Pacific (Tokyo)",
             "ca-central-1": "Canada (Central)",
             "eu-central-1": "EU (Frankfurt)",
             "eu-west-1": "EU (Ireland)",
             "eu-west-2": "EU (London)",
             "eu-south-1": "Europe (Milan)",
             "eu-west-3": "EU (Paris)",
             "eu-south-2": "Europe (Spain)",
             "eu-north-1": "EU (Stockholm)",
             "eu-central-2": "Europe (Zurich)",
             "il-central-1": "Israel (Tel Aviv)",
             "me-south-1": "Middle East (Bahrain)",
             "me-central-1": "Middle East (UAE)",
             "sa-east-1": "South America (Sao Paulo)"}

# Search instance type in all available regions
instance_type = input('Enter an instance type(default: t2.micro): ') or 't2.micro'
if "." not in instance_type:
    instance_type = instance_type + ".large"
available_regions = get_available_regions_for_instance_type(instance_type)
print('\n')
print(f'The {instance_type} instance type is available in the following regions with your AWS account:')
for region in available_regions:
    print("{:<18} {:<30}".format(region, region_list.get(region, "*")))