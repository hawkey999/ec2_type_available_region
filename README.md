# ec2_type_available_region
Check a ec2 type availability in all aws regions

## How to Use
```
python3 list-ec2-all-available-region.py

Enter an instance type(default: t2.micro): t2.micro
```
## Example return
```Checking t2.micro instance type in region: ap-south-2 Asia Pacific (Hyderabad)...AuthFailure, cannot access ap-south-2  
Checking t2.micro instance type in region: ap-south-1 Asia Pacific (Mumbai)...Available  
Checking t2.micro instance type in region: eu-south-1 Europe (Milan)...AuthFailure, cannot access eu-south-1 
Checking t2.micro instance type in region: eu-south-2 Europe (Spain)...AuthFailure, cannot access eu-south-2  
Checking t2.micro instance type in region: me-central-1 Middle East (UAE)...AuthFailure, cannot access me-central-1
Checking t2.micro instance type in region: il-central-1 Israel (Tel Aviv)...AuthFailure, cannot access il-central-1
Checking t2.micro instance type in region: ca-central-1 Canada (Central)...Available
Checking t2.micro instance type in region: eu-central-1 EU (Frankfurt)...Available
Checking t2.micro instance type in region: eu-central-2 Europe (Zurich)...AuthFailure, cannot access eu-central-2
Checking t2.micro instance type in region: us-west-1 US West (N. California)...Available
Checking t2.micro instance type in region: us-west-2 US West (Oregon)...Available
Checking t2.micro instance type in region: af-south-1 Africa (Cape Town)...AuthFailure, cannot access af-south-1
Checking t2.micro instance type in region: eu-north-1 EU (Stockholm)...Not available
Checking t2.micro instance type in region: eu-west-3 EU (Paris)...Available
Checking t2.micro instance type in region: eu-west-2 EU (London)...Available
Checking t2.micro instance type in region: eu-west-1 EU (Ireland)...Available
Checking t2.micro instance type in region: ap-northeast-3 Asia Pacific (Osaka-Local)...Available
Checking t2.micro instance type in region: ap-northeast-2 Asia Pacific (Seoul)...Available
Checking t2.micro instance type in region: me-south-1 Middle East (Bahrain)...AuthFailure, cannot access me-south-1
Checking t2.micro instance type in region: ap-northeast-1 Asia Pacific (Tokyo)...Available
Checking t2.micro instance type in region: sa-east-1 South America (Sao Paulo)...Available
Checking t2.micro instance type in region: ap-east-1 Asia Pacific (Hong Kong)...Not available
Checking t2.micro instance type in region: ap-southeast-1 Asia Pacific (Singapore)...Available
Checking t2.micro instance type in region: ap-southeast-2 Asia Pacific (Sydney)...Available
Checking t2.micro instance type in region: ap-southeast-3 Asia Pacific (Jakarta)...AuthFailure, cannot access ap-southeast-3
Checking t2.micro instance type in region: ap-southeast-4 Asia Pacific (Melbourne)...AuthFailure, cannot access ap-southeast-4
Checking t2.micro instance type in region: us-east-1 US East (N. Virginia)...Available
Checking t2.micro instance type in region: us-east-2 US East (Ohio)...Available


The t2.micro instance type is available in the following regions with your AWS account:
ap-south-1         Asia Pacific (Mumbai)         
ca-central-1       Canada (Central)              
eu-central-1       EU (Frankfurt)                
us-west-1          US West (N. California)       
us-west-2          US West (Oregon)              
eu-west-3          EU (Paris)                    
eu-west-2          EU (London)                   
eu-west-1          EU (Ireland)                  
ap-northeast-3     Asia Pacific (Osaka-Local)    
ap-northeast-2     Asia Pacific (Seoul)          
ap-northeast-1     Asia Pacific (Tokyo)          
sa-east-1          South America (Sao Paulo)     
ap-southeast-1     Asia Pacific (Singapore)      
ap-southeast-2     Asia Pacific (Sydney)         
us-east-1          US East (N. Virginia)         
us-east-2          US East (Ohio)               
```
