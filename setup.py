#!/usr/bin/env python

from distutils.core import setup
import os

setup(name='django-chatbox',
      version='1.0',
      description='Django chat application written using Hookbox',
      author='Andrii Kurinnyi',
      author_email='andrew@marpasoft.com',
      url='http://github.com/marpasoft/django-chatbox',
      packages=['chatbox',],
      keywords=['django', 'chat', 'hookbox', 'comet'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Framework :: Django',
      ],
      long_description=open(
          os.path.join(os.path.dirname(__file__), 'README.rst'),
      ).read().strip(),
)
