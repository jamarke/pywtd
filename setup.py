import setuptools

setuptools.setup(
    name="py-wtd",
    version="0.1.0",
    url="https://github.com/jamarke/py-wtd",

    author="jamarke",
    author_email="tacocorporation@protonmail.com",

    description="A minimal python interface to the www.worldtradingdata.com API",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['pandas>0.22.0',
                      'requests>2.18.4'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6'
    ],
)
