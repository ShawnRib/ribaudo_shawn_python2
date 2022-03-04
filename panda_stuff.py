import pandas as pd
import sqlalchemy as sq

con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/puppies')
df = pd.read_sql('puppies', con)
print(df)

# read only
df = pd.read_sql('puppies', con, columns=['name', 'owner'])
print(df)

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
