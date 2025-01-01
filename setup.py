from setuptools import setup, find_packages

setup(
    name='mpesa-python',
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
    url='https://github.com/Johnnas12/mpesa_python_sdk',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires=">=3.6",
)
