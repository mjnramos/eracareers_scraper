#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Eracareers scraper

This program searches for new job opportunities at eracareers.pt

For more details, please refer to README.md or any other official documentation
"""


import argparse
import json
import logging
import pandas as pd
import requests

from argparse import RawTextHelpFormatter
from bs4 import BeautifulSoup
from os import path


__author__ = "Miguel Ramos"
__copyright__ = "Copyright 2020, Miguel Ramos"
__credits__ = ["Miguel Ramos"]
__license__ = "MIT"
__version__ = "1"
__maintainer__ = "Miguel Ramos"
__email__ = "mjnramos@protonmail.com"
__status__ = "Production"


# Logger configurations
log_format = logging.Formatter(("%(asctime)s [%(levelname)s] "
                                "%(name)s@%(lineno)s: %(message)s"))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(f"{__name__}.log")
file_handler.setFormatter(log_format)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)


# Execution functions
def extract_data_to_form(soup_parser, data_id):
    """From the data received, extract the security parameters, to b used on
    the next call
    """

    return soup_parser.find("input", {"id": data_id}).get("value")


def eracareers_call(page_address, form_data, jobs_found):
    """Calls the first eracareer results page"""

    page_request = requests.post(page_address, data=form_data)
    soup_parser = BeautifulSoup(page_request.content, "html.parser")

    # Get the number of pages
    pages_info = soup_parser.find_all(
        "span",
        id="TemplateInterna1__ctl0_Label1"
        )[0]

    # There are 4 bold parameters, the last one is the number of pages
    number_of_pages = int(pages_info.find_all("b")[-1].text)

    # Extract results content
    results = soup_parser.find_all("div", class_="DIVresultadoPesquisa")

    # Merge results with previous jobs found
    jobs_found.extend(results)

    # Prepare next page call
    form_data["__EVENTVALIDATION"] = extract_data_to_form(
        soup_parser,
        "__EVENTVALIDATION"
        )

    form_data["__VIEWSTATE"] = extract_data_to_form(
        soup_parser,
        "__VIEWSTATE"
        )

    # Prepare output
    output = {
        "number_of_pages": number_of_pages,
        "form_data": form_data,
        "jobs_found": jobs_found
        }

    return output


def eracareers_call_prepare(page_address):
    """Makes a regular call to eracareers.pt, to get form security fields"""

    page_request = requests.get(page_address)
    soup_parser = BeautifulSoup(page_request.content, "html.parser")

    viewstate = extract_data_to_form(
        soup_parser,
        "__VIEWSTATE"
        )

    eventvalidation = extract_data_to_form(
        soup_parser,
        "__EVENTVALIDATION"
        )

    data = {
        "TemplateInterna1:_ctl0:TextBox1": "",
        "TemplateInterna1:_ctl0:DropDownList2": 2,
        "TemplateInterna1:_ctl0:Button1": "OK",
        "__VIEWSTATE": viewstate,
        "__EVENTVALIDATION": eventvalidation,
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": ""
        }

    return data


def load_known_opportunities(file_path):
    """Load the jobids for all the opportunities in the file_path.
    Porgram uses this jobid list to indetify new opportunities.
    """

    if not path.exists(file_path):
        return []

    with open(file_path) as file:
        opportunities = json.load(file)

    return [job["id"] for job in opportunities]


def process_job(job):
    """Process a found job"""
    job_link = job.find_all("a")[0]

    this_job = {
        "id": job.get("id"),
        "link": f"http://www.eracareers.pt{job_link.get('href')}",
        "reference": job_link.text
    }

    return this_job


def save_known_opportunities(file_path, jobs):
    """Saves the found opportunities into a JSON file"""

    with open(file_path, "w") as file:
        json.dump(jobs, file)


# Run functions on direct call
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter
    )

    parser.add_argument(
        "-db",
        "--database",
        default="./all_opportunities.json",
        help="JSON file with all of the all of the opportunities that system "
             "knowns (default: ./all_opportunities.json)"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="./new_jobs.csv",
        help="Tab separated files with all the new jobs found on the run. If "
             "exists, will be overwritten (default: ./new_jobs.csv)"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s (version {__version__} | {__status__})"
    )

    args = parser.parse_args()

    # Load database
    logger.info(f"Application started from {__name__}")
    opportunities_list = load_known_opportunities(args.database)

    page_address = ("http://www.eracareers.pt/Search/index.aspx"
                    "?task=search&idc=1")

    # Call eracareers
    form_data = eracareers_call_prepare(page_address)

    # On firts call jobs_found is an empty list
    function_output = eracareers_call(page_address, form_data, [])
    number_of_pages = function_output["number_of_pages"]
    logger.info(f"Pages found: {number_of_pages}")

    form_data = function_output["form_data"]
    jobs_found = function_output["jobs_found"]

    # Loop over the remaning pages
    form_data["__EVENTTARGET"] = "TemplateInterna1$_ctl0$LinkButton2"
    del form_data["TemplateInterna1:_ctl0:Button1"]

    for i in range(2, number_of_pages+1):
        logger.debug(f"Getting results from page {i}")
        function_output = eracareers_call(page_address, form_data, jobs_found)
        form_data = function_output["form_data"]
        jobs_found = function_output["jobs_found"]

    # Loop over found jobs
    organized_jobs = list()
    new_jobs = list()

    for job in jobs_found:
        this_job = process_job(job)
        organized_jobs.append(this_job)

        if this_job["id"] not in opportunities_list:
            new_jobs.append(this_job)

    # Save database
    save_known_opportunities(args.database, organized_jobs)

    # Save new jobs
    logger.info(f"New jobs found: {len(new_jobs)}")
    new_jobs_df = pd.DataFrame(new_jobs)
    new_jobs_df.to_csv(args.output, sep="\t", index=False)
    logger.info(f"Application completed")
