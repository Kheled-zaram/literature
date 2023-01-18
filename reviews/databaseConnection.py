from sshtunnel import SSHTunnelForwarder
import oracledb as db
import pandas as pd

# def query(q):
#     # database variables
#     user = 'books'
#     password = 'books'
#     database = 'jdbc:postgresql://localhost:5432/books'
#
#     with SSHTunnelForwarder(
#             (host, 22),
#             ssh_username=ssh_username,
#             ssh_private_key=ssh_private_key,
#             remote_bind_address=(localhost, 3306)
#     ) as server:
#         conn = db.connect(host=localhost,
#                           port=server.local_bind_port,
#                           user=user,
#                           passwd=password,
#                           db=database)
#         return pd.read_sql_query(q, conn)