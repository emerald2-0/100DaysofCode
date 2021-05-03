import wikipedia

def print_wiki_results(user_content):
    """
    Searching for pages that match the specified word
    """
    results = wikipedia.search(user_content)

    for result in results:
        try:
            page = wikipedia.page(results)
        except wikipedia.exceptions.DisambiguationError:
            print('Disambiguation Error')
            continue
        except wikipedia.exceptions.PageError:
            print('Page error for: ' + result)
            continue
        print(page.summary)

if __name__=='__main__':
    user_request = input("Enter a search you would like: \n")
    print_wiki_results("Requesting...\n"+ user_request)