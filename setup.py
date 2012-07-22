import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'Kotti',
]

tests_require = [
    'WebTest',
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-xdist',
    'wsgi_intercept',
    'zope.testbrowser',
    ]

setup(name='kotti_notify_changes',
      version='0.1.0dev1',
      description='Kotti extension that notifies registered users about changed nodes.',
      long_description='\n\n'.join([README, CHANGES]),
      classifiers=[
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Development Status :: 5 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Framework :: Pylons',
      ],
      author='Christian Neumann',
      author_email='cneumann@datenkarussell.de',
      url='https://github.com/chrneumann/kotti_notify_changes',
      license="BSD3",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={
          'testing': tests_require,
      },
      )
