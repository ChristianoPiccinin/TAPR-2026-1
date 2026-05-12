import logging
import azure.functions as func
import os

app = func.Blueprint()


@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela sla')
    logging.info(f'{os.getenv("SQL_SERVER_SOURCE")}')
    