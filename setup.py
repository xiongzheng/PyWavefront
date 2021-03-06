from setuptools import setup

VERSION = '0.3.1'

setup(
    name='PyWavefront',
    version=VERSION,
    author='Kurt Yoder',
    author_email='kyoder@gmail.com',
    url='https://github.com/greenmoss/PyWavefront',
    description='Python/pyglet library for importing Wavefront .obj files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows', # XP
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['pywavefront'],
    extras_require={
        'visualization': ['pyglet'],
    }
)
