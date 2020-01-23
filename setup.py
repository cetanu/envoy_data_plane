from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='envoy_data_plane',
    version='0.0.2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.7.0',
    url='https://github.com/cetanu/envoy_data_plane',
    license='MIT',
    author='Vasilios Syrakis',
    author_email='vsyrakis@atlassian.com',
    description='Python dataclasses for the Envoy Data-Plane-API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'betterproto'
    ]
)
