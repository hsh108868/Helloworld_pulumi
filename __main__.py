"""An AWS Python Pulumi program"""
import pulumi
import pulumi_aws as ec2


size = 't2.micro'
ami = ec2.get_ami(most_recent=True,
        owners=[""])
