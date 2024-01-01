from datetime import datetime, timedelta
def transform_report(report):
    date_report = datetime.strptime(report['date_report'], '%d/%m/%Y')
    start_day = (date_report - timedelta(days=1)).strftime('%d/%m/%Y')
    end_day = date_report.strftime('%d/%m/%Y')

    transformed_report = {
        "location": report["location"],
        "start_day": start_day,
        "end_day": end_day,
        "device": report["device"],
        "cable": report["cable"],
        "power": report["power"],
        "report": report["report"],
        "sv_power": report["sv_power"],
        "sv_cable": report["sv_cable"],
        "sv_device": report["sv_device"],
        "other_job": report["other_job"],
        "exist": report["exist"],
        "propose": report["propose"],
        "creator": report["creator"],
        "save": f"{report['location'].split('/')[1]}-{date_report.day}"
    }

    return transformed_report