from distutils.core import setup

setup(
    name='trunity_3_client',
    version='0.1',
    packages=[
        'trunity_3_client',
    ],
    install_requires=[
        'requests',
        'beautifulsoup4',
      ],
    url='',
    license='MIT',
    author='hunting',
    author_email='VicHuntig@yandex.ua',
    description='API client for Trunity 3 learning platform and more'
)
