import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='ditto',
      version='0.0.1',
      description='ditto - Tool to incorporate bioinformatic tools using docker.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Ricardo Pascal',
      author_email='voorloop@gmail.com',
      url='https://github.com/voorloopnul/ditto',
      packages=setuptools.find_packages(),
      python_requires='>=3.4',
      )