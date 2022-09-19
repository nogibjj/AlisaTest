from databricks import sql
import os


def querydb(query="American"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT Name FROM default.artists_1_csv WHERE Nationality="+query+"DESC")
            result = cursor.fetchall()

        for row in result:
            print(row)
    return result
