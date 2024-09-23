import setuptools

with open("README.md", "r", encoding="utf-̣8", errors="ignore") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "AndrewHaward2310"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "Nguyen.LD216207@sis.hust.edu.vn"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to classify kidney disease",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)