from distutils.core import setup

setup(
    name='b64',
    packages=['b64'],
    version='0.4',
    license='MIT',
    description='convert html/local/online data to base64 fast, easy and clean',
    author='n0x1s',
    author_email='n0x1s0x01@gmail.com',
    url='https://github.com/n0x1s/b64',
    download_url='https://github.com/N0x1s/b64/archive/0.4.tar.gz',
    keywords=['base64', 'image to base64', 'video to base64',
              'base64 convert', 'html to base64', 'data uri'],
    install_requires=[
          'requests',
          'bs4',
		  'lxml',
          'cached_properties',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
