import duckdb

con = duckdb.connect("dev.duckdb", read_only=True)

con.execute("""
    COPY (SELECT * FROM mart_missions_by_site)
    TO 'exports/mart_missions_by_site.csv' (HEADER, DELIMITER ',')
""")

con.execute("""
    COPY (SELECT * FROM mart_missions_by_site)
    TO 'exports/mart_missions_by_site.parquet' (FORMAT PARQUET)
""")

print("Export done: exports/mart_missions_by_site.csv and .parquet")