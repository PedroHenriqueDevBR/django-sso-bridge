from setuptools import setup, find_packages

setup(
    name="django_sso_bridge",
    packages=find_packages(include=["django_sso_bridge"]),
    version="0.1.0",
    description="Bridge to connect django project with SSO System",
    author="PedroHenriqueDevBR",
    license="Apache License 2.0",
    install_requires=[],
    url="https://github.com/PedroHenriqueDevBR/django-sso-bridge",
    author_email="pedro.henrique.particular@gmail.com",
    long_description=open("README.md").read(),
    zip_safe=False,
)
