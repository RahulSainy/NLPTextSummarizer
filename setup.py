import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_name = "NLPTextSummarizer"
AUTHOR_USER_NAME = "RahulSainy"
SRC_REPO = "NLPTextSummarizer"
AUTHOR_EMAIL = "kradekidrahul@gmail.com"

setuptools.setup(
    name=REPO_name,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A NLP package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_name}/issues"
        },
    
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where="src")
)