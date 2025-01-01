from setuptools import setup, find_packages

setup(
    name='payment_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pydantic'
    ],
    description='A Python SDK for integrating with the payment MPESSA API.',
    author='Yohanes Mesfin',
    author_email='yohanesmesfin3@gmail.com',
    url='https://github.com/johnnas12/Mpessa_payment_sdk',  # Update with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
