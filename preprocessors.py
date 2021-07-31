def remove_pun(chatbot,statement):
    statement.text = statement.text.replace('-', '')
    statement.text = statement.text.replace(',', '')
    statement.text = statement.text.replace('?', '')
    statement.text = statement.text.replace('.', '')
    statement.text = statement.text.replace('/', '')
    statement.text = statement.text.replace('%', '')
    statement.text = statement.text.replace('"', '')
    statement.text = statement.text.replace('#', '')
    statement.text = statement.text.replace('*', '')
    statement.text = statement.text.replace('^', '')
    statement.text = statement.text.lower()


    # statement.text = statement.text.replace('how ', '')
    # statement.text = statement.text.replace('what ', '')
    # statement.text = statement.text.replace('is ','')
    # statement.text = statement.text.replace('who ','')
    # statement.text = statement.text.replace('', 'hello')
    print(statement)
    return statement