import extraction
def init_pipeline():
    url = str(input('Enter URL...'))
    content = extraction.get_data_from_article(url)
    print(f'title: {content.get('title')} \n authors: {content.get('authors')} \n date of publishing: {content.get('publish_date')} \n content: {content.get("content")}')
init_pipeline()