import click, requests, bs4

class Code:

    def __init__(self):
        pass
    
    @staticmethod
    @click.command()
    @click.argument("search_words", nargs = -1)
    def search(search_words):

        "Search a term"

        search_term = "".join(search_words)
        
        url = "https://www.dictionary.com/browse/" + search_term
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", attrs = {"data-type": "word-definitions"})

        if content is None:

            click.echo("There is no information about this word.")
        
        else:

            content = content.text.replace(".", ". \n").replace("See more", "")
            grammar_classes = ["noun", "adjective", "adverb"]

            for x in grammar_classes:
                lenght_of_word = len(grammar_classes[grammar_classes.index(x)])

                if x == content[:lenght_of_word]:
                    content = content[lenght_of_word:]
                    
            click.echo(content)