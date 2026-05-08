import logging
import azure.functions as func

app = func.Blueprint()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_csat(myTimer: func.TimerRequest) -> None:
    logging.info('tabela csat')
