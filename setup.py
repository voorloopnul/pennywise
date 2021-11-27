import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='pennywise',
      version='0.0.8',
      description='pennywise - A docker based bioinformatics shape shifting tool.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Ricardo Pascal',
      author_email='voorloop@gmail.com',
      url='https://github.com/voorloopnul/pennywise',
      packages=setuptools.find_packages(),
      scripts=['pennywise'],
      python_requires='>=3.4',
      install_requires=[
             "docker == 5.0.3",
             "docopt == 0.6.2",
      ]
)