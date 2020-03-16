'''
List Documents from regulations.api
'''

def jformat(documents):
    '''
    Format String of JSON document
    '''
    formatted = json.dumps(documents, sort_keys=True, indent=4)
    return formatted
