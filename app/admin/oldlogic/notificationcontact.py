# coding: utf8
from app.common.util.input_checker import param_err, check_exist, check_len, check_is_email, check_is_str


def add_contact_action(params):
    email = params.get('email')
    comment = params.get('comment')

    if not check_exist(email) or not check_is_email(email):
        return param_err('邮箱')
    if not check_exist(comment):
        return param_err('备注')

    return {'type': True}
