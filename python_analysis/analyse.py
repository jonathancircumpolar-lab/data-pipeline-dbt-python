import duckdb
import pandas as pd
import matplotlib.pyplot as plt

con = duckdb.connect("dev.duckdb", read_only=True)

df = con.execute("SELECT * FROM mart_missions_by_site").df()

print(df.head())
print(f"\nTotal rows: {len(df)}")

table = df.pivot(index="site_id", columns="parcel_status", values="parcel_count").fillna(0)
print("\nPivot table:")
print(table)

table.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Parcel status distribution by site")
plt.xlabel("Site")
plt.ylabel("Number of parcels")
plt.tight_layout()
plt.savefig("python_analysis/chart_by_site.png")
print("\nChart saved: python_analysis/chart_by_site.png")