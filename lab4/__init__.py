from dagster import Definitions, load_assets_from_modules
import lab4.assets.cwr as cwr
import lab4.assets.rwc as rwc
from lab4.jobs import *

all_assets = load_assets_from_modules([cwr, rwc])

defs = Definitions(
    assets=all_assets,
    jobs=[cwr_job, rwc_job],
    schedules=[cwr_schedule, rwc_schedule]
)