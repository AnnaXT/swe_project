"""
This module contains details about application.
"""
import db.db_connect as dbc

TEST_APPLICATION_NAME = 'Test application'
NAME = 'application name'
APPLICANT_NAME = 'applicant name'
APPLICANT_EMAIL = 'applicant email'
PROJECT = 'applied project'
APP_DATE = 'application date'
APP_STATUS = 'application status'
RESUME = 'resume'
TRANSCRIPT = 'transcript'
COVER_LETTER = 'cover_leter'

REQUIRED_FLDS = [NAME, APPLICANT_EMAIL, PROJECT, APP_DATE, RESUME]

APPLICATION_COLLECT = 'applicantions'
APPLICATION_KEY = 'application name'


def get_applications():
    dbc.connect_db()
    return dbc.fetch_all(APPLICATION_COLLECT)


def get_applications_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict('applicant email', APPLICATION_COLLECT)


def get_application_details(name):
    dbc.connect_db()
    return dbc.fetch_one(APPLICATION_COLLECT, {'application name': name})


def get_user_application(user_email):
    dbc.connect_db()
    return dbc.fetch_one(APPLICATION_COLLECT, {'applicant email': user_email})


def application_exists(name):
    """
    check whether or not a application exists.
    """
    return get_application_details(name) is not None


def del_application(name):
    """
    Delete a doc from db collection by its name.
    """
    return dbc.del_one(APPLICATION_COLLECT, {APPLICATION_KEY: name})


def add_application(name, appl_details):
    dbc.connect_db()
    appl_details[APPLICATION_KEY] = name
    return dbc.insert_one(APPLICATION_COLLECT, appl_details)


def main():
    applications = get_applications()
    print(f'{applications=}')
    print(f'{get_application_details(TEST_APPLICATION_NAME)=}')


if __name__ == '__main__':
    main()
