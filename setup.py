from setuptools import setup

setup(
    name='NoiseLabelDataset',
    version='0.1.1',    
    description='Support Pytorch Dataset to create Noise Label Dataset to train',
    url='https://github.com/ericabd888/NoiseLabelDataset',
    author='YUAN-CHIH YANG',
    author_email='ericabd888@gmail.com',
    license='BSD 2-clause',
    packages=['NoiseLabelDataset'],
    install_requires=['numpy',],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.6',
    ],
)