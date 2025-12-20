# my first no AI program
import pandas as pd

data=pd.read_csv("data/sales.csv")
print(data.head())
print(data.tail())
print(data.shape)
print(data.columns)
print(data.info())


print("Missing values:")
print(data.isna().sum())

summary=data.describe()

with open("output/summary.txt", "w") as f:
    f.write(str(summary))

print("summary saved to output/summary.txt")




'''
print("shape:", data.shape)
print("columns:", data.columns)
print("info:", data.info())
print("describe:", data.describe())
print("unique values in 'Product':", data['Product'].unique())
print("mean of 'Sales':", data['Sales'].mean())
print("sum of 'Sales':", data['Sales'].sum())
print("max of 'Sales':", data['Sales'].max())
print("min of 'Sales':", data['Sales'].min())
print("median of 'Sales':", data['Sales'].median())
print("mode of 'Sales':", data['Sales'].mode())
print("std of 'Sales':", data['Sales'].std())
print("var of 'Sales':", data['Sales'].var())
print("cov of 'Sales':", data['Sales'].cov(data['Sales']))
print("corr of 'Sales':", data['Sales'].corr(data['Sales']))
print("skew of 'Sales':", data['Sales'].skew())
print("kurt of 'Sales':", data['Sales'].kurt())
print("quantile of 'Sales':", data['Sales'].quantile(0.5))
print("hist of 'Sales':", data['Sales'].hist())
print("boxplot of 'Sales':", data['Sales'].boxplot())
print("pie of 'Sales':", data['Sales'].pie())
print("bar of 'Sales':", data['Sales'].bar())
print("line of 'Sales':", data['Sales'].line())
print("scatter of 'Sales':", data['Sales'].scatter())
print("hexbin of 'Sales':", data['Sales'].hexbin())
print("imshow of 'Sales':", data['Sales'].imshow())
print("contour of 'Sales':", data['Sales'].contour())
print("contourf of 'Sales':", data['Sales'].contourf())
print("quiver of 'Sales':", data['Sales'].quiver())
print("streamplot of 'Sales':", data['Sales'].streamplot())
print("tricontour of 'Sales':", data['Sales'].tricontour())
print("tricontourf of 'Sales':", data['Sales'].tricontourf())
print("trimesh of 'Sales':", data['Sales'].trimesh())
print("triplot of 'Sales':", data['Sales'].triplot())
print("tripcolor of 'Sales':", data['Sales'].tripcolor())
'''



