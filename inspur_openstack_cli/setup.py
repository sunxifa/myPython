from setuptools import setup, find_packages

setup(
    name = "inspur-openstack-cli",
    version = "0.2",
    packages = find_packages(),
    scripts = ['neutron/inspur-net-list','neutron/inspur-subnet-list']
)
