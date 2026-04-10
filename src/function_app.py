import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_1(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Executando azure function 1')

@app.timer_trigger(schedule="0 */3 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_2(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Executando azure function 2')