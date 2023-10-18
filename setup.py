from setuptools import setup,find_packages
hypen="-e."
def get_requirements(file_path:str):
    with open(file_path) as file:
        lines=file.readlines()
        requirements=[line.split("\n")[0] for line in lines]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements


setup(
    name="metro interstate",version="0.0.2",
    author="SAEED",author_email="saidshaikh.nagar@gmail.com",
    packages=find_packages(),install_requires=get_requirements("requirements.txt")
)
