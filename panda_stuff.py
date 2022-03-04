import pandas as pd
import sqlalchemy as sq

con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/puppies')
df_owner = pd.read_sql('owners', con)
print(df_owner)

# read only
#df_puppies = pd.read_sql('puppies', con, columns=['name', 'owner'])
df_puppies = pd.read_sql('puppies', con)
print(df_puppies)


df_fur_group = df_puppies.groupby('color_fur')
print(df_fur_group.count())
total_row_puppies = df_puppies.shape[0]
total_row_owner = df_owner.shape[0]
print('Total row for puppies table: ' + str(total_row_puppies))
print('Total row for owners table: ' + str(total_row_owner))
print('Total number of column in puppies table: ' + str(df_puppies.shape[1]))
print('Total number of column in owners table: ' + str(df_owner.shape[1]))
'''
# select name FROM puppies where name='asdf';

df = pd.read_sql('select name FROM puppies where name="Fire"', con)
print(df)

# write to sql for puppies
puppies_list=pd.DataFrame({
        "name": ['Fish', "Fire", "Wind", "Earth", "Water", "Neo", "Rock", "Joker", "Ginger", "Ziggy"],
        "color_fur": ['brown','white','black','brown','white','black','white','white','white','black'],
        "owner": [1,2,3,4,5,6,7,8,9,10]})

#write to sql for owners
oweners_list=pd.DataFrame({
        "name": ['Shawn', "Tyler", "Catherine", "Robin", "David", "Andrew", "Sophia", "Carl", "Caleb", "Todd"],
        "puppy_id": [1,2,3,4,5,6,7,8,9,10]})

puppies_list.to_sql('puppies',con, if_exists="append", index=False)
oweners_list.to_sql('owners',con, if_exists="append", index=False)

'''