import pandas as pd

#Function for get first announcement
def get_announcement(sort):

    #Condition for sort by increasing price
    if sort == 'down':
        #Init DataFrame with row counts to skip
        df = pd.read_excel('apartments.xlsx',header=None,skiprows=1, nrows=1)
        #Get values from DataFrame in list
        title = " ".join(df[0].tolist())
        links = " ".join(df[1].tolist())
        adress = " ".join(df[2].tolist())
        metro = " ".join(df[3].tolist())
        price = " ".join(map(str,df[4].tolist()))
        #Dict for announcement
        posts = f'<b>{title}\n\n\n<i><u>✅Цена: {price}</u></i>\n\n✅<i><u>Метро: {metro}</u></i>\n\n✅Адресс: <i><u>{adress}</u></i></b>\n\n\nhttps://www.avito.ru{links}'

        return posts

    #Condition for sort by decreasing price
    elif sort == 'up':
        #Get the row count in an excel file
        rows = pd.read_excel('apartments.xlsx', usecols='A').count() - 1
        #Init DataFrame with row counts to skip
        df = pd.read_excel('apartments.xlsx',header=None, skiprows=int(rows), nrows=1)
        #Get values from DataFrame in list
        title = " ".join(df[0].tolist())
        links = " ".join(df[1].tolist())
        adress = " ".join(df[2].tolist())
        metro = " ".join(df[3].tolist())
        price = " ".join(map(str,df[4].tolist()))
        #Dict for announcement
        posts = f'<b>{title}\n\n\n<i><u>✅Цена :{price}</u></i>\n\n✅<i><u>Метро: {metro}</u></i>\n\n✅<i><u>Адресс: {adress}</u></i></b>\n\n\nhttps://www.avito.ru{links}'

        return posts


#Function for get next announcement
def next_announcement(current):
    df = pd.read_excel('apartments.xlsx',header=None ,skiprows=current, nrows=1)
    title = " ".join(df[0].tolist())
    links = " ".join(df[1].tolist())
    adress = " ".join(df[2].tolist())
    metro = " ".join(df[3].tolist())
    price = " ".join(map(str,df[4].tolist()))
    posts = f'<b>{title}\n\n\n✅<i><u>Цена: {price}</u></i>\n\n✅<i><u>Метро: {metro}</u></i>\n\n✅<i><u>Адресс: {adress}</u></i></b>\n\n\nhttps://www.avito.ru{links}'

    return posts
