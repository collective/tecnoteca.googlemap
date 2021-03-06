# -*- coding: utf-8 -*-
"""
This module contains the tool of tecnoteca.googlemap
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.3'

long_description = (
    read('docs/README.txt')
    )

tests_require = ['zope.testing']

setup(name='tecnoteca.googlemap',
      version=version,
      description="Tecnoteca GoogleMap Plone Product",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='tecnoteca googlemap',
      author='Tecnoteca srl',
      author_email='tecnoteca@tecnoteca.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tecnoteca', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        'Products.SmartColorWidget>=1.1.5',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='tecnoteca.googlemap.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
