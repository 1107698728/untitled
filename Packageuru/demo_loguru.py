from loguru import  logger

logger.add("a.log",format="{time:YYYY-MM-DD at HH:mm:ss}  | {level}  |  {module}")
logger.debug("这是一条日志")
logger.info("这是一条日志")
logger.warning("这是一条日志")
logger.success("这是一条日志")
logger.error("这是一条日志")