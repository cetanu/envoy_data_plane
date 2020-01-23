from setuptools import setup, find_packages

setup(
    name='envoy_data_plane',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/cetanu/envoy_data_plane',
    license='MIT',
    author='Vasilios Syrakis',
    author_email='vsyrakis@atlassian.com',
    description='Python dataclasses for the Envoy Data-Plane-API',
    install_requires=[
        'betterproto[compiler]'
    ]
)
