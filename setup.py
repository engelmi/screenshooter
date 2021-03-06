from distutils.core import setup
setup(
    name = 'ScreenShooter',
    packages = ['screenshooter'],
    version = '0.10',
    license='MIT',
    description = 'Simple screenshot tool',
    author = 'Michael Engel',
    author_email = 'engel.michael@hotmail.de',
    url = 'https://github.com/engelmi/screenshooter',
    download_url = 'https://github.com/engelmi/screenshooter/archive/v_10.tar.gz',
    keywords = ['Screen', 'Screen Shot', 'Shortcut', 'Keyboard', 'Hook'],
    install_requires=[
        'keyboard',
        'mss',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)