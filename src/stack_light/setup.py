from setuptools import find_packages, setup

package_name = 'stack_light'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='innogarage',
    maintainer_email='innogarage@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
     entry_points={
        'console_scripts': [
            'stack_light_node = stack_light.stack_light_node:main',
        ],
    },
)
