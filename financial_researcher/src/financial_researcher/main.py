#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    inputs = {
        "company": None,
        "current_year": datetime.now().year,
    }

    if company_name:=os.getenv("COMPANY_NAME"):
        inputs["company"] = company_name
    else:
        print("Error: Please set the COMPANY_NAME environment variable.")
        sys.exit(1)
    result = FinancialResearcher().crew().kickoff(inputs=inputs)
    print(result.raw)


if __name__ == "__main__":
    start_time = datetime.now()
    run()
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Execution Time: {duration}")
