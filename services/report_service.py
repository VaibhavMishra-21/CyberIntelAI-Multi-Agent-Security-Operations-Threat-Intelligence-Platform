from datetime import datetime

class ReportService:

    @staticmethod
    def save_report(report):

        filename = (
            f"reports/security_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        return filename
