#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

setup_params = dict(
	name='pytest-runner',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	url="https://bitbucket.org/jaraco/pytest-runner",
	description="Invoke py.test as distutils command with dependency "
		"resolution.",
	py_modules = ['ptr'],
	zip_safe=True,
	entry_points = {
		'distutils.commands': [
			'ptr = ptr:PyTest',
			'pytest = ptr:PyTest',
		],
	},
	license = 'MIT',
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	setup_requires=[
		'hgtools',
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
