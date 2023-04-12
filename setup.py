from setuptools import setup, find_packages

setup(
    name="django_sso_bridge",
    version="0.1",
    url="https://github.com/PedroHenriqueDevBR/django-sso-bridge",
    license="Apache License 2.0",
    author="PedroHenriqueDevBR",
    author_email="pedro.henrique.particular@gmail.com",
    description="Bridge to connect django project with SSO System",
    packages=find_packages(exclude=["tests"]),
    long_description=open("README.md").read(),
    zip_safe=False,
)
