from pathlib import Path
from utils.excel_utils import *
import uuid

user_file = Path(__file__).parent.parent / 'data/user_credentials.xlsx'
sheet_name = 'Sheet1'


def read_user_credential():
    max_row = get_row_count(user_file, sheet_name)
    user_credential = read_single_col_open_file_once(user_file, sheet_name, 2, max_row, 1)
    # print(user_credential)
    return user_credential


def new_user_generate():
    new_site_name = f"user_{uuid.uuid1()}@mail.com"
    return new_site_name


def write_new_valid_user_credential(user):
    writing_row = get_row_count(user_file, sheet_name) + 1
    write_single_row(user_file, sheet_name, writing_row, 2, 0, user)
