code_msg = {
    200: '成功',
    401: '请登录后再尝试',
    492: '数据不完整',
    493: '请求错误',
}

def to_dict_msg(code=200, data=None, msg=None, **kwargs):
    return {
        "code": code,
        "data": data if data else {},
        "msg": msg if msg else code_msg.get(code, "未知错误"),
        **kwargs
    }
