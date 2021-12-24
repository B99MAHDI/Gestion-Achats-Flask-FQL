from faunadb import query as q
from faunadb.objects import Ref  
from faunadb.client import FaunaClient 
import os
import json
import re
import pandas as pd
client = FaunaClient(secret="fnAEESOdRxACBVaSmdldu8F91bMRmFah71aFZ4Yn")
#indexes = client.query(q.paginate(q.indexes()))
#myemail = "elmahdi.bahou@ensem.ac.ma"
#get_data = client.query(q.map_(q.lambda_("data",q.get(q.var("data"))) , q.paginate(q.match(q.index("login_by_email"),"myemail"))))
#get_data = client.query(q.map_(q.lambda_("data", q.get(q.var("data"))),q.paginate(q.match(q.index("achat_fournisseur_by_id"), 1 ))))
#client.query(q.map_(q.lambda_("data",q.get(q.var("data"))) , q.paginate(q.match(q.index("all_achat_fournisseur")))))
#nb = len(get_data["data"])
#get_last_data = get_data["data"][0]["data"]
#specific_table = client.query(q.map_(q.lambda_("data",q.get(q.var('data'))),q.paginate(q.match(q.index("all_tous_articles")))))
#data_specific_table = specific_table['data']
#L=[]
#for row in data_specific_table:
#    L.append(row['data'])
#nb_data = len(L)
#L.reverse()
#print(L)
"""
def convertToBinaryData(filename):
    with open(filename,  'rb') as file:
        binaryData = file.read()
    return binaryData
def encode_file(filenam):
    with open(filenam , 'r' , encoding="utf-8") as f:
        encoded_data = f.read()
    return encoded_data
"""

"""
liste = []
data = client.query(q.map_(q.lambda_("data",q.get(q.var("data"))),q.paginate(q.match(q.index("tous_articles_by_nom_table"),"Cfo Cfa Divers"))))
data_imprimer = data["data"]
for row in data_imprimer:
    data_row = [row["data"]["client"],row["data"]["designation"],row["data"]["prixunitaire"]]
    liste.append(data_row)
df_imprimer = pd.DataFrame(liste, columns=['Client', 'Désignation', 'Prix Unitaire'])
#df_imprimer.to_excel("Base_de_données_("+"Cfo Cfa Divers"+").xlsx", index=False)
encode_fi = str(df_imprimer).encode("utf8")
#excel_file = convertToBinaryData("Base_de_données_("+"Cfo Cfa Divers"+").xlsx")
#decode_excel_file = excel_file.decode("utf-8")
#excel_file = df_imprimer.encode("utf-8").strip()
get_info_tous_articles = client.query(q.map_(q.lambda_("data",q.get(q.var("data"))),q.paginate(q.match(q.index("info_tousarticles_by_nom_table"),"Cfo Cfa Divers"))))
client.query(q.update(get_info_tous_articles["data"][0]["ref"],{"data": {"enregistrement": encode_fi }}))
encode_fi = get_info_tous_articles["data"][0]["data"]["enregistrement"]
decode_fi = encode_fi.decode("utf8")
#file_bytes = file.decode('utf-8')
#st = "hello world"
#excel_file = ' '.join(format(ord(x), 'b') for x in df_imprimer)
#excel_file = ' '.join(format(x, 'b') for x in bytearray(str(df_imprimer), 'utf-8'))
#binary_values = excel_file.decode('utf-8')
print (encode_fi)
print(decode_fi)
#print(decode_excel_file)
"""
liste = []
data = client.query(q.map_(q.lambda_("data",q.get(q.var("data"))),q.paginate(q.match(q.index("tous_articles_by_nom_table"),'Cfo Cfa Divers'))))
data_imprimer = data["data"]
for row in data_imprimer:
    data_row = [row["data"]["client"],row["data"]["designation"],row["data"]["prixunitaire"]]
    liste.append(data_row)

print(liste)


#print (data)





#Create(Collection("tous_articles"),{data:{"tous_articles_id":3,"nom_table":"Plom Cvc Divers","client":"ayoub mouhajiri","designation":"responsable achat","prixunitaire":987654345678}})

#Update(Select("ref",Get(Match(Index("tous_articles_by_nom_table"), "Cfo Cfa"))),{data: { "nom_table": "Cfo Cfa Divers" }})

#Update(Select("ref",Get(Match(Index("tous_articles_by_nom_table"), "Plom Cvc"))),{data: { "nom_table": "Plom Cvc Divers" }})

#Create (Collection ("achat_fournisseur"),{data:{"achat_fournisseur_id":1,"ct_num":"MOUHAJIRI","dl_design":"Ayoub","prixunitaire":"ayoubmouhajiri99@gmail.com","commerciale":"ayoub mouhajiri","num_telephone":"03723623672","email":"ayoubmouhajiri99@gmail.com"}})

#Create (Collection ("achat_fournisseur"),{data:{"achat_fournisseur_id":2,"ct_num":"BAHOU","dl_design":"MAHDI","prixunitaire":"1999","commerciale":"bahou el mahdi","num_telephone":"0987654312221","email":"elmahdi.bahou@ensem.ac.ma"}})

#CreateIndex({name: "achat_fournisseur_desc",source: Collection("achat_fourniseeur"),values: [{ field: ["data", "first"], reverse: true },{ field: ["data"] }]})

#Map(Paginate(Match(Index('achat_fournisseur_by_num_tele'))),Lambda(['name', 'ref'], ContainsStr(Var('name'), "0")))

#Map(Paginate(Match(Index('achat_fournisseur_by_ctnum'))),Lambda(['name', 'ref'], ContainsStr(LowerCase(Var('name')), 'bah')))