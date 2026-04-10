import logging
import azure.functions as func

app = func.FunctionApp()


# ── Função 1: Timer Trigger ────────────────────────────────────────────────
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=True) 
def timer_trigger_z(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Função 1: Timer Trigger...')



# ── Função 2: Timer Trigger ────────────────────────────────────────────────
@app.timer_trigger(
    arg_name="timer",
    schedule="0 */5 * * * *",   
    run_on_startup=False,
    use_monitor=True,
)
def get_data(timer: func.TimerRequest) -> None:
    """Agrega KPIs diários e exporta para ADLS / Power BI."""
    if timer.past_due:
        logging.warning("daily_report está atrasado!")

    logging.info("Conectado ao DB de chamados da CorpTech...")
    # lógica de agregação → ADLS Gen2 ou Power BI Streaming Dataset




# ── Função 3: Timer Trigger ────────────────────────────────────────────────
@app.timer_trigger(
    arg_name="timer",
    schedule="0 */5 * * * *",   
    run_on_startup=False,
    use_monitor=True,
)
def daily_report(timer: func.TimerRequest) -> None:
    """Agrega KPIs diários e exporta para ADLS / Power BI."""
    if timer.past_due:
        logging.warning("daily_report está atrasado!")

    logging.info("Gerando relatório diário de chamados CorpTech...")
    # lógica de agregação → ADLS Gen2 ou Power BI Streaming Dataset
