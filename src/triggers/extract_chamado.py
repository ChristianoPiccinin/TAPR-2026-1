import logging
import azure.functions as func
import os
import pyodbc
import json


app = func.Blueprint()

@app.timer_trigger(schedule="0 */2 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado(myTimer: func.TimerRequest) -> None:

    logging.info("Iniciando leitura da tabela itsm.chamado")
 
    server = os.getenv("SQL_SERVER")
    database = os.getenv("SQL_DATABASE")
    username = os.getenv("SQL_USER")
    password = os.getenv("SQL_PASSWORD")


    logging.info(f"Server: {server}, Database: {database}, User: {username}, Password: {password}")


    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    query = """
        SELECT TOP (100) *
        FROM itsm.chamado
    """

    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(query)

            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            data = [
                dict(zip(columns, row))
                for row in rows
            ]

            # logging.info(
            #     json.dumps(data, default=str, ensure_ascii=False)
            # )

            logging.info(f"rows: {data[:5]}")  # Loga apenas os primeiros 5 registros para evitar excesso de log
            #logging.info(f"Total de registros lidos: {len(data)}")

    except Exception as e:
        logging.error(f"Erro ao ler itsm.chamado: {str(e)}")
        raise