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
        content = soup.find("section", attrs = {"data-type": "part-of-speech-module"})

        if content is None:

            click.echo("There is no information about this word.")
        
        else:

            content = content.text.replace(".", ". \n")
            click.echo(content)
