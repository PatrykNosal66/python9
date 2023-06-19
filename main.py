import wikipediaapi
from collections import Counter


def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def read_wiki_titles(fname):
    with open(fname, 'r') as file:
        for line in file:
            yield line.strip()


def calculate_average_letter_count(fname):
    total_letter_counts = Counter()
    articles_count = 0
    titles_generator = read_wiki_titles(fname)

    for title in titles_generator:
        article = get_article(title)
        print(article)
        letter_counts = Counter(char.lower() for char in article if char.isalpha())
        total_letter_counts += letter_counts
        articles_count += 1

    if articles_count > 0:
        average_letter_counts = {letter: count / articles_count for letter, count in total_letter_counts.items()}
        return average_letter_counts
    else:
        return {}


filename = "small.txt"

average_counts = calculate_average_letter_count(filename)

for letter, count in average_counts.items():
    print(f"Average usage of letter '{letter}': {count}")
