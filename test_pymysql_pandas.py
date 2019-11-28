import pandas as pd
import pymysql
import pdb

a = pymysql.connect(
    host="192.168.16.16",
    port=3106,
    user="root",
    passwd="root",
    db="pandas_exercise",
    use_unicode=True,
    charset="utf8",
)

# sql='select %s from %s where month(last_update)=%s limit 100'%('last_update','acct_info201609',10)

SQL = """
SELECT
		*
	FROM
		collection
	WHERE
		create_time_str = "2019-05-13"
	# AND
	# 	collection_id = "456124561234"
"""


d = pd.read_sql(SQL, con=a)
a.close()
print(d)


print(d.groupby("collection_id").collection_result.last())
print(d.groupby("collection_id").tel_length.sum())

f = d.groupby("collection_id")

e = pd.concat([f.collection_result.last(), f.tel_length.sum()], axis = 1)

pdb.set_trace()