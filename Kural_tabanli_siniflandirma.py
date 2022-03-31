#csv dosyasını okutup genel bilgileri gösteriyoruz
import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv('data/persona.csv')
df.head()
df.shape
df.info()
df.describe().T
df.isnull().sum()

#ortalama kazançları öğreniyoruz
df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"})

#çıktıyı daha iyi görebilmek için sıralama yapıyoruz ve agg_df olarak kaydediyoruz
agg_df = df.groupby(by=["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

#indexteki isimleri değişken ismine değiştiriyoruz
agg_df = agg_df.reset_index()
agg_df.head()

#AGE değişkeninin kategorik değişkene çeviriyoruz ve AGE değişkenini bölüyoruz
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

#yeni seviye müşterileri tanımlayarak veri setinde değişken olarak ekliyoruz
agg_df.columns
for row in agg_df.values:
    print(row)

[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]

agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()

agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))

#birçok farklı segment olabileceği için segmentleri tekilleştiriyoruz
agg_df["customers_level_based"].value_counts()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df = agg_df.reset_index()
agg_df.head()

agg_df["customers_level_based"].value_counts()
agg_df.head()

#müşterileri segmentlere ayırıyoruz
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

















































