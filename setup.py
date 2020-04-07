from setuptools import setup

setup(
    name='ec2-snapshotter',
    version='0.1',
    author='Iani Stamenov',
    author_email='stamenov@udel.edu',
    description='EC2-Snapshotter is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/yawny-tsunami/EC2-Snapshotter',
    install_requires=[
    'click',
    'boto3'

    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
        
)
