import os
import pandas as pd
import regex
from pandas import DataFrame #Series,
import datetime
import numpy as np

def main():
    # Today's date
    today = datetime.datetime.today().strftime('%Y-%m-%d')

    filename_new_today = filename()[0]  #Words that will be appended today
    filename_old_DB = filename()[1]     #Words DB that created yesterday
    filename_new_DB = filename()[2]     #Words DB that will be created today (old_DB + today's new_words)
    filename_t_wordset = filename()[3]  #words set for today

    # Display rows, columns and width in full
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

    # Extract new words (.txt)(.xlsx)
    df_new_today = Ext_new_df(filename_new_today, today)

    # Read existing data (.csv)(.xlsx)
    df_old_DB =Read_old_df(filename_old_DB)

    # Join new words with old database
    df_new_DB = pd.concat([df_new_today, df_old_DB])

    # Create a column for counting how many days passed from day 1
    # Create Today with date formaat
    date_format = '%Y-%m-%d'
    today = datetime.datetime.strptime(today, date_format) #datetime.date
    df_new_DB['Date'] = pd.to_datetime(df_new_DB['Date']) #datetime64[ns]
    df_new_DB['Count'] = today - df_new_DB['Date']  #numpy.dtype[timedelta64]
    df_new_DB['Count'] = df_new_DB['Count'].dt.days + 1   #changing data type numpy.dtype[timedelta64]->numpy.dtype[int64]
    df_new_DB['Count'] = df_new_DB['Count'].apply(np.ceil)

    df_t_wordset = df_new_DB[df_new_DB['Count'].isin([1,2,3,4,7,15,30])]

    # Export todays' word set
    df_new_DB.to_csv(filename_new_DB, index = False, sep=',', encoding='utf-8-sig')
    df_t_wordset.to_csv(filename_t_wordset, index = False,  sep=',', encoding='utf-8-sig')


def filename():
    filefolder = r'C:\Users\muric\Desktop\Togae'
    today = datetime.datetime.today()
    y_day = today - datetime.timedelta(days=1)

    new_today= os.path.join(filefolder, 'test.txt')
    old_DB=os.path.join(filefolder, f'{y_day:%Y%m%d}_Dutch_DB.csv')
    new_DB=os.path.join(filefolder, f'{today:%Y%m%d}_Dutch_DB.csv')
    t_wordset=os.path.join(filefolder, f'{today:%Y%m%d}_Dutch_set.csv')

    return new_today, old_DB, new_DB, t_wordset

def Ext_new_df(filename, today):

    d_list = []
    k_list = []

    # Extract words from text file
    if filename.endswith('.txt'):
        with open(filename, encoding='utf-8')  as f:
            for line in f:
                line = line.strip()
                line = line.replace(",", ".")
                if str(';') in line:
                    x = line.find(';')
                    k_words = line[x+1:].strip()
                    d_words = line[:(x-1)].strip()
                elif line:
                    x = regex.search(r'\p{IsHangul}', line)
                    k_words = line[x.start():].strip()
                    d_words = line[:(x.start() - 1)].strip()
                else:
                    break
                d_list.append(d_words)
                k_list.append(k_words)
            word_dict = {'Dutch':d_list, 'Korean' : k_list}
    elif filename.endswith('.xlsx'):
        word_dict = pd.read_excel(filename)

    word_frame = DataFrame(word_dict)
    word_frame['Date'] = today #Column: Dutch, Korean, Date
    return word_frame

def Read_old_df(filename):
    if os.path.isfile(filename):
        if filename.endswith('.xlsx'):
            df = pd.read_excel(filename)
        elif filename.endswith('.csv'):
            df = pd.read_csv(filename,
                             engine='python',
                             encoding = 'utf_8')
    else:
        df = pd.DataFrame(columns=['Dutch','Korean','Date'])

    return df

if __name__ == '__main__':
    main()