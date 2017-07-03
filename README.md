# Simple ecommerce webscrapper

This is a simple wikipedia webscrapper as well as a jupyter notebook file showcasing the initial exploration of the scrapped pages.

## Dependencies

I recommend you use anaconda, more info on: https://anaconda.org/.

After installing conda you can create a virtual environment as follows:

```
conda env create -f environment.yml
source activate wikipedia_env
```

Another option is to install needed packages with your favorite third-party package manager, like pip for example:
```
pip install -r requirements.txt
```

## Usage

The crawler
```
scrapy crawl wiki
```

The notebook
```
jupyter notebook
```
