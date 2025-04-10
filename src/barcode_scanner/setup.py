from setuptools import find_packages, setup

package_name = 'barcode_scanner'

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
    maintainer='ino',
    maintainer_email='ino@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
   
    entry_points={
    'console_scripts': [
        'barcode_scanner_node = barcode_scanner.barcode_scanner_node:main',
        ],
    },

)
