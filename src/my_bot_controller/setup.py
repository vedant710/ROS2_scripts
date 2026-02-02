from setuptools import setup

package_name = 'my_bot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vedant',
    maintainer_email='vedantkulkarni252@gmail.com',
    description='Simple robot controller',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'simple_controller = my_bot_controller.simple_controller:main',
        ],
    },
)
